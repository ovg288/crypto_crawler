from enums.currency_pair import CURRENCY_PAIR
from enums.currency import CURRENCY


def split_currency_pairs(pair_id):
    return {
        CURRENCY_PAIR.BTC_TO_DASH: (CURRENCY.BITCOIN, CURRENCY.DASH),
        CURRENCY_PAIR.BTC_TO_ETH: (CURRENCY.BITCOIN, CURRENCY.ETH),
        CURRENCY_PAIR.BTC_TO_LTC: (CURRENCY.BITCOIN, CURRENCY.LTC),
        CURRENCY_PAIR.BTC_TO_XRP: (CURRENCY.BITCOIN, CURRENCY.XRP),
        CURRENCY_PAIR.BTC_TO_BCC: (CURRENCY.BITCOIN, CURRENCY.BCC),
        CURRENCY_PAIR.BTC_TO_ETC: (CURRENCY.BITCOIN, CURRENCY.ETC),
        CURRENCY_PAIR.BTC_TO_SC: (CURRENCY.BITCOIN, CURRENCY.SC),
        CURRENCY_PAIR.BTC_TO_DGB: (CURRENCY.BITCOIN, CURRENCY.DGB),
        CURRENCY_PAIR.BTC_TO_XEM: (CURRENCY.BITCOIN, CURRENCY.XEM),
        CURRENCY_PAIR.BTC_TO_ARDR: (CURRENCY.BITCOIN, CURRENCY.ARDR),
        CURRENCY_PAIR.ETH_TO_DASH: (CURRENCY.ETH, CURRENCY.DASH),
        CURRENCY_PAIR.ETH_TO_LTC: (CURRENCY.ETH, CURRENCY.LTC),
        CURRENCY_PAIR.ETH_TO_XRP: (CURRENCY.ETH, CURRENCY.XRP),
        CURRENCY_PAIR.ETH_TO_BCC: (CURRENCY.ETH, CURRENCY.BCC),
        CURRENCY_PAIR.ETH_TO_ETC: (CURRENCY.ETH, CURRENCY.ETC),
        CURRENCY_PAIR.ETH_TO_SC: (CURRENCY.ETH, CURRENCY.SC),
        CURRENCY_PAIR.ETH_TO_DGB: (CURRENCY.ETH, CURRENCY.DGB),
        CURRENCY_PAIR.ETH_TO_XEM: (CURRENCY.ETH, CURRENCY.XEM),
        CURRENCY_PAIR.USD_TO_DASH: (CURRENCY.USD, CURRENCY.DASH),
        CURRENCY_PAIR.USD_TO_BTC: (CURRENCY.USD, CURRENCY.BITCOIN),
        CURRENCY_PAIR.USD_TO_LTC: (CURRENCY.USD, CURRENCY.LTC),
        CURRENCY_PAIR.USD_TO_XRP: (CURRENCY.USD, CURRENCY.XRP),
        CURRENCY_PAIR.USD_TO_BCC: (CURRENCY.USD, CURRENCY.BCC),
        CURRENCY_PAIR.USD_TO_ETC: (CURRENCY.USD, CURRENCY.ETC),
        CURRENCY_PAIR.USD_TO_ETH: (CURRENCY.USD, CURRENCY.ETH),
    }[pair_id]


def get_currency_pair_from_poloniex(pair_name):
    return {
        'BTC_DASH': CURRENCY_PAIR.BTC_TO_DASH,
        'BTC_ETH': CURRENCY_PAIR.BTC_TO_ETH,
        'BTC_LTC': CURRENCY_PAIR.BTC_TO_LTC,
        'BTC_XRP': CURRENCY_PAIR.BTC_TO_XRP,
        'BTC_ETC': CURRENCY_PAIR.BTC_TO_ETC,
        'BTC_SC': CURRENCY_PAIR.BTC_TO_SC,
        'BTC_DGB' : CURRENCY_PAIR.BTC_TO_DGB,
        'BTC_XEM': CURRENCY_PAIR.BTC_TO_XEM,
        'BTC_ARDR': CURRENCY_PAIR.BTC_TO_ARDR,
        'BTC_BCH': CURRENCY_PAIR.BTC_TO_BCC,
        'ETH_ETC': CURRENCY_PAIR.ETH_TO_ETC,
        'ETH_BCH': CURRENCY_PAIR.ETH_TO_BCC,
        'USDT_DASH': CURRENCY_PAIR.USD_TO_DASH,
        'USDT_ETH': CURRENCY_PAIR.USD_TO_ETH,
        'USDT_LTC': CURRENCY_PAIR.USD_TO_LTC,
        'USDT_XRP': CURRENCY_PAIR.USD_TO_XRP,
        'USDT_ETC': CURRENCY_PAIR.USD_TO_ETC,
        'USDT_BCH': CURRENCY_PAIR.USD_TO_BCC
    }[pair_name]


