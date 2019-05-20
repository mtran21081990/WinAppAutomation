from AppiumLibrary import AppiumLibrary
from .keywords import *
from .utils import *
import sys

__version__ = '1.0.0'
_APPLICATION_APPIUM_URL_KEY = "APPIUM_URL"
_APPLICATION_PATH_KEY = "PATH"
_APPLICATION_NAME_KEY = "APPLICATION_NAME"
_APPLICATION_MAIN_WINDOW_NAME_KEY = "MAIN_WINDOW_NAME"
_APPLICATION_DEFAULT_USERNAME_KEY = "DEFAULT_USERNAME"
_APPLICATION_DEFAULT_PASSWORD_KEY = "DEFAULT_PASSWORD"


class AppiumAppLibrary(AppiumLibrary, SikuliWrapperKeywords):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, timeout=5.0, implicit_wait=0.0, run_on_failure='Capture Screen'):

        self.utils = Utilities()
        self.timeout = timestr_to_secs(timeout)
        self.implicit_wait = timestr_to_secs(implicit_wait)
        self.speed = 0.0
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()

        AppiumLibrary.__init__(self, self.timeout, run_on_failure)
        SikuliWrapperKeywords.__init__(self)

        ####################################################################################
        # Make sure pydevd installed: pip install pydevd
        # AND Uncomment following codes to enable debug mode
        # sys.path.append("pycharm-debug-py3k.egg")
        # import pydevd
        # pydevd.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)
        ####################################################################################

    def get_applicable_name(self, name):
        return name + "_" + self.utils.get_current_datetime_as_name()

    def setup_application(self, settings):
        """
        Open application or attach the already-opened application
        :settings: dictionary of browser setting. Sample:
        APPLICATION:
          TYPE: wpf
          ALREADY_OPENED: No
          NAME: WpfTestApplication
          PATH: absolute/path/to/app.exe
          DEFAULT_USERNAME: admin
          DEFAULT_PASSWORD: password
        """
        # init application
        appium_url = settings.get(_APPLICATION_APPIUM_URL_KEY).strip().lower()
        application_path = settings.get(_APPLICATION_PATH_KEY, None)
        kwargs = {"platformName": "Windows", "deviceName": "tbd", "app": application_path}
        self.open_application(appium_url, None, **kwargs)

    def click_item_on_application(self, locator):
        self.click_element(locator)
