# ticker urls
POLONIEX_GET_TICKER = "https://poloniex.com/public?command=returnTicker"  # Yeah, it just return EVERYTHING

# OHLC ~ canddle stick urls
#  https://poloniex.com/public?command=returnChartData&currencyPair=BTC_XMR&start=1405699200&end=9999999999&period=14400
POLONIEX_GET_OHLC = "https://poloniex.com/public?command=returnChartData&currencyPair="

#       FIXME NOTE - depth can vary
# https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_NXT&depth=10, depth optional
POLONIEX_GET_ORDER_BOOK = "https://poloniex.com/public?command=returnOrderBook&currencyPair="

# https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_NXT&start=1501693512&end=1501693572
POLONIEX_GET_HISTORY = "https://poloniex.com/public?command=returnTradeHistory&currencyPair="

POLONIEX_CURRENCY_PAIRS = ["BTC_DASH", "BTC_ETH", "BTC_LTC", "BTC_XRP", "BTC_ETC", "BTC_SC", "BTC_DGB", "BTC_XEM",
                           "BTC_ARDR", "BTC_BCH", "BTC_OMG", "BTC_ZEC", "BTC_REP", "BTC_XMR", "BTC_DOGE", "BTC_ZRX",
                           "BTC_GAS", "BTC_STRAT", "BTC_STR", "BTC_LSK",
                           "ETH_ETC", "ETH_BCH", "ETH_OMG", "ETH_ZEC", "ETH_REP", "ETH_ZRX", "ETH_GAS", "ETH_LSK",
                           "USDT_DASH", "USDT_BTC", "USDT_ETH", "USDT_LTC", "USDT_XRP", "USDT_ETC", "USDT_BCH",
                           "USDT_ZEC", "USDT_REP", "USDT_XMR", "USDT_STR"]

POLONIEX_TRADING_API = "https://poloniex.com/tradingApi"

POLONIEX_CANCEL_ORDER = POLONIEX_TRADING_API
POLONIEX_BUY_ORDER = POLONIEX_TRADING_API
POLONIEX_SELL_ORDER = POLONIEX_TRADING_API
POLONIEX_CHECK_BALANCE = POLONIEX_TRADING_API
POLONIEX_GET_OPEN_ORDERS = POLONIEX_TRADING_API
POLONIEX_GET_ORDER_HISTORY = POLONIEX_TRADING_API

POLONIEX_NUM_OF_DEAL_RETRY = 1
POLONIEX_DEAL_TIMEOUT = 5
# Default and max
POLONIEX_ORDER_HISTORY_LIMIT = 10000

POLONIEX_WEBSCOKET_URL = "wss://api2.poloniex.com/"
POLONIEX_WEBSOCKET_TIMEOUT = 5

POLONIEX_WEBSOCKET_ORDER = "o"
POLONIEX_WEBSOCKET_TRADE = "t"
POLONIEX_WEBSOCKET_ORDER_BID = 1
POLONIEX_WEBSOCKET_ORDER_ASK = 0
WEBSOCKET_SUBSCRIBE_HEARTBEAT = 1010


class PoloniexParameters(object):
    def __init__(self):
        """
            Not used at present
        """
    SUBSCRIBE_TROLL_BOX = 1001
    SUBSCRIBE_TICKER = 1002
    SUBSCRIBE_BASE_COIN_24HR_STATS = 1003
