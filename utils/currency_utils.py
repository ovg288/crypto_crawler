from enums.currency_pair import CURRENCY_PAIR
from enums.currency import CURRENCY
from enums.exchange import EXCHANGE

from bittrex.currency_utils import get_currency_pair_to_bittrex
from kraken.currency_utils import get_currency_pair_to_kraken
from poloniex.currency_utils import get_currency_pair_to_poloniex
from binance.currency_utils import get_currency_pair_to_binance
from huobi.currency_utils import get_currency_pair_to_huobi


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
        CURRENCY_PAIR.BTC_TO_OMG: (CURRENCY.BITCOIN, CURRENCY.OMG),
        CURRENCY_PAIR.BTC_TO_ZEC: (CURRENCY.BITCOIN, CURRENCY.ZEC),
        CURRENCY_PAIR.BTC_TO_REP: (CURRENCY.BITCOIN, CURRENCY.REP),
        CURRENCY_PAIR.BTC_TO_XMR: (CURRENCY.BITCOIN, CURRENCY.XMR),
        CURRENCY_PAIR.BTC_TO_DOGE: (CURRENCY.BITCOIN, CURRENCY.DOGE),
        CURRENCY_PAIR.BTC_TO_DCR: (CURRENCY.BITCOIN, CURRENCY.DCR),
        CURRENCY_PAIR.BTC_TO_NEO: (CURRENCY.BITCOIN, CURRENCY.NEO),
        CURRENCY_PAIR.BTC_TO_QTUM: (CURRENCY.BITCOIN, CURRENCY.QTUM),
        CURRENCY_PAIR.BTC_TO_EOS: (CURRENCY.BITCOIN, CURRENCY.EOS),
        CURRENCY_PAIR.BTC_TO_IOTA: (CURRENCY.BITCOIN, CURRENCY.IOTA),
        CURRENCY_PAIR.BTC_TO_BTG: (CURRENCY.BITCOIN, CURRENCY.BTG),
        CURRENCY_PAIR.BTC_TO_WTC: (CURRENCY.BITCOIN, CURRENCY.WTC),
        CURRENCY_PAIR.BTC_TO_KNC: (CURRENCY.BITCOIN, CURRENCY.KNC),
        CURRENCY_PAIR.BTC_TO_BAT: (CURRENCY.BITCOIN, CURRENCY.BAT),
        CURRENCY_PAIR.BTC_TO_ZRX: (CURRENCY.BITCOIN, CURRENCY.ZRX),
        CURRENCY_PAIR.BTC_TO_RDN: (CURRENCY.BITCOIN, CURRENCY.RDN),
        CURRENCY_PAIR.BTC_TO_GAS: (CURRENCY.BITCOIN, CURRENCY.GAS),
        CURRENCY_PAIR.BTC_TO_ADA: (CURRENCY.BITCOIN, CURRENCY.ADA),
        CURRENCY_PAIR.BTC_TO_RCN: (CURRENCY.BITCOIN, CURRENCY.RCN),
        CURRENCY_PAIR.BTC_TO_QSP: (CURRENCY.BITCOIN, CURRENCY.QSP),
        CURRENCY_PAIR.BTC_TO_XBY: (CURRENCY.BITCOIN, CURRENCY.XBY),
        CURRENCY_PAIR.BTC_TO_PAC: (CURRENCY.BITCOIN, CURRENCY.PAC),
        CURRENCY_PAIR.BTC_TO_RDD: (CURRENCY.BITCOIN, CURRENCY.RDD),
        CURRENCY_PAIR.BTC_TO_ICX: (CURRENCY.BITCOIN, CURRENCY.ICX),
        CURRENCY_PAIR.BTC_TO_WABI: (CURRENCY.BITCOIN, CURRENCY.WABI),
        CURRENCY_PAIR.BTC_TO_XLM: (CURRENCY.BITCOIN, CURRENCY.XLM),
        CURRENCY_PAIR.BTC_TO_TRX: (CURRENCY.BITCOIN, CURRENCY.TRX),
        CURRENCY_PAIR.BTC_TO_AION: (CURRENCY.BITCOIN, CURRENCY.AION),
        CURRENCY_PAIR.BTC_TO_ITC: (CURRENCY.BITCOIN, CURRENCY.ITC),
        CURRENCY_PAIR.BTC_TO_ARK: (CURRENCY.BITCOIN, CURRENCY.ARK),
        CURRENCY_PAIR.BTC_TO_STRAT: (CURRENCY.BITCOIN, CURRENCY.STRAT),
        CURRENCY_PAIR.BTC_TO_LSK: (CURRENCY.BITCOIN, CURRENCY.LSK),
        CURRENCY_PAIR.BTC_TO_ENG: (CURRENCY.BITCOIN, CURRENCY.ENG),
        CURRENCY_PAIR.BTC_TO_XVG: (CURRENCY.BITCOIN, CURRENCY.XVG),
        CURRENCY_PAIR.BTC_TO_ONT: (CURRENCY.BITCOIN, CURRENCY.ONT),
        CURRENCY_PAIR.BTC_TO_HSR: (CURRENCY.BITCOIN, CURRENCY.HSR),
        CURRENCY_PAIR.BTC_TO_ZIL: (CURRENCY.BITCOIN, CURRENCY.ZIL),
        CURRENCY_PAIR.BTC_TO_VEN: (CURRENCY.BITCOIN, CURRENCY.VEN),
        CURRENCY_PAIR.BTC_TO_ELF: (CURRENCY.BITCOIN, CURRENCY.ELF),
        CURRENCY_PAIR.BTC_TO_BLZ: (CURRENCY.BITCOIN, CURRENCY.BLZ),
        CURRENCY_PAIR.BTC_TO_REQ: (CURRENCY.BITCOIN, CURRENCY.REQ),
        CURRENCY_PAIR.BTC_TO_LINK: (CURRENCY.BITCOIN, CURRENCY.LINK),
        CURRENCY_PAIR.BTC_TO_NAS: (CURRENCY.BITCOIN, CURRENCY.NAS),
        CURRENCY_PAIR.BTC_TO_ELA: (CURRENCY.BITCOIN, CURRENCY.ELA),
        CURRENCY_PAIR.ETH_TO_DASH: (CURRENCY.ETH, CURRENCY.DASH),
        CURRENCY_PAIR.ETH_TO_LTC: (CURRENCY.ETH, CURRENCY.LTC),
        CURRENCY_PAIR.ETH_TO_XRP: (CURRENCY.ETH, CURRENCY.XRP),
        CURRENCY_PAIR.ETH_TO_BCC: (CURRENCY.ETH, CURRENCY.BCC),
        CURRENCY_PAIR.ETH_TO_ETC: (CURRENCY.ETH, CURRENCY.ETC),
        CURRENCY_PAIR.ETH_TO_SC: (CURRENCY.ETH, CURRENCY.SC),
        CURRENCY_PAIR.ETH_TO_DGB: (CURRENCY.ETH, CURRENCY.DGB),
        CURRENCY_PAIR.ETH_TO_XEM: (CURRENCY.ETH, CURRENCY.XEM),
        CURRENCY_PAIR.ETH_TO_OMG: (CURRENCY.ETH, CURRENCY.OMG),
        CURRENCY_PAIR.ETH_TO_ZEC: (CURRENCY.ETH, CURRENCY.ZEC),
        CURRENCY_PAIR.ETH_TO_REP: (CURRENCY.ETH, CURRENCY.REP),
        CURRENCY_PAIR.ETH_TO_XMR: (CURRENCY.ETH, CURRENCY.XMR),
        CURRENCY_PAIR.ETH_TO_NEO: (CURRENCY.ETH, CURRENCY.NEO),
        CURRENCY_PAIR.ETH_TO_QTUM: (CURRENCY.ETH, CURRENCY.QTUM),
        CURRENCY_PAIR.ETH_TO_EOS: (CURRENCY.ETH, CURRENCY.EOS),
        CURRENCY_PAIR.ETH_TO_IOTA: (CURRENCY.ETH, CURRENCY.IOTA),
        CURRENCY_PAIR.ETH_TO_BTG: (CURRENCY.ETH, CURRENCY.BTG),
        CURRENCY_PAIR.ETH_TO_WTC: (CURRENCY.ETH, CURRENCY.WTC),
        CURRENCY_PAIR.ETH_TO_KNC: (CURRENCY.ETH, CURRENCY.KNC),
        CURRENCY_PAIR.ETH_TO_BAT: (CURRENCY.ETH, CURRENCY.BAT),
        CURRENCY_PAIR.ETH_TO_ZRX: (CURRENCY.ETH, CURRENCY.ZRX),
        CURRENCY_PAIR.ETH_TO_RDN: (CURRENCY.ETH, CURRENCY.RDN),
        CURRENCY_PAIR.ETH_TO_GAS: (CURRENCY.ETH, CURRENCY.GAS),
        CURRENCY_PAIR.ETH_TO_ADA: (CURRENCY.ETH, CURRENCY.ADA),
        CURRENCY_PAIR.ETH_TO_RCN: (CURRENCY.ETH, CURRENCY.RCN),
        CURRENCY_PAIR.ETH_TO_QSP: (CURRENCY.ETH, CURRENCY.QSP),
        CURRENCY_PAIR.ETH_TO_XBY: (CURRENCY.ETH, CURRENCY.XBY),
        CURRENCY_PAIR.ETH_TO_PAC: (CURRENCY.ETH, CURRENCY.PAC),
        CURRENCY_PAIR.ETH_TO_RDD: (CURRENCY.ETH, CURRENCY.RDD),
        CURRENCY_PAIR.ETH_TO_ICX: (CURRENCY.ETH, CURRENCY.ICX),
        CURRENCY_PAIR.ETH_TO_WABI: (CURRENCY.ETH, CURRENCY.WABI),
        CURRENCY_PAIR.ETH_TO_XLM: (CURRENCY.ETH, CURRENCY.XLM),
        CURRENCY_PAIR.ETH_TO_TRX: (CURRENCY.ETH, CURRENCY.TRX),
        CURRENCY_PAIR.ETH_TO_AION: (CURRENCY.ETH, CURRENCY.AION),
        CURRENCY_PAIR.ETH_TO_ITC: (CURRENCY.ETH, CURRENCY.ITC),
        CURRENCY_PAIR.ETH_TO_ARK: (CURRENCY.ETH, CURRENCY.ARK),
        CURRENCY_PAIR.ETH_TO_STRAT: (CURRENCY.ETH, CURRENCY.STRAT),
        CURRENCY_PAIR.ETH_TO_LSK: (CURRENCY.ETH, CURRENCY.LSK),
        CURRENCY_PAIR.ETH_TO_ENG: (CURRENCY.ETH, CURRENCY.ENG),
        CURRENCY_PAIR.ETH_TO_XVG: (CURRENCY.ETH, CURRENCY.XVG),
        CURRENCY_PAIR.ETH_TO_ONT: (CURRENCY.ETH, CURRENCY.ONT),
        CURRENCY_PAIR.ETH_TO_HSR: (CURRENCY.ETH, CURRENCY.HSR),
        CURRENCY_PAIR.ETH_TO_ZIL: (CURRENCY.ETH, CURRENCY.ZIL),
        CURRENCY_PAIR.ETH_TO_VEN: (CURRENCY.ETH, CURRENCY.VEN),
        CURRENCY_PAIR.ETH_TO_ELF: (CURRENCY.ETH, CURRENCY.ELF),
        CURRENCY_PAIR.ETH_TO_BLZ: (CURRENCY.ETH, CURRENCY.BLZ),
        CURRENCY_PAIR.ETH_TO_REQ: (CURRENCY.ETH, CURRENCY.REQ),
        CURRENCY_PAIR.ETH_TO_LINK: (CURRENCY.ETH, CURRENCY.LINK),
        CURRENCY_PAIR.ETH_TO_NAS: (CURRENCY.ETH, CURRENCY.NAS),
        CURRENCY_PAIR.ETH_TO_ELA: (CURRENCY.ETH, CURRENCY.ELA),
        CURRENCY_PAIR.USD_TO_DASH: (CURRENCY.USD, CURRENCY.DASH),
        CURRENCY_PAIR.USD_TO_BTC: (CURRENCY.USD, CURRENCY.BITCOIN),
        CURRENCY_PAIR.USD_TO_LTC: (CURRENCY.USD, CURRENCY.LTC),
        CURRENCY_PAIR.USD_TO_XRP: (CURRENCY.USD, CURRENCY.XRP),
        CURRENCY_PAIR.USD_TO_BCC: (CURRENCY.USD, CURRENCY.BCC),
        CURRENCY_PAIR.USD_TO_ETC: (CURRENCY.USD, CURRENCY.ETC),
        CURRENCY_PAIR.USD_TO_ETH: (CURRENCY.USD, CURRENCY.ETH),
        CURRENCY_PAIR.USD_TO_ZEC: (CURRENCY.USD, CURRENCY.ZEC),
        CURRENCY_PAIR.USD_TO_REP: (CURRENCY.USD, CURRENCY.REP),
        CURRENCY_PAIR.USD_TO_XMR: (CURRENCY.USD, CURRENCY.XMR),
        CURRENCY_PAIR.USDT_TO_DASH: (CURRENCY.USDT, CURRENCY.DASH),
        CURRENCY_PAIR.USDT_TO_BTC: (CURRENCY.USDT, CURRENCY.BITCOIN),
        CURRENCY_PAIR.USDT_TO_LTC: (CURRENCY.USDT, CURRENCY.LTC),
        CURRENCY_PAIR.USDT_TO_XRP: (CURRENCY.USDT, CURRENCY.XRP),
        CURRENCY_PAIR.USDT_TO_BCC: (CURRENCY.USDT, CURRENCY.BCC),
        CURRENCY_PAIR.USDT_TO_ETC: (CURRENCY.USDT, CURRENCY.ETC),
        CURRENCY_PAIR.USDT_TO_ETH: (CURRENCY.USDT, CURRENCY.ETH),
        CURRENCY_PAIR.USDT_TO_ZEC: (CURRENCY.USDT, CURRENCY.ZEC),
        CURRENCY_PAIR.USDT_TO_REP: (CURRENCY.USDT, CURRENCY.REP),
        CURRENCY_PAIR.USDT_TO_XMR: (CURRENCY.USDT, CURRENCY.XMR),
        CURRENCY_PAIR.USDT_TO_NEO: (CURRENCY.USDT, CURRENCY.NEO),
        CURRENCY_PAIR.USDT_TO_QTUM: (CURRENCY.USDT, CURRENCY.QTUM),
        CURRENCY_PAIR.USDT_TO_EOS: (CURRENCY.USDT, CURRENCY.EOS),
        CURRENCY_PAIR.USDT_TO_IOTA: (CURRENCY.USDT, CURRENCY.IOTA),
        CURRENCY_PAIR.USDT_TO_BTG: (CURRENCY.USDT, CURRENCY.BTG),
        CURRENCY_PAIR.USDT_TO_WTC: (CURRENCY.USDT, CURRENCY.WTC),
        CURRENCY_PAIR.USDT_TO_KNC: (CURRENCY.USDT, CURRENCY.KNC),
        CURRENCY_PAIR.USDT_TO_BAT: (CURRENCY.USDT, CURRENCY.BAT),
        CURRENCY_PAIR.USDT_TO_ZRX: (CURRENCY.USDT, CURRENCY.ZRX),
        CURRENCY_PAIR.USDT_TO_RDN: (CURRENCY.USDT, CURRENCY.RDN),
        CURRENCY_PAIR.USDT_TO_GAS: (CURRENCY.USDT, CURRENCY.GAS),
        CURRENCY_PAIR.USDT_TO_ADA: (CURRENCY.USDT, CURRENCY.ADA),
        CURRENCY_PAIR.USDT_TO_RCN: (CURRENCY.USDT, CURRENCY.RCN),
        CURRENCY_PAIR.USDT_TO_QSP: (CURRENCY.USDT, CURRENCY.QSP),
        CURRENCY_PAIR.USDT_TO_XBY: (CURRENCY.USDT, CURRENCY.XBY),
        CURRENCY_PAIR.USDT_TO_PAC: (CURRENCY.USDT, CURRENCY.PAC),
        CURRENCY_PAIR.USDT_TO_RDD: (CURRENCY.USDT, CURRENCY.RDD),
        CURRENCY_PAIR.USDT_TO_ICX: (CURRENCY.USDT, CURRENCY.ICX),
        CURRENCY_PAIR.USDT_TO_WABI: (CURRENCY.USDT, CURRENCY.WABI),
        CURRENCY_PAIR.USDT_TO_XLM: (CURRENCY.USDT, CURRENCY.XLM),
        CURRENCY_PAIR.USDT_TO_TRX: (CURRENCY.USDT, CURRENCY.TRX),
        CURRENCY_PAIR.USDT_TO_AION: (CURRENCY.USDT, CURRENCY.AION),
        CURRENCY_PAIR.USDT_TO_ITC: (CURRENCY.USDT, CURRENCY.ITC),
        CURRENCY_PAIR.USDT_TO_XVG: (CURRENCY.USDT, CURRENCY.XVG),
        CURRENCY_PAIR.USDT_TO_HSR: (CURRENCY.USDT, CURRENCY.HSR),
        CURRENCY_PAIR.USDT_TO_ZIL: (CURRENCY.USDT, CURRENCY.ZIL),
        CURRENCY_PAIR.USDT_TO_VEN: (CURRENCY.USDT, CURRENCY.VEN),
        CURRENCY_PAIR.USDT_TO_ELF: (CURRENCY.USDT, CURRENCY.ELF),
        CURRENCY_PAIR.USD_TO_USDT: (CURRENCY.USDT, CURRENCY.USD),
        CURRENCY_PAIR.USDT_TO_NAS: (CURRENCY.USDT, CURRENCY.NAS),
        CURRENCY_PAIR.USDT_TO_ELA: (CURRENCY.USDT, CURRENCY.ELA)
    }[pair_id]


