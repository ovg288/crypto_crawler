DEBUG_ENABLED = True

LOG_ALL_ERRORS = 5
LOG_ALL_MARKET_RELATED_CRAP = 10
LOG_ALL_MARKET_NETWORK_RELATED_CRAP = 100
LOG_ALL_DEBUG = 200
LOG_ALL_OTHER_STUFF = 1000

DEBUG_LEVEL = LOG_ALL_DEBUG # LOG_ALL_MARKET_RELATED_CRAP


def should_print_debug():
    return DEBUG_ENABLED


def print_to_console(msg, debug_level):
    if debug_level <= DEBUG_LEVEL:
        print msg
