from AppiumLibrary import AppiumLibrary
from .keywords import *
from .utils import *
import sys

__version__ = '1.0.0'


class AppiumAppLibrary(AppiumLibrary, SikuliWrapperKeywords, ApplicationManagementKeywords, WindowManagementKeywords):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, timeout=30.0, implicit_wait=0.0):

        self.utils = Utilities()
        self.timeout = timestr_to_secs(timeout)
        self.implicit_wait = timestr_to_secs(implicit_wait)
        self.speed = 0.0

        AppiumLibrary.__init__(self, self.timeout)
        SikuliWrapperKeywords.__init__(self)
        ApplicationManagementKeywords.__init__(self)
        WindowManagementKeywords.__init__(self)

        ####################################################################################
        # Make sure pydevd installed: pip install pydevd
        # AND Uncomment following codes to enable debug mode
        # sys.path.append("pycharm-debug-py3k.egg")
        # import pydevd
        # pydevd.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)
        ####################################################################################

    def switch_to_new_window(self, new_window_locator, new_window_alias):
        self.switch_application("Root")
        new_window = self._element_find(new_window_locator, True, True)
        new_window_handle = new_window.get_attribute("NativeWindowHandle")
        hex_handle = hex(int(new_window_handle))
        kwargs = {"platformName": "Windows", "deviceName": "tbd", "appTopLevelWindow": hex_handle}
        self.open_application(self.appium_url, new_window_alias, **kwargs)