def get_currency_pair_from_kraken(pair_name):
    return {
        'DASHXBT': CURRENCY_PAIR.BTC_TO_DASH,
        'XETHXXBT': CURRENCY_PAIR.BTC_TO_ETH,
        'XLTCXXBT': CURRENCY_PAIR.BTC_TO_LTC,
        'XXRPXXBT': CURRENCY_PAIR.BTC_TO_XRP,
        'BCHXBT': CURRENCY_PAIR.BTC_TO_BCC,
        'XETCXXBT': CURRENCY_PAIR.BTC_TO_ETC,
        'XXDGXXBT': CURRENCY_PAIR.BTC_TO_DGB,
        'XETCXETH': CURRENCY_PAIR.ETH_TO_ETC,
        'DASHUSD': CURRENCY_PAIR.USD_TO_DASH,
        'XETHZUSD': CURRENCY_PAIR.USD_TO_ETH,
        'XLTCZUSD': CURRENCY_PAIR.USD_TO_LTC,
        'XXRPZUSD': CURRENCY_PAIR.USD_TO_XRP,
        'BCHUSD': CURRENCY_PAIR.USD_TO_BCC,
        'XETCZUSD': CURRENCY_PAIR.USD_TO_ETC
    }[pair_name]


def get_currency_pair_from_bittrex(pair_name):
    return {
        'BTC-DASH': CURRENCY_PAIR.BTC_TO_DASH,
        'BTC-ETH': CURRENCY_PAIR.BTC_TO_ETH,
        'BTC-LTC': CURRENCY_PAIR.BTC_TO_LTC,
        'BTC-XRP': CURRENCY_PAIR.BTC_TO_XRP,
        'BTC-BCC': CURRENCY_PAIR.BTC_TO_BCC,
        'BTC-ETC': CURRENCY_PAIR.BTC_TO_ETC,
        'BTC-SC': CURRENCY_PAIR.BTC_TO_SC,
        'BTC-DGB': CURRENCY_PAIR.BTC_TO_DGB,
        'BTC-XEM': CURRENCY_PAIR.BTC_TO_XEM,
        'BTC-ARDR': CURRENCY_PAIR.BTC_TO_ARDR,
        'ETH-DASH': CURRENCY_PAIR.ETH_TO_DASH,
        'ETH-LTC': CURRENCY_PAIR.ETH_TO_LTC,
        'ETH-XRP': CURRENCY_PAIR.ETH_TO_XRP,
        'ETH-BCC': CURRENCY_PAIR.ETH_TO_BCC,
        'ETH-ETC': CURRENCY_PAIR.ETH_TO_ETC,
        'ETH-SC': CURRENCY_PAIR.ETH_TO_SC,
        'ETH-DGB': CURRENCY_PAIR.ETH_TO_DGB,
        'ETH-XEM': CURRENCY_PAIR.ETH_TO_XEM,
        'USDT-DASH': CURRENCY_PAIR.USD_TO_DASH,
        'USDT-BTC': CURRENCY_PAIR.USD_TO_BTC,
        'USDT-LTC': CURRENCY_PAIR.USD_TO_LTC,
        'USDT-XRP': CURRENCY_PAIR.USD_TO_XRP,
        'USDT-BCC': CURRENCY_PAIR.USD_TO_BCC,
        'USDT-ETC': CURRENCY_PAIR.USD_TO_ETC,
        'USDT-ETH': CURRENCY_PAIR.USD_TO_ETH
    }[pair_name]


