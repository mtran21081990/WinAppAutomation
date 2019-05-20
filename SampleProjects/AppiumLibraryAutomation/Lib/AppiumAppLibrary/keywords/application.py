from AppiumLibrary.keywords import _ApplicationManagementKeywords
from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__version__ = '1.0.1'

_APPLICATION_APPIUM_URL_KEY = "APPIUM_URL"
_APPLICATION_PATH_KEY = "PATH"
_APPLICATION_NAME_KEY = "APPLICATION_NAME"
_APPLICATION_MAIN_WINDOW_NAME_KEY = "MAIN_WINDOW_NAME"
_APPLICATION_DEFAULT_USERNAME_KEY = "DEFAULT_USERNAME"
_APPLICATION_DEFAULT_PASSWORD_KEY = "DEFAULT_PASSWORD"


class ApplicationManagementKeywords(KeywordGroup):

    def __init__(self):
        self.application_management = _ApplicationManagementKeywords()
