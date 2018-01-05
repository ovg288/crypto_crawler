from kraken.constants import KRAKEN_GET_OHLC

from data.Candle import Candle

from debug_utils import should_print_debug

from data_access.internet import send_request

from enums.status import STATUS

from debug_utils import print_to_console, LOG_ALL_DEBUG


def get_ohlc_kraken_url(currency, date_start, date_end, period):
    # https://api.kraken.com/0/public/OHLC?pair=XXRPXXBT&since=1501520850&interval=15
    final_url = KRAKEN_GET_OHLC + currency + "&since=" + str(date_start) + \
                "&interval=" + str(period)

    if should_print_debug():
        print_to_console(final_url, LOG_ALL_DEBUG)

    return final_url


def get_ohlc_kraken_result_processor(json_responce, currency, date_start, date_end):
    result_set = []

    if json_responce is not None and "result" in json_responce:
        if currency in json_responce["result"]:
            # "result":{"XXRPXXBT":[[1500873300,"0.00007037","0.00007055","0.00007012","0.00007053","0.00007035","104062.41283454",17],
            # [1500874200,"0.00007056","0.00007071","0.00007006","0.00007007","0.00007041","90031.72579746",33],
            for record in json_responce["result"][currency]:
                result_set.append(Candle.from_kraken(record, currency))

    return result_set


def get_ohlc_kraken(currency, date_start, date_end, period):
    result_set = []

    final_url = get_ohlc_kraken_url(currency, date_start, date_end, period)

    err_msg = "get_ohlc_kraken called for {pair} at {timest}".format(pair=currency, timest=date_start)
    error_code, r = send_request(final_url, err_msg)

    if error_code == STATUS.SUCCESS and r is not None and "result" in r:
        if currency in r["result"]:
            # "result":{"XXRPXXBT":[[1500873300,"0.00007037","0.00007055","0.00007012","0.00007053","0.00007035","104062.41283454",17],
            # [1500874200,"0.00007056","0.00007071","0.00007006","0.00007007","0.00007041","90031.72579746",33],
            for record in r["result"][currency]:
                result_set.append(Candle.from_kraken(record, currency))

    return result_set
