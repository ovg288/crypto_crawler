# FIXME NOTE: from dao import * doesnt work and lead to circular import hell. Still not sure how to tackle it properly
import dao

from data_access.classes.WorkUnit import WorkUnit
from data_access.message_queue import DEAL_INFO_MSG, DEBUG_INFO_MSG, ORDERS_MSG, FAILED_ORDERS_MSG

from debug_utils import print_to_console, LOG_ALL_ERRORS, LOG_ALL_MARKET_NETWORK_RELATED_CRAP, ERROR_LOG_FILE_NAME
from constants import DEAL_MAX_TIMEOUT

from enums.deal_type import DEAL_TYPE
from enums.exchange import EXCHANGE
from enums.status import STATUS

from utils.currency_utils import get_currency_pair_name_by_exchange_id, split_currency_pairs, get_currency_name_by_id
from utils.file_utils import log_to_file
from utils.key_utils import get_key_by_exchange
from utils.string_utils import float_to_str
from utils.time_utils import get_now_seconds_utc

# FIXME NOTE - global variables are VERY bad
# is it for SINGLE arbitrage process only, not overall!
overall_profit_so_far = 0.0


def init_deal(trade_to_perform, debug_msg):
    res = STATUS.FAILURE, None
    try:
        if trade_to_perform.trade_type == DEAL_TYPE.SELL:
            res = dao.sell_by_exchange(trade_to_perform)
        else:
            res = dao.buy_by_exchange(trade_to_perform)
    except Exception, e:
        msg = "init_deal: FAILED ERROR WE ALL DIE with following exception: {excp} {dbg}".format(excp=str(e),
                                                                                                 dbg=debug_msg)
        print_to_console(msg, LOG_ALL_ERRORS)
        log_to_file(msg, ERROR_LOG_FILE_NAME)

    return res


def init_deals_with_logging(trade_pairs, difference, file_name, msg_queue):
    global overall_profit_so_far

    first_deal = trade_pairs.deal_1
    second_deal = trade_pairs.deal_2

    if second_deal.exchange_id == EXCHANGE.KRAKEN:
        # It is hilarious but if deal at kraken will not succeeded no need to bother with second exchange
        first_deal = trade_pairs.deal_2
        second_deal = trade_pairs.deal_1

    # market routine
    debug_msg = "Deals details: " + str(first_deal)
    result_1 = init_deal(first_deal, debug_msg)

    first_deal.execute_time = get_now_seconds_utc()

    if result_1[0] != STATUS.SUCCESS:
        msg = "Failing of adding FIRST deal! {deal}".format(deal=str(first_deal))
        print_to_console(msg, LOG_ALL_ERRORS)
        log_to_file(msg, ERROR_LOG_FILE_NAME)
        return STATUS.FAILURE

    debug_msg = "Deals details: " + str(second_deal)
    result_2 = init_deal(second_deal, debug_msg)

    second_deal.execute_time = get_now_seconds_utc()

    if result_1[0] == STATUS.FAILURE or result_2[0] == STATUS.FAILURE:
        msg = "Failing of adding deals! {deal_pair}".format(deal_pair=str(trade_pairs))
        print_to_console(msg, LOG_ALL_ERRORS)
        log_to_file(msg, ERROR_LOG_FILE_NAME)
        return STATUS.FAILURE

    overall_profit_so_far += trade_pairs.current_profit

    msg = "Some deals sent to exchanges. Expected profit: {cur}. Overall: {tot} Difference in percents: " \
          "{diff} Deal details: {deal}".format(cur=float_to_str(trade_pairs.current_profit),
                                               tot=float_to_str(overall_profit_so_far),
                                               diff=difference, deal=str(trade_pairs))

    print_to_console(msg, LOG_ALL_MARKET_NETWORK_RELATED_CRAP)
    log_to_file(trade_pairs, file_name)

    msg_queue.add_message(DEAL_INFO_MSG, msg)

    return STATUS.SUCCESS


def init_deals_with_logging_speedy_fake(trade_pairs, difference, file_name, processor):
    pass


def return_with_no_change(json_document, corresponding_trade):

    corresponding_trade.execute_time = get_now_seconds_utc()

    try:
        corresponding_trade.deal_id = dao.parse_deal_id(corresponding_trade.exchange_id, json_document)
    except:
        log_to_file("Cant parse deal_id! for following document", "parce_deal_id.log")
        log_to_file(json_document, "parce_deal_id.log")

    return json_document, corresponding_trade


def init_deals_with_logging_speedy(trade_pairs, difference, file_name, processor, msg_queue):

    # FIXME move after deal placement ?

    global overall_profit_so_far
    overall_profit_so_far += trade_pairs.current_profit

    base_currency_id, dst_currency_id = split_currency_pairs(trade_pairs.deal_1.pair_id)

    msg = """We try to send following deals to exchange.
        <b>Expected profit in {base_coin}:</b> <i>{cur}</i>.
        <b>Overall:</b> <i>{tot}</i>
        <b>Difference in percents:</b> <i>{diff}</i>

                Deal details:
        {deal}
        """.format(base_coin=get_currency_name_by_id(base_currency_id), cur=float_to_str(trade_pairs.current_profit),
                   tot=float_to_str(overall_profit_so_far), diff=difference, deal=str(trade_pairs))

    msg_queue.add_message(DEAL_INFO_MSG, msg)
    log_to_file(msg, file_name)

    parallel_deals = []

    for order in [trade_pairs.deal_1, trade_pairs.deal_2]:
        method_for_url = dao.get_method_for_create_url_trade_by_exchange_id(order)
        # key, pair_name, price, amount
        key = get_key_by_exchange(order.exchange_id)
        pair_name = get_currency_pair_name_by_exchange_id(order.pair_id, order.exchange_id)
        post_details = method_for_url(key, pair_name, order.price, order.volume)
        constructor = return_with_no_change

        wu = WorkUnit(post_details.final_url, constructor, order)
        wu.add_post_details(post_details)

        parallel_deals.append(wu)

    res = processor.process_async_post(parallel_deals, DEAL_MAX_TIMEOUT)

    if res is None:
        log_to_file("For TradePair - {tp} result is {res}".format(tp=trade_pairs, res=res), file_name)
        log_to_file("For TradePair - {tp} result is {res}".format(tp=trade_pairs, res=res), ERROR_LOG_FILE_NAME)
        return

    # check for errors only
    for entry in res:
        json_responce, order = entry
        if "ERROR" in json_responce:

            msg = """   <b>ERROR: </b>NONE 
            During deal placement: {u1} 
            Details: {err_msg}
            """.format(u1=order, err_msg=json_responce)

            msg_queue.add_order(FAILED_ORDERS_MSG, order)

        else:
            msg = """ For trade {trade}
            Response is {resp} """.format(trade=order, resp=json_responce)

        print_to_console(msg, LOG_ALL_ERRORS)
        msg_queue.add_message(DEBUG_INFO_MSG, msg)
        log_to_file(msg, file_name)

    for order in [trade_pairs.deal_1, trade_pairs.deal_2]:
        msg_queue.add_order(ORDERS_MSG, order)