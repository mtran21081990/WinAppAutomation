from builtins import staticmethod
import logging
from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords import ApplicationKeywords

__version__ = '1.0.1'

_APPLICATION_TYPE_KEY = "TYPE"
_APPLICATION_PATH_KEY = "PATH"
_APPLICATION_NAME_KEY = "APPLICATION_NAME"
_APPLICATION_MAIN_WINDOW_NAME_KEY = "MAIN_WINDOW_NAME"
_APPLICATION_ALREADY_OPENED_KEY = "ALREADY_OPENED"
_APPLICATION_DEFAULT_USERNAME_KEY = "DEFAULT_USERNAME"
_APPLICATION_DEFAULT_PASSWORD_KEY = "DEFAULT_PASSWORD"


class ApplicationManagementKeywords(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.application_management = ApplicationKeywords(ctx)

    @keyword
    def run_or_attach_application(self, settings):
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
        application_type = settings.get(_APPLICATION_TYPE_KEY).strip().lower()
        application_path = settings.get(_APPLICATION_PATH_KEY, None)
        application_name = settings.get(_APPLICATION_NAME_KEY, None)
        application_opened = settings.get(_APPLICATION_ALREADY_OPENED_KEY, "no").lower()

        if application_opened == "yes" or application_opened == "y" or application_opened == "true":
            if self._is_process_id(application_name):
                self.application_management.attach_application_by_id(application_name)
            else:
                self.application_management.attach_application_by_name(application_name)
        else:
            self.application_management.launch_application(application_path)

    @staticmethod
    def _is_process_id(temp):
        try:
            int(temp)
            return True
        except ValueError:
            return False

    def get_windows(self):
        return self.application_management.state.app.GetWindows()
