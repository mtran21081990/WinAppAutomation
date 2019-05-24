from AppiumLibrary.keywords.keywordgroup import KeywordGroup
from AppiumLibrary.keywords._applicationmanagement import _ApplicationManagementKeywords

__version__ = '1.0.0'

_APPLICATION_APPIUM_URL_KEY = "APPIUM_URL"
_APPLICATION_PATH_KEY = "PATH"


class ApplicationManagementKeywords(_ApplicationManagementKeywords):

    def __init__(self):
        _ApplicationManagementKeywords.__init__(self)

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


