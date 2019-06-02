from AppiumLibrary.keywords.keywordgroup import KeywordGroup
import logging
__version__ = '1.0.0'


class ButtonManagement(KeywordGroup):

	def __init__(self):
		self.type = "Button"

	def get_button_text(self, locator):
		return self._get_element_attribute(locator, self.type, "Name")

	def get_button_helptext(self, locator):
		return self._get_element_attribute(locator, self.type, "HelpText")

	def is_button_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, self.type, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_button_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, self.type, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def button_should_be_enabled(self, locator):
		if not self.is_button_enabled:
			raise AssertionError("Button '{}' is not enabled".format(locator))

	def button_should_be_disabled(self, locator):
		if self.is_button_enabled:
			raise AssertionError("Button '{}' is not disabled".format(locator))

	def button_should_be_visible(self, locator):
		if not self.is_button_visible:
			raise AssertionError("Button '{}' is not visible".format(locator))

	def button_should_not_be_visible(self, locator):
		if self.is_button_visible:
			raise AssertionError("Button '{}' is not hidden".format(locator))

	def button_text_should_equal_to(self, locator, text):
		actual = self.get_button_text(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("Button '{}' has Text: '{}'. Expected: '{}'.".format(locator, text, actual))

	def click_on_button(self, locator):
		try:
			self._get_element_with_type(locator, self.type).click()
		except Exception:
			raise AssertionError("Cannot click on Button '{}'.".format(locator))

	def double_click_button(self, locator):
		try:
			ele = self._get_element_with_type(locator, self.type)
			self._double_click(ele)
		except Exception:
			raise AssertionError("Cannot double click on Button '{}'.".format(locator))

	def right_click_button(self, locator):
		try:
			ele = self._get_element_with_type(locator, self.type)
			self._right_click(ele)
		except Exception:
			raise AssertionError("Cannot right click on Button '{}'.".format(locator))