def get_pair_id_by_name(pair_name):
    return {
        "BTC_TO_DASH": CURRENCY_PAIR.BTC_TO_DASH,
        "BTC_TO_ETH": CURRENCY_PAIR.BTC_TO_ETH,
        "BTC_TO_LTC": CURRENCY_PAIR.BTC_TO_LTC,
        "BTC_TO_XRP": CURRENCY_PAIR.BTC_TO_XRP,
        "BTC_TO_BCC": CURRENCY_PAIR.BTC_TO_BCC,
        "BTC_TO_ETC": CURRENCY_PAIR.BTC_TO_ETC,
        "BTC_TO_SC": CURRENCY_PAIR.BTC_TO_SC,
        "BTC_TO_DGB": CURRENCY_PAIR.BTC_TO_DGB,
        "BTC_TO_XEM": CURRENCY_PAIR.BTC_TO_XEM,
        "BTC_TO_ARDR": CURRENCY_PAIR.BTC_TO_ARDR,
        "BTC_TO_OMG": CURRENCY_PAIR.BTC_TO_OMG,
        "BTC_TO_ZEC": CURRENCY_PAIR.BTC_TO_ZEC,
        "BTC_TO_REP": CURRENCY_PAIR.BTC_TO_REP,
        "BTC_TO_XMR": CURRENCY_PAIR.BTC_TO_XMR,
        "BTC_TO_DOGE": CURRENCY_PAIR.BTC_TO_DOGE,
        "BTC_TO_DCR": CURRENCY_PAIR.BTC_TO_DCR,
        "BTC_TO_NEO": CURRENCY_PAIR.BTC_TO_NEO,
        "BTC_TO_QTUM": CURRENCY_PAIR.BTC_TO_QTUM,
        "BTC_TO_EOS": CURRENCY_PAIR.BTC_TO_EOS,
        "BTC_TO_IOTA": CURRENCY_PAIR.BTC_TO_IOTA,
        "BTC_TO_BTG": CURRENCY_PAIR.BTC_TO_BTG,
        "BTC_TO_WTC": CURRENCY_PAIR.BTC_TO_WTC,
        "BTC_TO_KNC": CURRENCY_PAIR.BTC_TO_KNC,
        "BTC_TO_BAT": CURRENCY_PAIR.BTC_TO_BAT,
        "BTC_TO_ZRX": CURRENCY_PAIR.BTC_TO_ZRX,
        "BTC_TO_RDN": CURRENCY_PAIR.BTC_TO_RDN,
        "BTC_TO_GAS": CURRENCY_PAIR.BTC_TO_GAS,
        "BTC_TO_ADA": CURRENCY_PAIR.BTC_TO_ADA,
        "BTC_TO_RCN": CURRENCY_PAIR.BTC_TO_RCN,
        "BTC_TO_QSB": CURRENCY_PAIR.BTC_TO_QSP,
        "BTC_TO_XBY": CURRENCY_PAIR.BTC_TO_XBY,
        "BTC_TO_PAC": CURRENCY_PAIR.BTC_TO_PAC,
        "BTC_TO_RDD": CURRENCY_PAIR.BTC_TO_RDD,
        "BTC_TO_ICX": CURRENCY_PAIR.BTC_TO_ICX,
        "BTC_TO_WABI": CURRENCY_PAIR.BTC_TO_WABI,
        "BTC_TO_XLM": CURRENCY_PAIR.BTC_TO_XLM,
        "BTC_TO_TRX": CURRENCY_PAIR.BTC_TO_TRX,
        "BTC_TO_AION": CURRENCY_PAIR.BTC_TO_AION,
        "BTC_TO_ITC": CURRENCY_PAIR.BTC_TO_ITC,
        "BTC_TO_ARK": CURRENCY_PAIR.BTC_TO_ARK,
        "BTC_TO_STRAT": CURRENCY_PAIR.BTC_TO_STRAT,
        "BTC_TO_LSK": CURRENCY_PAIR.BTC_TO_LSK,
        "BTC_TO_ENG": CURRENCY_PAIR.BTC_TO_ENG,
        "BTC_TO_XVG": CURRENCY_PAIR.BTC_TO_XVG,
        "BTC_TO_ONT": CURRENCY_PAIR.BTC_TO_ONT,
        "BTC_TO_HSR": CURRENCY_PAIR.BTC_TO_HSR,
        "BTC_TO_ZIL": CURRENCY_PAIR.BTC_TO_ZIL,
        "BTC_TO_VEN": CURRENCY_PAIR.BTC_TO_VEN,
        "BTC_TO_ELF": CURRENCY_PAIR.BTC_TO_ELF,
        "BTC_TO_BLZ": CURRENCY_PAIR.BTC_TO_BLZ,
        "BTC_OT_REQ": CURRENCY_PAIR.BTC_TO_REQ,
        "BTC_TO_LINK": CURRENCY_PAIR.BTC_TO_LINK,
        "BTC_TO_NAS": CURRENCY_PAIR.BTC_TO_NAS,
        "BTC_TO_ELA": CURRENCY_PAIR.BTC_TO_ELA,
        "ETH_TO_DASH": CURRENCY_PAIR.ETH_TO_DASH,
        "ETH_TO_LTC": CURRENCY_PAIR.ETH_TO_LTC,
        "ETH_TO_XRP": CURRENCY_PAIR.ETH_TO_XRP,
        "ETH_TO_BCC": CURRENCY_PAIR.ETH_TO_BCC,
        "ETH_TO_ETC": CURRENCY_PAIR.ETH_TO_ETC,
        "ETH_TO_SC": CURRENCY_PAIR.ETH_TO_SC,
        "ETH_TO_DGB": CURRENCY_PAIR.ETH_TO_DGB,
        "ETH_TO_XEM": CURRENCY_PAIR.ETH_TO_XEM,
        "ETH_TO_OMG": CURRENCY_PAIR.ETH_TO_OMG,
        "ETH_TO_ZEC": CURRENCY_PAIR.ETH_TO_ZEC,
        "ETH_TO_REP": CURRENCY_PAIR.ETH_TO_REP,
        "ETH_TO_XMR": CURRENCY_PAIR.ETH_TO_XMR,
        "ETH_TO_NEO": CURRENCY_PAIR.ETH_TO_NEO,
        "ETH_TO_QTUM": CURRENCY_PAIR.ETH_TO_QTUM,
        "ETH_TO_EOS": CURRENCY_PAIR.ETH_TO_EOS,
        "ETH_TO_IOTA": CURRENCY_PAIR.ETH_TO_IOTA,
        "ETH_TO_BTG": CURRENCY_PAIR.ETH_TO_BTG,
        "ETH_TO_WTC": CURRENCY_PAIR.ETH_TO_WTC,
        "ETH_TO_KNC": CURRENCY_PAIR.ETH_TO_KNC,
        "ETH_TO_BAT": CURRENCY_PAIR.ETH_TO_BAT,
        "ETH_TO_ZRX": CURRENCY_PAIR.ETH_TO_ZRX,
        "ETH_TO_RDN": CURRENCY_PAIR.ETH_TO_RDN,
        "ETH_TO_GAS": CURRENCY_PAIR.ETH_TO_GAS,
        "ETH_TO_ADA": CURRENCY_PAIR.ETH_TO_ADA,
        "ETH_TO_RCN": CURRENCY_PAIR.ETH_TO_RCN,
        "ETH_TO_QSB": CURRENCY_PAIR.ETH_TO_QSP,
        "ETH_TO_XBY": CURRENCY_PAIR.ETH_TO_XBY,
        "ETH_TO_PAC": CURRENCY_PAIR.ETH_TO_PAC,
        "ETH_TO_RDD": CURRENCY_PAIR.ETH_TO_RDD,
        "ETH_TO_ICX": CURRENCY_PAIR.ETH_TO_ICX,
        "ETH_TO_WABI": CURRENCY_PAIR.ETH_TO_WABI,
        "ETH_TO_XLM": CURRENCY_PAIR.ETH_TO_XLM,
        "ETH_TO_TRX": CURRENCY_PAIR.ETH_TO_TRX,
        "ETH_TO_AION": CURRENCY_PAIR.ETH_TO_AION,
        "ETH_TO_ITC": CURRENCY_PAIR.ETH_TO_ITC,
        "ETH_TO_ARK": CURRENCY_PAIR.ETH_TO_ARK,
        "ETH_TO_STRAT": CURRENCY_PAIR.ETH_TO_STRAT,
        "ETH_TO_LSK": CURRENCY_PAIR.ETH_TO_LSK,
        "ETH_TO_ENG": CURRENCY_PAIR.ETH_TO_ENG,
        "ETH_TO_XVG": CURRENCY_PAIR.ETH_TO_XVG,
        "ETH_TO_ONT": CURRENCY_PAIR.ETH_TO_ONT,
        "ETH_TO_HSR": CURRENCY_PAIR.ETH_TO_HSR,
        "ETH_TO_ZIL": CURRENCY_PAIR.ETH_TO_ZIL,
        "ETH_TO_VEN": CURRENCY_PAIR.ETH_TO_VEN,
        "ETH_TO_ELF": CURRENCY_PAIR.ETH_TO_ELF,
        "ETH_TO_BLZ": CURRENCY_PAIR.ETH_TO_BLZ,
        "ETH_TO_REQ": CURRENCY_PAIR.ETH_TO_REQ,
        "ETH_TO_LINK": CURRENCY_PAIR.ETH_TO_LINK,
        "ETH_TO_NAS": CURRENCY_PAIR.ETH_TO_NAS,
        "ETH_TO_ELA": CURRENCY_PAIR.ETH_TO_ELA,
        "USD_TO_DASH": CURRENCY_PAIR.USD_TO_DASH,
        "USD_TO_BTC": CURRENCY_PAIR.USD_TO_BTC,
        "USD_TO_LTC": CURRENCY_PAIR.USD_TO_LTC,
        "USD_TO_XRP": CURRENCY_PAIR.USD_TO_XRP,
        "USD_TO_BCC": CURRENCY_PAIR.USD_TO_BCC,
        "USD_TO_ETC": CURRENCY_PAIR.USD_TO_ETC,
        "USD_TO_ETH": CURRENCY_PAIR.USD_TO_ETH,
        "USD_TO_ZEC": CURRENCY_PAIR.USD_TO_ZEC,
        "USD_TO_REP": CURRENCY_PAIR.USD_TO_REP,
        "USD_TO_XMR": CURRENCY_PAIR.USD_TO_XMR,
        "USDT_TO_DASH": CURRENCY_PAIR.USDT_TO_DASH,
        "USDT_TO_BTC": CURRENCY_PAIR.USDT_TO_BTC,
        "USDT_TO_LTC": CURRENCY_PAIR.USDT_TO_LTC,
        "USDT_TO_XRP": CURRENCY_PAIR.USDT_TO_XRP,
        "USDT_TO_BCC": CURRENCY_PAIR.USDT_TO_BCC,
        "USDT_TO_ETC": CURRENCY_PAIR.USDT_TO_ETC,
        "USDT_TO_ETH": CURRENCY_PAIR.USDT_TO_ETH,
        "USDT_TO_ZEC": CURRENCY_PAIR.USDT_TO_ZEC,
        "USDT_TO_REP": CURRENCY_PAIR.USDT_TO_REP,
        "USDT_TO_XMR": CURRENCY_PAIR.USDT_TO_XMR,
        "USDT_TO_NEO": CURRENCY_PAIR.USDT_TO_NEO,
        "USDT_TO_QTUM": CURRENCY_PAIR.USDT_TO_QTUM,
        "USDT_TO_EOS": CURRENCY_PAIR.USDT_TO_EOS,
        "USDT_TO_IOTA": CURRENCY_PAIR.USDT_TO_IOTA,
        "USDT_TO_BTG": CURRENCY_PAIR.USDT_TO_BTG,
        "USDT_TO_WTC": CURRENCY_PAIR.USDT_TO_WTC,
        "USDT_TO_KNC": CURRENCY_PAIR.USDT_TO_KNC,
        "USDT_TO_BAT": CURRENCY_PAIR.USDT_TO_BAT,
        "USDT_TO_ZRX": CURRENCY_PAIR.USDT_TO_ZRX,
        "USDT_TO_RDN": CURRENCY_PAIR.USDT_TO_RDN,
        "USDT_TO_GAS": CURRENCY_PAIR.USDT_TO_GAS,
        "USDT_TO_ADA": CURRENCY_PAIR.USDT_TO_ADA,
        "USDT_TO_RCN": CURRENCY_PAIR.USDT_TO_RCN,
        "USDT_TO_QSB": CURRENCY_PAIR.USDT_TO_QSP,
        "USDT_TO_XBY": CURRENCY_PAIR.USDT_TO_XBY,
        "USDT_TO_PAC": CURRENCY_PAIR.USDT_TO_PAC,
        "USDT_TO_RDD": CURRENCY_PAIR.USDT_TO_RDD,
        "USDT_TO_ICX": CURRENCY_PAIR.USDT_TO_ICX,
        "USDT_TO_WABI": CURRENCY_PAIR.USDT_TO_WABI,
        "USDT_TO_XLM": CURRENCY_PAIR.USDT_TO_XLM,
        "USDT_TO_TRX": CURRENCY_PAIR.USDT_TO_TRX,
        "USDT_TO_AION": CURRENCY_PAIR.USDT_TO_AION,
        "USDT_TO_ITC": CURRENCY_PAIR.USDT_TO_ITC,
        "USDT_TO_XVG": CURRENCY_PAIR.USDT_TO_XVG,
        "USDT_TO_OMG": CURRENCY_PAIR.USDT_TO_OMG,
        "USDT_TO_HSR": CURRENCY_PAIR.USDT_TO_HSR,
        "USDT_TO_ZIL": CURRENCY_PAIR.USDT_TO_ZIL,
        "USDT_TO_VEN": CURRENCY_PAIR.USDT_TO_VEN,
        "USDT_TO_ELF": CURRENCY_PAIR.USDT_TO_ELF,
        "USDT_TO_NAS": CURRENCY_PAIR.USDT_TO_NAS,
        "USDT_TO_ELA": CURRENCY_PAIR.USDT_TO_ELA,
        "USD_TO_USDT": CURRENCY_PAIR.USD_TO_USDT,
    }[pair_name.upper()]


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
        CURRENCY_PAIR.BTC_TO_OMG: "BTC_TO_OMG",
        CURRENCY_PAIR.BTC_TO_ZEC: "BTC_TO_ZEC",
        CURRENCY_PAIR.BTC_TO_REP: "BTC_TO_REP",
        CURRENCY_PAIR.BTC_TO_XMR: "BTC_TO_XMR",
        CURRENCY_PAIR.BTC_TO_DOGE: "BTC_TO_DOGE",
        CURRENCY_PAIR.BTC_TO_DCR: "BTC_TO_DCR",
        CURRENCY_PAIR.BTC_TO_NEO: "BTC_TO_NEO",
        CURRENCY_PAIR.BTC_TO_QTUM: "BTC_TO_QTUM",
        CURRENCY_PAIR.BTC_TO_EOS: "BTC_TO_EOS",
        CURRENCY_PAIR.BTC_TO_IOTA: "BTC_TO_IOTA",
        CURRENCY_PAIR.BTC_TO_BTG: "BTC_TO_BTG",
        CURRENCY_PAIR.BTC_TO_WTC: "BTC_TO_WTC",
        CURRENCY_PAIR.BTC_TO_KNC: "BTC_TO_KNC",
        CURRENCY_PAIR.BTC_TO_BAT: "BTC_TO_BAT",
        CURRENCY_PAIR.BTC_TO_ZRX: "BTC_TO_ZRX",
        CURRENCY_PAIR.BTC_TO_RDN: "BTC_TO_RDN",
        CURRENCY_PAIR.BTC_TO_GAS: "BTC_TO_GAS",
        CURRENCY_PAIR.BTC_TO_ADA: "BTC_TO_ADA",
        CURRENCY_PAIR.BTC_TO_RCN: "BTC_TO_RCN",
        CURRENCY_PAIR.BTC_TO_QSP: "BTC_TO_QSB",
        CURRENCY_PAIR.BTC_TO_XBY: "BTC_TO_XBY",
        CURRENCY_PAIR.BTC_TO_PAC: "BTC_TO_PAC",
        CURRENCY_PAIR.BTC_TO_RDD: "BTC_TO_RDD",
        CURRENCY_PAIR.BTC_TO_ICX: "BTC_TO_ICX",
        CURRENCY_PAIR.BTC_TO_WABI: "BTC_TO_WABI",
        CURRENCY_PAIR.BTC_TO_XLM: "BTC_TO_XLM",
        CURRENCY_PAIR.BTC_TO_TRX: "BTC_TO_TRX",
        CURRENCY_PAIR.BTC_TO_AION: "BTC_TO_AION",
        CURRENCY_PAIR.BTC_TO_ITC: "BTC_TO_ITC",
        CURRENCY_PAIR.BTC_TO_ARK: "BTC_TO_ARK",
        CURRENCY_PAIR.BTC_TO_STRAT: "BTC_TO_STRAT",
        CURRENCY_PAIR.BTC_TO_LSK: "BTC_TO_LSK",
        CURRENCY_PAIR.BTC_TO_ENG: "BTC_TO_ENG",
        CURRENCY_PAIR.BTC_TO_XVG: "BTC_TO_XVG",
        CURRENCY_PAIR.BTC_TO_ONT: "BTC_TO_ONT",
        CURRENCY_PAIR.BTC_TO_HSR: "BTC_TO_HSR",
        CURRENCY_PAIR.BTC_TO_ZIL: "BTC_TO_ZIL",
        CURRENCY_PAIR.BTC_TO_VEN: "BTC_TO_VEN",
        CURRENCY_PAIR.BTC_TO_ELF: "BTC_TO_ELF",
        CURRENCY_PAIR.BTC_TO_BLZ: "BTC_TO_BLZ",
        CURRENCY_PAIR.BTC_TO_REQ: "BTC_OT_REQ",
        CURRENCY_PAIR.BTC_TO_LINK: "BTC_TO_LINK",
        CURRENCY_PAIR.BTC_TO_NAS: "BTC_TO_NAS",
        CURRENCY_PAIR.BTC_TO_ELA: "BTC_TO_ELA",
        CURRENCY_PAIR.ETH_TO_DASH: "ETH_TO_DASH",
        CURRENCY_PAIR.ETH_TO_LTC: "ETH_TO_LTC",
        CURRENCY_PAIR.ETH_TO_XRP: "ETH_TO_XRP",
        CURRENCY_PAIR.ETH_TO_BCC: "ETH_TO_BCC",
        CURRENCY_PAIR.ETH_TO_ETC: "ETH_TO_ETC",
        CURRENCY_PAIR.ETH_TO_SC: "ETH_TO_SC",
        CURRENCY_PAIR.ETH_TO_DGB: "ETH_TO_DGB",
        CURRENCY_PAIR.ETH_TO_XEM: "ETH_TO_XEM",
        CURRENCY_PAIR.ETH_TO_OMG: "ETH_TO_OMG",
        CURRENCY_PAIR.ETH_TO_ZEC: "ETH_TO_ZEC",
        CURRENCY_PAIR.ETH_TO_REP: "ETH_TO_REP",
        CURRENCY_PAIR.ETH_TO_XMR: "ETH_TO_XMR",
        CURRENCY_PAIR.ETH_TO_NEO: "ETH_TO_NEO",
        CURRENCY_PAIR.ETH_TO_QTUM: "ETH_TO_QTUM",
        CURRENCY_PAIR.ETH_TO_EOS: "ETH_TO_EOS",
        CURRENCY_PAIR.ETH_TO_IOTA: "ETH_TO_IOTA",
        CURRENCY_PAIR.ETH_TO_BTG: "ETH_TO_BTG",
        CURRENCY_PAIR.ETH_TO_WTC: "ETH_TO_WTC",
        CURRENCY_PAIR.ETH_TO_KNC: "ETH_TO_KNC",
        CURRENCY_PAIR.ETH_TO_BAT: "ETH_TO_BAT",
        CURRENCY_PAIR.ETH_TO_ZRX: "ETH_TO_ZRX",
        CURRENCY_PAIR.ETH_TO_RDN: "ETH_TO_RDN",
        CURRENCY_PAIR.ETH_TO_GAS: "ETH_TO_GAS",
        CURRENCY_PAIR.ETH_TO_ADA: "ETH_TO_ADA",
        CURRENCY_PAIR.ETH_TO_RCN: "ETH_TO_RCN",
        CURRENCY_PAIR.ETH_TO_QSP: "ETH_TO_QSB",
        CURRENCY_PAIR.ETH_TO_XBY: "ETH_TO_XBY",
        CURRENCY_PAIR.ETH_TO_PAC: "ETH_TO_PAC",
        CURRENCY_PAIR.ETH_TO_RDD: "ETH_TO_RDD",
        CURRENCY_PAIR.ETH_TO_ICX: "ETH_TO_ICX",
        CURRENCY_PAIR.ETH_TO_WABI: "ETH_TO_WABI",
        CURRENCY_PAIR.ETH_TO_XLM: "ETH_TO_XLM",
        CURRENCY_PAIR.ETH_TO_TRX: "ETH_TO_TRX",
        CURRENCY_PAIR.ETH_TO_AION: "ETH_TO_AION",
        CURRENCY_PAIR.ETH_TO_ITC: "ETH_TO_ITC",
        CURRENCY_PAIR.ETH_TO_ARK: "ETH_TO_ARK",
        CURRENCY_PAIR.ETH_TO_STRAT: "ETH_TO_STRAT",
        CURRENCY_PAIR.ETH_TO_LSK: "ETH_TO_LSK",
        CURRENCY_PAIR.ETH_TO_ENG: "ETH_TO_ENG",
        CURRENCY_PAIR.ETH_TO_XVG: "ETH_TO_XVG",
        CURRENCY_PAIR.ETH_TO_ONT: "ETH_TO_ONT",
        CURRENCY_PAIR.ETH_TO_HSR: "ETH_TO_HSR",
        CURRENCY_PAIR.ETH_TO_ZIL: "ETH_TO_ZIL",
        CURRENCY_PAIR.ETH_TO_VEN: "ETH_TO_VEN",
        CURRENCY_PAIR.ETH_TO_ELF: "ETH_TO_ELF",
        CURRENCY_PAIR.ETH_TO_BLZ: "ETH_TO_BLZ",
        CURRENCY_PAIR.ETH_TO_REQ: "ETH_TO_REQ",
        CURRENCY_PAIR.ETH_TO_LINK: "ETH_TO_LINK",
        CURRENCY_PAIR.ETH_TO_NAS: "ETH_TO_NAS",
        CURRENCY_PAIR.ETH_TO_ELA: "ETH_TO_ELA",
        CURRENCY_PAIR.USD_TO_DASH: "USD_TO_DASH",
        CURRENCY_PAIR.USD_TO_BTC: "USD_TO_BTC",
        CURRENCY_PAIR.USD_TO_LTC: "USD_TO_LTC",
        CURRENCY_PAIR.USD_TO_XRP: "USD_TO_XRP",
        CURRENCY_PAIR.USD_TO_BCC: "USD_TO_BCC",
        CURRENCY_PAIR.USD_TO_ETC: "USD_TO_ETC",
        CURRENCY_PAIR.USD_TO_ETH: "USD_TO_ETH",
        CURRENCY_PAIR.USD_TO_ZEC: "USD_TO_ZEC",
        CURRENCY_PAIR.USD_TO_REP: "USD_TO_REP",
        CURRENCY_PAIR.USD_TO_XMR: "USD_TO_XMR",
        CURRENCY_PAIR.USDT_TO_DASH: "USDT_TO_DASH",
        CURRENCY_PAIR.USDT_TO_BTC: "USDT_TO_BTC",
        CURRENCY_PAIR.USDT_TO_LTC: "USDT_TO_LTC",
        CURRENCY_PAIR.USDT_TO_XRP: "USDT_TO_XRP",
        CURRENCY_PAIR.USDT_TO_BCC: "USDT_TO_BCC",
        CURRENCY_PAIR.USDT_TO_ETC: "USDT_TO_ETC",
        CURRENCY_PAIR.USDT_TO_ETH: "USDT_TO_ETH",
        CURRENCY_PAIR.USDT_TO_ZEC: "USDT_TO_ZEC",
        CURRENCY_PAIR.USDT_TO_REP: "USDT_TO_REP",
        CURRENCY_PAIR.USDT_TO_XMR: "USDT_TO_XMR",
        CURRENCY_PAIR.USDT_TO_NEO: "USDT_TO_NEO",
        CURRENCY_PAIR.USDT_TO_QTUM: "USDT_TO_QTUM",
        CURRENCY_PAIR.USDT_TO_EOS: "USDT_TO_EOS",
        CURRENCY_PAIR.USDT_TO_IOTA: "USDT_TO_IOTA",
        CURRENCY_PAIR.USDT_TO_BTG: "USDT_TO_BTG",
        CURRENCY_PAIR.USDT_TO_WTC: "USDT_TO_WTC",
        CURRENCY_PAIR.USDT_TO_KNC: "USDT_TO_KNC",
        CURRENCY_PAIR.USDT_TO_BAT: "USDT_TO_BAT",
        CURRENCY_PAIR.USDT_TO_ZRX: "USDT_TO_ZRX",
        CURRENCY_PAIR.USDT_TO_RDN: "USDT_TO_RDN",
        CURRENCY_PAIR.USDT_TO_GAS: "USDT_TO_GAS",
        CURRENCY_PAIR.USDT_TO_ADA: "USDT_TO_ADA",
        CURRENCY_PAIR.USDT_TO_RCN: "USDT_TO_RCN",
        CURRENCY_PAIR.USDT_TO_QSP: "USDT_TO_QSB",
        CURRENCY_PAIR.USDT_TO_XBY: "USDT_TO_XBY",
        CURRENCY_PAIR.USDT_TO_PAC: "USDT_TO_PAC",
        CURRENCY_PAIR.USDT_TO_RDD: "USDT_TO_RDD",
        CURRENCY_PAIR.USDT_TO_ICX: "USDT_TO_ICX",
        CURRENCY_PAIR.USDT_TO_WABI: "USDT_TO_WABI",
        CURRENCY_PAIR.USDT_TO_XLM: "USDT_TO_XLM",
        CURRENCY_PAIR.USDT_TO_TRX: "USDT_TO_TRX",
        CURRENCY_PAIR.USDT_TO_AION: "USDT_TO_AION",
        CURRENCY_PAIR.USDT_TO_ITC: "USDT_TO_ITC",
        CURRENCY_PAIR.USDT_TO_XVG: "USDT_TO_XVG",
        CURRENCY_PAIR.USDT_TO_OMG: "USDT_TO_OMG",
        CURRENCY_PAIR.USDT_TO_HSR: "USDT_TO_HSR",
        CURRENCY_PAIR.USDT_TO_ZIL: "USDT_TO_ZIL",
        CURRENCY_PAIR.USDT_TO_VEN: "USDT_TO_VEN",
        CURRENCY_PAIR.USDT_TO_ELF: "USDT_TO_ELF",
        CURRENCY_PAIR.USDT_TO_NAS: "USDT_TO_NAS",
        CURRENCY_PAIR.USDT_TO_ELA: "USDT_TO_ELA",
        CURRENCY_PAIR.USD_TO_USDT: "USD_TO_USDT",
    }[pair_id]