def get_currency_pair_to_poloniex(pair_id):
    return {
        CURRENCY_PAIR.BTC_TO_DASH: 'BTC_DASH',
        CURRENCY_PAIR.BTC_TO_ETH: 'BTC_ETH',
        CURRENCY_PAIR.BTC_TO_LTC: 'BTC_LTC',
        CURRENCY_PAIR.BTC_TO_XRP: 'BTC_XRP',
        CURRENCY_PAIR.BTC_TO_ETC: 'BTC_ETC',
        CURRENCY_PAIR.BTC_TO_SC: 'BTC_SC',
        CURRENCY_PAIR.BTC_TO_DGB : 'BTC_DGB',
        CURRENCY_PAIR.BTC_TO_XEM: 'BTC_XEM',
        CURRENCY_PAIR.BTC_TO_ARDR: 'BTC_ARDR',
        CURRENCY_PAIR.BTC_TO_BCC: 'BTC_BCH',
        CURRENCY_PAIR.ETH_TO_ETC: 'ETH_ETC',
        CURRENCY_PAIR.ETH_TO_BCC: 'ETH_BCH',
        CURRENCY_PAIR.USD_TO_DASH: 'USDT_DASH',
        CURRENCY_PAIR.USD_TO_ETH: 'USDT_ETH',
        CURRENCY_PAIR.USD_TO_LTC: 'USDT_LTC',
        CURRENCY_PAIR.USD_TO_XRP: 'USDT_XRP',
        CURRENCY_PAIR.USD_TO_ETC: 'USDT_ETC',
        CURRENCY_PAIR.USD_TO_BCC: 'USDT_BCH'
    }[pair_id]


def get_currency_pair_to_kraken(pair_id):
    return {
        CURRENCY_PAIR.BTC_TO_DASH: 'DASHXBT',
        CURRENCY_PAIR.BTC_TO_ETH: 'XETHXXBT',
        CURRENCY_PAIR.BTC_TO_LTC: 'XLTCXXBT',
        CURRENCY_PAIR.BTC_TO_XRP: 'XXRPXXBT',
        CURRENCY_PAIR.BTC_TO_BCC: 'BCHXBT',
        CURRENCY_PAIR.BTC_TO_ETC: 'XETCXXBT',
        CURRENCY_PAIR.ETH_TO_ETC: 'XETCXETH',
        CURRENCY_PAIR.USD_TO_DASH: 'DASHUSD',
        CURRENCY_PAIR.USD_TO_ETH: 'XETHZUSD',
        CURRENCY_PAIR.USD_TO_LTC: 'XLTCZUSD',
        CURRENCY_PAIR.USD_TO_XRP: 'XXRPZUSD',
        CURRENCY_PAIR.USD_TO_BCC: 'BCHUSD',
        CURRENCY_PAIR.USD_TO_ETC: 'XETCZUSD'
    }[pair_id]


