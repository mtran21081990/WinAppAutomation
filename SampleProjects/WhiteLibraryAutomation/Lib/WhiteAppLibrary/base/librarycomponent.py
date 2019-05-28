import clr
import os
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from ..utils import is_noney, timestr_to_secs
from WhiteLibrary.keywords.robotlibcore import PY2

clr.AddReference("TestStack.White")


class LibraryComponent(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def info(self, msg, html=False):
        logger.info(msg, html)

    def debug(self, msg, html=False):
        logger.debug(msg, html)

    def log(self, msg, level='INFO', html=False):
        if not is_noney(level):
            logger.write(msg, level.upper(), html)

    def warn(self, msg, html=False):
        logger.warn(msg, html)

    def log_source(self, loglevel='INFO'):
        self.ctx.log_source(loglevel)

    def get_timeout(self, timeout=None):
        if is_noney(timeout):
            return self.ctx.timeout
        return timestr_to_secs(timeout)

    @property
    def log_dir(self):
        try:
            logfile = BuiltIn().get_variable_value('${LOG FILE}')
            if logfile == 'NONE':
                return BuiltIn().get_variable_value('${OUTPUTDIR}')
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwdu() if PY2 else os.getcwd()
