from WhiteLibrary import WhiteLibrary
from .keywords import *
from .utils import *
import sys

__version__ = '1.0.0'


class WhiteAppLibrary(WhiteLibrary):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, timeout=5.0, implicit_wait=0.0):

        WhiteLibrary.__init__(self)

        self.sikuli_manager = SikuliWrapper(self)
        self.screenshot_manager = ScreenshotManagement(self)
        self.application_manager = ApplicationManagement(self)
        self.window_manager = WindowManagement(self)
        self.element_manager = ElementManagement(self)
        self.button_manager = ButtonManagement(self)
        self.label_manager = LabelManagement(self)
        self.list_manager = ListManagement(self)
        self.menu_manager = MenuManagement(self)
        self.slider_manager = SliderManagement(self)
        self.spinner_manager = SpinnerManagement(self)
        self.tree_manager = TreeManagement(self)
        self.datetime_picker_manager = DateTimePickerManagement(self)
        self.tab_manager = TabManagement(self)
        self.textbox_manager = TextBoxManagement(self)
        self.calendar_manager = CalendarManagement(self)
        self.utils = Utilities()

        arr_libraries = [self.sikuli_manager, self.screenshot_manager, self.application_manager, self.window_manager,
                         self.element_manager, self.button_manager, self.label_manager, self.list_manager,
                         self.menu_manager, self.slider_manager, self.spinner_manager, self.tree_manager,
                         self.datetime_picker_manager, self.tab_manager, self.textbox_manager, self.calendar_manager]
        self.libraries.append(arr_libraries)
        self.add_library_components(arr_libraries)

        self.timeout = timestr_to_secs(timeout)
        self.implicit_wait = timestr_to_secs(implicit_wait)
        self.speed = 0.0
        ####################################################################################
        # Make sure pydevd installed: pip install pydevd
        # AND Uncomment following codes to enable debug mode
        # sys.path.append("pycharm-debug-py3k.egg")
        # import pydevd
        # pydevd.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)
        ####################################################################################

    def _end_keyword(self, name, attrs):
        if self.screenshot_type == 'desktop' and self.screenshots_enabled:
            self.screenshot_manager.take_window_screenshot()

    def verify_string_value(self, expected, actual, case_sensitive=True):
        self._verify_string_value(expected, actual, case_sensitive)

    def verify_value(self, expected, actual):
        self._verify_value(expected, actual)

    def get_typed_item_by_locator(self, item_type, locator):
        return self._get_typed_item_by_locator(item_type, locator)

    def get_item_by_locator(self, locator):
        return self._get_item_by_locator(locator)

    def get_search_criteria(self, locator):
        return self._get_search_criteria(locator)