def get_currency_pair_to_bittrex(pair_id):
    return {
        CURRENCY_PAIR.BTC_TO_DASH: 'BTC-DASH',
        CURRENCY_PAIR.BTC_TO_ETH: 'BTC-ETH',
        CURRENCY_PAIR.BTC_TO_LTC: 'BTC-LTC',
        CURRENCY_PAIR.BTC_TO_XRP: 'BTC-XRP',
        CURRENCY_PAIR.BTC_TO_BCC: 'BTC-BCC',
        CURRENCY_PAIR.BTC_TO_ETC: 'BTC-ETC',
        CURRENCY_PAIR.BTC_TO_SC: 'BTC-SC',
        CURRENCY_PAIR.BTC_TO_DGB: 'BTC-DGB',
        CURRENCY_PAIR.BTC_TO_XEM: 'BTC-XEM',
        CURRENCY_PAIR.BTC_TO_ARDR: 'BTC-ARDR',
        CURRENCY_PAIR.ETH_TO_DASH: 'ETH-DASH',
        CURRENCY_PAIR.ETH_TO_LTC: 'ETH-LTC',
        CURRENCY_PAIR.ETH_TO_XRP: 'ETH-XRP',
        CURRENCY_PAIR.ETH_TO_BCC: 'ETH-BCC',
        CURRENCY_PAIR.ETH_TO_ETC: 'ETH-ETC',
        CURRENCY_PAIR.ETH_TO_SC: 'ETH-SC',
        CURRENCY_PAIR.ETH_TO_DGB: 'ETH-DGB',
        CURRENCY_PAIR.ETH_TO_XEM: 'ETH-XEM',
        CURRENCY_PAIR.USD_TO_DASH: 'USDT-DASH',
        CURRENCY_PAIR.USD_TO_BTC: 'USDT-BTC',
        CURRENCY_PAIR.USD_TO_LTC: 'USDT-LTC',
        CURRENCY_PAIR.USD_TO_XRP: 'USDT-XRP',
        CURRENCY_PAIR.USD_TO_BCC: 'USDT-BCC',
        CURRENCY_PAIR.USD_TO_ETC: 'USDT-ETC',
        CURRENCY_PAIR.USD_TO_ETH: 'USDT-ETH'

    }[pair_id]


def get_pair_name_by_id(pair_id):
    return {
        CURRENCY_PAIR.BTC_TO_DASH: "BTC_TO_DASH",
        CURRENCY_PAIR.BTC_TO_ETH: "BTC_TO_ETH",
        CURRENCY_PAIR.BTC_TO_LTC: "BTC_TO_LTC",
        CURRENCY_PAIR.BTC_TO_XRP: "BTC_TO_XRP",
        CURRENCY_PAIR.BTC_TO_BCC: "BTC_TO_BCC",
        CURRENCY_PAIR.BTC_TO_ETC: "BTC_TO_ETC",
        CURRENCY_PAIR.BTC_TO_SC: "BTC_TO_SC",
        CURRENCY_PAIR.BTC_TO_DGB: "BTC_TO_DGB",
        CURRENCY_PAIR.BTC_TO_XEM: "BTC_TO_XEM",
        CURRENCY_PAIR.BTC_TO_ARDR: "BTC_TO_ARDR",
        CURRENCY_PAIR.ETH_TO_DASH: "ETH_TO_DASH",
        CURRENCY_PAIR.ETH_TO_LTC: "ETH_TO_LTC",
        CURRENCY_PAIR.ETH_TO_XRP: "ETH_TO_XRP",
        CURRENCY_PAIR.ETH_TO_BCC: "ETH_TO_BCC",
        CURRENCY_PAIR.ETH_TO_ETC: "ETH_TO_ETC",
        CURRENCY_PAIR.ETH_TO_SC: "ETH_TO_SC",
        CURRENCY_PAIR.ETH_TO_DGB: "ETH_TO_DGB",
        CURRENCY_PAIR.ETH_TO_XEM: "ETH_TO_XEM",
        CURRENCY_PAIR.USD_TO_DASH: "USD_TO_DASH",
        CURRENCY_PAIR.USD_TO_BTC: "USD_TO_BTC",
        CURRENCY_PAIR.USD_TO_LTC: "USD_TO_LTC",
        CURRENCY_PAIR.USD_TO_XRP: "USD_TO_XRP",
        CURRENCY_PAIR.USD_TO_BCC: "USD_TO_BCC",
        CURRENCY_PAIR.USD_TO_ETC: "USD_TO_ETC",
        CURRENCY_PAIR.USD_TO_ETH: "USD_TO_ETH"
    }[pair_id]


"""
    NOTE:   routine below is used only for balance retrieval
            supported currencies are
            ARBITRAGE_CURRENCY = [CURRENCY.DASH, CURRENCY.BCC, CURRENCY.XRP, CURRENCY.LTC, CURRENCY.ETC, CURRENCY.ETH]
"""


