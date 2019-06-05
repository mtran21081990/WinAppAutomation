from AppiumLibrary import AppiumLibrary
from selenium.webdriver.common.action_chains import ActionChains
from .keywords import *
from .utils import *
import logging
import sys

__version__ = '1.0.0'


class AppiumAppLibrary(AppiumLibrary, SikuliWrapper, ApplicationManagement, WindowManagement, ButtonManagement,
                       TextboxManagement, ComboboxManagement, RadioButtonManagement, CheckboxManagement,
                       ListboxManagement):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, timeout=60.0, implicit_wait=0.0):

        self.utils = Utilities()
        self.timeout = timestr_to_secs(timeout)
        self.implicit_wait = timestr_to_secs(implicit_wait)
        self.speed = 0.0

        AppiumLibrary.__init__(self, self.timeout)
        SikuliWrapper.__init__(self)
        ApplicationManagement.__init__(self)
        WindowManagement.__init__(self)
        ButtonManagement.__init__(self)
        TextboxManagement.__init__(self)
        ComboboxManagement.__init__(self)
        RadioButtonManagement.__init__(self)
        CheckboxManagement.__init__(self)
        ListboxManagement.__init__(self)

        ####################################################################################
        # Make sure pydevd installed: pip install pydevd
        # AND Uncomment following codes to enable debug mode
        # sys.path.append("pycharm-debug-py3k.egg")
        # import pydevd
        # pydevd.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)
        ####################################################################################

    def _get_element(self, locator):
        eles = self._get_elements(locator)
        if len(eles) > 1:
            message = "CAUTION: Locator '{}' matched {} elements. Use the 1st element.".format(locator, len(eles))
            logging.warning(message)
        return eles[0]

    def _get_elements(self, locator):
        eles = self._element_find(locator, False, True)
        if len(eles) == 0:
            raise AssertionError("Element '%s' could not be found" % locator)
        else:
            return eles

    def _get_element_with_type(self, locator, control_type):
        eles = self._get_elements(locator)
        ele_len = len(eles)
        if ele_len > 1:
            arr = []
            for ele in eles:
                if str(ele.get_attribute("ClassName")).lower() == str(control_type).lower():
                    arr.append(ele)
            logging.warning("CAUTION: Locator '{}' matched {} elements with type '{}'. Use the first element.".format(
                locator, ele_len, control_type))
            return arr[0]
        else:
            ele_type = eles[0].get_attribute("ClassName")
            if str(ele_type).lower() != str(control_type).lower():
                raise AssertionError("Element '{}' is not a {}. Its type is {}".format(locator, control_type, ele_type))
            return eles[0]

    def _get_element_attribute(self, locator, control_type, attribute):
        ele = self._get_element_with_type(locator, control_type)
        try:
            attr_val = ele.get_attribute(attribute)
            self._info("Element '%s' attribute '%s' value '%s' " % (locator, attribute, attr_val))
            return attr_val
        except Exception as e:
            raise AssertionError("Attribute '{}' is not valid for element '{}'. Exception: ".format(
                attribute, locator, e))

    def _click(self, ele=None):
        actions = ActionChains(self._current_application())
        actions.double_click(ele)
        actions.perform()

    def _double_click(self, ele=None):
        actions = ActionChains(self._current_application())
        actions.double_click(ele)
        actions.perform()

    def _right_click(self, ele=None):
        actions = ActionChains(self._current_application())
        actions.context_click(ele)
        actions.perform()

    def _drag_and_drop(self, source_element, target_element):
        actions = ActionChains(self._current_application())
        actions.drag_and_drop(source_element, target_element)
        actions.perform()

    def _drag_and_drop_by_offset(self, source_element, x_offset, y_offset):
        actions = ActionChains(self._current_application())
        actions.drag_and_drop_by_offset(source_element, x_offset, y_offset)
        actions.perform()

    def _send_keys_on_element(self, value):
        actions = ActionChains(self._current_application())
        actions.send_keys(value)
        actions.perform()

    @staticmethod
    def _change_locator_to_xpath(locator):
        if locator.startswith('//'):
            return locator
        else:
            prefix = ""
            criteria = ""
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0].strip().lower()
                criteria = "='" + locator_parts[2].strip() + "'"
            switcher = {
                "accessibility_id": "@AutomationId",
                "name": "@Name",
            }
            x_locator = switcher.get(prefix) + criteria
            return x_locator
