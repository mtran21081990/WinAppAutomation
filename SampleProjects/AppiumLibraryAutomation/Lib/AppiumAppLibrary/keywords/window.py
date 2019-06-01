from AppiumLibrary.keywords.keywordgroup import KeywordGroup
import logging
__version__ = '1.0.0'


class WindowManagement(KeywordGroup):

    def _is_window_control(self, locator):
        class_name = self.get_element_attribute(locator, "ClassName")
        if class_name != "Window":
            raise AssertionError("Element with locator '%s' is not a Window" % locator)
        return True

    def get_window_title(self, locator):
        if self._is_window_control(locator):
            return self.get_element_attribute(locator, "Name")
        return ""

    def window_title_should_equal_to(self, locator, title):
        actual = str(self.get_window_title(locator))
        if str(title) != actual:
            raise AssertionError("Window '%s' with Title should be '%s' " "but it is '%s'." % locator, title, actual)