def get_currency_id_from_kraken(currency_name):
    return {
        'XXBT': CURRENCY.BITCOIN,
        'DASH': CURRENCY.DASH,
        'BCH': CURRENCY.BCC,
        'XXRP': CURRENCY.XRP,
        'XLTC': CURRENCY.LTC,
        'XETC': CURRENCY.ETC,
        'XETH': CURRENCY.ETH,
        'XXDG': CURRENCY.DGB,
        'ZUSD': CURRENCY.USD,
        'USD': CURRENCY.USD
    }[currency_name]


def get_currency_name_for_kraken(currency_id):
    return {
        CURRENCY.BITCOIN: 'XXBT',
        CURRENCY.DASH: 'DASH',
        CURRENCY.BCC: 'BCH',
        CURRENCY.XRP: 'XXRP',
        CURRENCY.LTC: 'XLTC',
        CURRENCY.ETC: 'XETC',
        CURRENCY.ETH: 'XETH',
        CURRENCY.DGB: 'XXDG',
        CURRENCY.USD: 'ZUSD',
        CURRENCY.USD: 'USD'
    }[currency_id]


def get_currency_id_from_bittrex(currency_name):
    return {
        'BTC': CURRENCY.BITCOIN,
        'DASH': CURRENCY.DASH,
        'BCC': CURRENCY.BCC,
        'XRP': CURRENCY.XRP,
        'LTC': CURRENCY.LTC,
        'ETC': CURRENCY.ETC,
        'ETH': CURRENCY.ETH,
        'SC': CURRENCY.SC,
        'DGB': CURRENCY.DGB,
        'XEM': CURRENCY.XEM,
        'ARDR': CURRENCY.ARDR,
        'USD': CURRENCY.USD
    }[currency_name]


def get_currency_name_for_bittrex(currency_id):
    return {
        CURRENCY.BITCOIN: 'BTC',
        CURRENCY.DASH: 'DASH',
        CURRENCY.BCC: 'BCC',
        CURRENCY.XRP: 'XRP',
        CURRENCY.LTC: 'LTC',
        CURRENCY.ETC: 'ETC',
        CURRENCY.ETH: 'ETH',
        CURRENCY.SC: 'SC',
        CURRENCY.DGB: 'DGB',
        CURRENCY.XEM: 'XEM',
        CURRENCY.ARDR: 'ARDR',
        CURRENCY.USD: 'USD'
    }[currency_id]


def get_currency_id_from_poloniex(currency_name):
    return {
        'BTC': CURRENCY.BITCOIN,
        'DASH': CURRENCY.DASH,
        'BCH': CURRENCY.BCC,
        'XRP': CURRENCY.XRP,
        'LTC': CURRENCY.LTC,
        'ETC': CURRENCY.ETC,
        'ETH': CURRENCY.ETH,
        'SC': CURRENCY.SC,
        'DGB': CURRENCY.DGB,
        'XEM': CURRENCY.XEM,
        'ARDR': CURRENCY.ARDR,
        'USD': CURRENCY.USD
    }[currency_name]


def get_currency_name_for_poloniex(currency_id):
    return {
        CURRENCY.BITCOIN: 'BTC',
        CURRENCY.DASH: 'DASH',
        CURRENCY.BCC: 'BCH',
        CURRENCY.XRP: 'XRP',
        CURRENCY.LTC: 'LTC',
        CURRENCY.ETC: 'ETC',
        CURRENCY.ETH: 'ETH',
        CURRENCY.SC: 'SC',
        CURRENCY.DGB: 'DGB',
        CURRENCY.XEM: 'XEM',
        CURRENCY.ARDR: 'ARDR',
        CURRENCY.USD: 'USD'
    }[currency_id]


def get_currency_name_by_id(currency_id):
    return {
        CURRENCY.BITCOIN: 'BTC',
        CURRENCY.DASH: 'DASH',
        CURRENCY.BCC: 'BCH',
        CURRENCY.XRP: 'XRP',
        CURRENCY.LTC: 'LTC',
        CURRENCY.ETC: 'ETC',
        CURRENCY.ETH: 'ETH',
        CURRENCY.SC: 'SC',
        CURRENCY.DGB: 'DGB',
        CURRENCY.XEM: 'XEM',
        CURRENCY.ARDR: 'ARDR',
        CURRENCY.USD: 'USD'
    }[currency_id]
