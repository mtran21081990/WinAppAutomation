from AppiumLibrary.keywords._element import _ElementKeywords

__version__ = '1.0.0'

_APPLICATION_MAIN_WINDOW_NAME_KEY = "MAIN_WINDOW_NAME"


class WindowManagementKeywords(_ElementKeywords):

    def __init__(self):
        _ElementKeywords.__init__(self)

    def _is_window_control(self, locator):
        return self.element_attribute_should_match(locator, "className", "Window")
    """
    def get_window_title(self, locator):
        if self._is_window_control(locator):
            return self.get_element_attribute(locator, "Name")
        else:
            raise AssertionError("Element with locator '%s' is not a Window" % locator)
    """
    def get_window_title(self, locator):
        return self.get_element_attribute(locator, "Name")

    def window_title_should_equal_to(self, locator, title):
        actual = str(self.get_window_title(locator))
        if str(title) != actual:
            raise AssertionError("Window '%s' with Title should be '%s' " "but it is '%s'." % locator, title, actual)
        return True

