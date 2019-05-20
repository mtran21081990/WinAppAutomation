# Copyright 2008-2011 Nokia Networks
# Copyright 2011-2016 Ryan Tomac, Ed Manlove and contributors
# Copyright 2016-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

from ..utils import is_noney, timestr_to_secs

from .context import ContextAware
from WhiteLibrary.keywords.robotlibcore import PY2


class LibraryComponent(ContextAware):

    def __init__(self, ctx):
        ContextAware.__init__(self, ctx)

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
