from .utilities import Utilities
from robot.utils import is_string
from robot.utils import plural_or_not, secs_to_timestr, timestr_to_secs
try:
    from robot.utils import PY3
except ImportError:
    import sys
    PY3 = sys.version_info[0] == 3


def is_truthy(item):
    if is_string(item):
        return item.upper() not in ('FALSE', 'NO', '', 'NONE')
    return bool(item)


def is_falsy(item):
    return not is_truthy(item)


def is_noney(item):
    return item is None or is_string(item) and item.upper() == 'NONE'


def escape_xpath_value(value):
    if '"' in value and '\'' in value:
        parts_wo_apos = value.split('\'')
        return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
    if '\'' in value:
        return "\"%s\"" % value
    return "'%s'" % value
