import os
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.utils import get_link_path
from ..base import LibraryComponent
from WhiteLibrary.keywords import ScreenshotKeywords
from WhiteLibrary.keywords.robotlibcore import keyword, PY2
from System.Drawing.Imaging import ImageFormat
from TestStack.White import Desktop

__version__ = '1.0.1'


class ScreenshotManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.screenshot_management = ScreenshotKeywords(ctx)

    @keyword
    def take_window_screenshot(self):
        filepath = self._get_screenshot_path("whitelib_screenshot_{index}.jpeg")
        logger.info(get_link_path(filepath, self._log_directory))
        logger.info(
            '</td></tr><tr><td colspan="3">''<a href="{src}"><img src="{src}" width="800px"></a>'.format(
                src=get_link_path(filepath, self._log_directory)), html=True)
        #logger.info("Window Bound: " + str(self.ctx.window_manager.window_management.state.window.Bounds))
        bmp = Desktop.CaptureScreenshot()
        bmp.Save(filepath, ImageFormat.Jpeg)
        return filepath

    @property
    def _log_directory(self):
        try:
            logfile = BuiltIn().get_variable_value('${LOG FILE}')
            if logfile is None:
                return BuiltIn().get_variable_value('${OUTPUTDIR}')
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwdu() if PY2 else os.getcwd()

    def _get_screenshot_path(self, filename):
        directory = self._log_directory
        filename = filename.replace('/', os.sep)
        index = 0
        while True:
            index += 1
            formatted = filename.format(index=index)
            filepath = os.path.join(directory, formatted)
            # filename didn't contain {index} or unique path was found
            if formatted == filename or not os.path.exists(filepath):
                return filepath