"""
    NOTE:   routine below is used only for balance retrieval
            supported currencies are
            ARBITRAGE_CURRENCY = [CURRENCY.DASH, CURRENCY.BCC, CURRENCY.XRP, CURRENCY.LTC, CURRENCY.ETC, CURRENCY.ETH]
"""


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
        CURRENCY.OMG: 'OMG',
        CURRENCY.ZEC: 'ZEC',
        CURRENCY.REP: 'REP',
        CURRENCY.XMR: 'XMR',
        CURRENCY.DOGE: 'DOGE',
        CURRENCY.DCR: 'DCR',
        CURRENCY.NEO: 'NEO',
        CURRENCY.QTUM: 'QTUM',
        CURRENCY.EOS: 'EOS',
        CURRENCY.IOTA: 'IOTA',
        CURRENCY.BTG: 'BTG',
        CURRENCY.WTC: 'WTC',
        CURRENCY.KNC: 'KNC',
        CURRENCY.BAT: 'BAT',
        CURRENCY.ZRX: 'ZRX',
        CURRENCY.RDN: 'RDN',
        CURRENCY.GAS: 'GAS',
        CURRENCY.ADA: 'ADA',
        CURRENCY.RCN: 'RCN',
        CURRENCY.QSP: 'QSB',
        CURRENCY.XBY: 'XBY',
        CURRENCY.PAC: 'PAC',
        CURRENCY.RDD: 'RDD',
        CURRENCY.ICX: 'ICX',
        CURRENCY.WABI: 'WABI',
        CURRENCY.XLM: 'XLM',
        CURRENCY.TRX: 'TRX',
        CURRENCY.AION: 'AION',
        CURRENCY.ITC: 'ITC',
        CURRENCY.ARK: 'ARK',
        CURRENCY.STRAT:'STRAT',
        CURRENCY.LSK: 'LSK',
        CURRENCY.ENG: 'ENG',
        CURRENCY.XVG: 'XVG',
        CURRENCY.ONT: 'ONT',
        CURRENCY.HSR: 'HSR',
        CURRENCY.ZIL: 'ZIL',
        CURRENCY.VEN: 'VEN',
        CURRENCY.ELF: 'ELF',
        CURRENCY.BLZ: 'BLZ',
        CURRENCY.REQ: 'REQ',
        CURRENCY.LINK: 'LINK',
        CURRENCY.NAS: 'NAS',
        CURRENCY.ELA: 'ELA',
        CURRENCY.USD: 'USD',
        CURRENCY.USDT: 'USDT'
    }[currency_id]


def get_currency_pair_name_by_exchange_id(pair_id, exchange_id):
    return {
        EXCHANGE.BITTREX: get_currency_pair_to_bittrex(pair_id),
        EXCHANGE.KRAKEN: get_currency_pair_to_kraken(pair_id),
        EXCHANGE.POLONIEX: get_currency_pair_to_poloniex(pair_id),
        EXCHANGE.BINANCE: get_currency_pair_to_binance(pair_id),
        EXCHANGE.HUOBI: get_currency_pair_to_huobi(pair_id),
    }[exchange_id]
