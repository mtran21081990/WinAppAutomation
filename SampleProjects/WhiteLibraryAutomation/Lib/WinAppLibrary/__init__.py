from WhiteLibrary import WhiteLibrary
from WhiteLibrary.keywords.robotlibcore import keyword
from .keywords import *
from .utils import *
import sys

__version__ = '1.0.0'


class WinAppLibrary(WhiteLibrary):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, timeout=5.0, implicit_wait=0.0, run_on_failure='Capture Screen'):

        WhiteLibrary.__init__(self)

        self.application = ApplicationManagementKeywords(self)
        self.window = WindowManagementKeywords(self)
        self.element = ElementManagementKeywords(self)
        self.sikuli = SikuliWrapperKeywords(self)
        self.utils = Utilities()

        arr_libraries = [self.sikuli, self.application, self.window, self.element]
        self.libraries.append(arr_libraries)
        self.add_library_components(arr_libraries)

        self.timeout = timestr_to_secs(timeout)
        self.implicit_wait = timestr_to_secs(implicit_wait)
        self.speed = 0.0
        self.run_on_failure_keyword = run_on_failure
        ####################################################################################
        # Make sure pydevd installed: pip install pydevd
        # AND Uncomment following codes to enable debug mode
        # sys.path.append("pycharm-debug-py3k.egg")
        # import pydevd
        # pydevd.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)
        ####################################################################################

    @keyword
    def setup_application(self, settings):
        # Run or Attach application depends on Setting file
        self.application.run_or_attach_application(settings)

        # Attach main window
        self.window.attach_main_window(settings)

    @keyword
    def get_applicable_name(self, name):
        return name + "_" + self.utils.get_current_datetime_as_name()
