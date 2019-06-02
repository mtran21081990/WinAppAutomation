from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__version__ = '1.0.0'


class WindowManagement(KeywordGroup):

	def __init__(self):
		self.type = "Window"

	def get_window_title(self, locator):
		return self._get_element_attribute(locator, self.type, "Name")

	def get_window_handle(self, locator):
		return self._get_element_attribute(locator, self.type, "NativeWindowHandle")

	def get_window_helptext(self, locator):
		return self._get_element_attribute(locator, self.type, "HelpText")

	def is_window_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, self.type, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_window_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, self.type, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def window_should_be_enabled(self, locator):
		if not self.is_window_enabled:
			raise AssertionError("Window '{}' is not enabled".format(locator))

	def window_should_be_disabled(self, locator):
		if self.is_window_enabled:
			raise AssertionError("Window '{}' is not disabled".format(locator))

	def window_should_be_visible(self, locator):
		if not self.is_window_visible:
			raise AssertionError("Window '{}' is not visible".format(locator))

	def window_should_not_be_visible(self, locator):
		if self.is_window_visible:
			raise AssertionError("Window '{}' is not hidden".format(locator))

	def window_title_should_equal_to(self, locator, title):
		actual = self.get_window_title(locator)
		if str(title).lower() != actual.lower():
			raise AssertionError("Window '{}' has Title: '{}'. Expected: '{}'.".format(locator, title, actual))
