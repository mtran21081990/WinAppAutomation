from robot.utils import plural_or_not, secs_to_timestr, timestr_to_secs
from .types import is_falsy, is_noney, is_string, is_truthy, PY3
from .librarylistener import LibraryListener
from .utilities import Utilities
from .errors import *

def escape_xpath_value(value):
    if '"' in value and '\'' in value:
        parts_wo_apos = value.split('\'')
        return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
    if '\'' in value:
        return "\"%s\"" % value
    return "'%s'" % value
