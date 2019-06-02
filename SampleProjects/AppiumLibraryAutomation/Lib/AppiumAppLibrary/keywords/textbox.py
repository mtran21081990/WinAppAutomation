from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "TextBox"


class TextboxManagement(KeywordGroup):

	def get_textbox_text(self, locator):
		ele = self._get_element_with_type(locator, __TYPE__)
		return ele.text

	def get_textbox_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def is_textbox_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_textbox_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def textbox_should_be_enabled(self, locator):
		if not self.is_textbox_enabled:
			raise AssertionError("Textbox '{}' is not enabled".format(locator))

	def textbox_should_be_disabled(self, locator):
		if self.is_textbox_enabled:
			raise AssertionError("Textbox '{}' is not disabled".format(locator))

	def textbox_should_be_visible(self, locator):
		if not self.is_textbox_visible:
			raise AssertionError("Textbox '{}' is not visible".format(locator))

	def textbox_should_not_be_visible(self, locator):
		if self.is_textbox_visible:
			raise AssertionError("Textbox '{}' is not hidden".format(locator))

	def textbox_text_should_equal_to(self, locator, text):
		actual = self.get_textbox_text(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("Textbox '{}' has Text: '{}'. Expected: '{}'.".format(locator, text, actual))

	def input_into_textbox(self, locator, text):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			ele.send_keys(text)
		except Exception:
			raise AssertionError("Cannot input '{}' into Textbox '{}'.".format(text, locator))

	def clear_textbox(self, locator):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			ele.clear()
		except Exception:
			raise AssertionError("Cannot clear Textbox '{}'.".format(locator))
