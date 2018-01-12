from enums.currency_pair import CURRENCY_PAIR
from enums.currency import CURRENCY


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
        CURRENCY.ICX: 'ICX',
        CURRENCY.WABI: 'WABI',
        CURRENCY.XLM: 'XLM',
        CURRENCY.TRX: 'TRX',
        CURRENCY.AION: 'AION',
        CURRENCY.ARK: 'ARK',
        CURRENCY.STRAT: 'STRAT',
        CURRENCY.USDT: 'USDT'
    }.get(currency_id)


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
        'OMG': CURRENCY.OMG,
        'ZEC': CURRENCY.ZEC,
        'REP': CURRENCY.REP,
        'XMR': CURRENCY.XMR,
        'DOGE': CURRENCY.DOGE,
        'DCR': CURRENCY.DCR,
        'NEO': CURRENCY.NEO,
        'QTUM': CURRENCY.QTUM,
        'EOS': CURRENCY.EOS,
        'IOTA': CURRENCY.IOTA,
        'BTG': CURRENCY.BTG,
        'WTC': CURRENCY.WTC,
        'KNC': CURRENCY.KNC,
        'BAT': CURRENCY.BAT,
        'ZRX': CURRENCY.ZRX,
        'RDN': CURRENCY.RDN,
        'GAS': CURRENCY.GAS,
        'ADA': CURRENCY.ADA,
        'RCN': CURRENCY.RCN,
        'ICX': CURRENCY.ICX,
        'WABI': CURRENCY.WABI,
        'XLM': CURRENCY.XLM,
        'TRX': CURRENCY.TRX,
        'AION': CURRENCY.AION,
        'ARK': CURRENCY.ARK,
        'STRAT': CURRENCY.STRAT,
        'USDT': CURRENCY.USDT
    }.get(currency_name)


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
        CURRENCY_PAIR.BTC_TO_OMG: 'BTC-OMG',
        CURRENCY_PAIR.BTC_TO_ZEC: 'BTC-ZEC',
        CURRENCY_PAIR.BTC_TO_REP: 'BTC-REP',
        CURRENCY_PAIR.BTC_TO_XMR: 'BTC-XMR',
        CURRENCY_PAIR.BTC_TO_DOGE: 'BTC-DOGE',
        CURRENCY_PAIR.BTC_TO_DCR: 'BTC-DCR',
        CURRENCY_PAIR.BTC_TO_NEO: 'BTC-NEO',
        CURRENCY_PAIR.BTC_TO_QTUM: 'BTC-QTUM',
        CURRENCY_PAIR.BTC_TO_BTG: 'BTC-BTG',
        CURRENCY_PAIR.BTC_TO_BAT: 'BTC-BAT',
        CURRENCY_PAIR.BTC_TO_ADA: 'BTC-ADA',
        CURRENCY_PAIR.BTC_TO_RCN: 'BTC-RCN',
        CURRENCY_PAIR.BTC_TO_RDD: 'BTC-RDD',
        CURRENCY_PAIR.BTC_TO_XLM: 'BTC-XLM',
        CURRENCY_PAIR.BTC_TO_ARK: 'BTC-ARK',
        CURRENCY_PAIR.BTC_TO_STRAT: 'BTC-STRAT',
        CURRENCY_PAIR.ETH_TO_DASH: 'ETH-DASH',
        CURRENCY_PAIR.ETH_TO_LTC: 'ETH-LTC',
        CURRENCY_PAIR.ETH_TO_XRP: 'ETH-XRP',
        CURRENCY_PAIR.ETH_TO_BCC: 'ETH-BCC',
        CURRENCY_PAIR.ETH_TO_ETC: 'ETH-ETC',
        CURRENCY_PAIR.ETH_TO_SC: 'ETH-SC',
        CURRENCY_PAIR.ETH_TO_DGB: 'ETH-DGB',
        CURRENCY_PAIR.ETH_TO_XEM: 'ETH-XEM',
        CURRENCY_PAIR.ETH_TO_OMG: 'ETH-OMG',
        CURRENCY_PAIR.ETH_TO_ZEC: 'ETH-ZEC',
        CURRENCY_PAIR.ETH_TO_REP: 'ETH-REP',
        CURRENCY_PAIR.ETH_TO_XMR: 'ETH-XMR',
        CURRENCY_PAIR.ETH_TO_NEO: 'ETH-NEO',
        CURRENCY_PAIR.ETH_TO_QTUM: 'ETH-QTUM',
        CURRENCY_PAIR.ETH_TO_BTG: 'ETH-BTG',
        CURRENCY_PAIR.ETH_TO_BAT: 'ETH-BAT',
        CURRENCY_PAIR.ETH_TO_ADA: 'ETH-ADA',
        CURRENCY_PAIR.ETH_TO_RCN: 'ETH-RCN',
        CURRENCY_PAIR.ETH_TO_XLM: 'ETH-XLM',
        CURRENCY_PAIR.ETH_TO_STRAT: 'ETH-STRAT',
        CURRENCY_PAIR.USDT_TO_DASH: 'USDT-DASH',
        CURRENCY_PAIR.USDT_TO_BTC: 'USDT-BTC',
        CURRENCY_PAIR.USDT_TO_LTC: 'USDT-LTC',
        CURRENCY_PAIR.USDT_TO_XRP: 'USDT-XRP',
        CURRENCY_PAIR.USDT_TO_BCC: 'USDT-BCC',
        CURRENCY_PAIR.USDT_TO_ETC: 'USDT-ETC',
        CURRENCY_PAIR.USDT_TO_ETH: 'USDT-ETH',
        CURRENCY_PAIR.USDT_TO_ZEC: 'USDT-ZEC',
        CURRENCY_PAIR.USDT_TO_XMR: 'USDT-XMR',
        CURRENCY_PAIR.USDT_TO_NEO: 'USDT-NEO',
        CURRENCY_PAIR.USDT_TO_BTG: 'USDT-BTG',
        CURRENCY_PAIR.USDT_TO_ADA: 'USDT-ADA'
    }.get(pair_id)


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
        'BTC-OMG': CURRENCY_PAIR.BTC_TO_OMG,
        'BTC-ZEC': CURRENCY_PAIR.BTC_TO_ZEC,
        'BTC-REP': CURRENCY_PAIR.BTC_TO_REP,
        'BTC-XMR': CURRENCY_PAIR.BTC_TO_XMR,
        'BTC-DOGE': CURRENCY_PAIR.BTC_TO_DOGE,
        'BTC-DCR': CURRENCY_PAIR.BTC_TO_DCR,
        'BTC-NEO': CURRENCY_PAIR.BTC_TO_NEO,
        'BTC-QTUM': CURRENCY_PAIR.BTC_TO_QTUM,
        'BTC-BTG': CURRENCY_PAIR.BTC_TO_BTG,
        'BTC-BAT': CURRENCY_PAIR.BTC_TO_BAT,
        'BTC-ADA': CURRENCY_PAIR.BTC_TO_ADA,
        'BTC-RCN': CURRENCY_PAIR.BTC_TO_RCN,
        'BTC-RDD': CURRENCY_PAIR.BTC_TO_RDD,
        'BTC-XLM': CURRENCY_PAIR.BTC_TO_XLM,
        'BTC-ARK': CURRENCY_PAIR.BTC_TO_ARK,
        'BTC-STRAT': CURRENCY_PAIR.BTC_TO_STRAT,
        'ETH-DASH': CURRENCY_PAIR.ETH_TO_DASH,
        'ETH-LTC': CURRENCY_PAIR.ETH_TO_LTC,
        'ETH-XRP': CURRENCY_PAIR.ETH_TO_XRP,
        'ETH-BCC': CURRENCY_PAIR.ETH_TO_BCC,
        'ETH-ETC': CURRENCY_PAIR.ETH_TO_ETC,
        'ETH-SC': CURRENCY_PAIR.ETH_TO_SC,
        'ETH-DGB': CURRENCY_PAIR.ETH_TO_DGB,
        'ETH-XEM': CURRENCY_PAIR.ETH_TO_XEM,
        'ETH-OMG': CURRENCY_PAIR.ETH_TO_OMG,
        'ETH-ZEC': CURRENCY_PAIR.ETH_TO_ZEC,
        'ETH-REP': CURRENCY_PAIR.ETH_TO_REP,
        'ETH-XMR': CURRENCY_PAIR.ETH_TO_XMR,
        'ETH-NEO': CURRENCY_PAIR.ETH_TO_NEO,
        'ETH-QTUM': CURRENCY_PAIR.ETH_TO_QTUM,
        'ETH-BTG': CURRENCY_PAIR.ETH_TO_BTG,
        'ETH-BAT': CURRENCY_PAIR.ETH_TO_BAT,
        'ETH-ADA': CURRENCY_PAIR.ETH_TO_ADA,
        'ETH-RCN': CURRENCY_PAIR.ETH_TO_RCN,
        'ETH-XLM': CURRENCY_PAIR.ETH_TO_XLM,
        'ETH-STRAT': CURRENCY_PAIR.ETH_TO_STRAT,
        'USDT-DASH': CURRENCY_PAIR.USDT_TO_DASH,
        'USDT-BTC': CURRENCY_PAIR.USDT_TO_BTC,
        'USDT-LTC': CURRENCY_PAIR.USDT_TO_LTC,
        'USDT-XRP': CURRENCY_PAIR.USDT_TO_XRP,
        'USDT-BCC': CURRENCY_PAIR.USDT_TO_BCC,
        'USDT-ETC': CURRENCY_PAIR.USDT_TO_ETC,
        'USDT-ETH': CURRENCY_PAIR.USDT_TO_ETH,
        'USDT-ZEC': CURRENCY_PAIR.USDT_TO_ZEC,
        'USDT-XMR': CURRENCY_PAIR.USDT_TO_XMR,
        'USDT-NEO': CURRENCY_PAIR.USDT_TO_NEO,
        'USDT-BTG': CURRENCY_PAIR.USDT_TO_BTG,
        'USDT-ADA': CURRENCY_PAIR.USDT_TO_ADA
    }.get(pair_name)