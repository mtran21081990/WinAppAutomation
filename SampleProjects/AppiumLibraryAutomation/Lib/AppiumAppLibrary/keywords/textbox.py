from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "TextBox"


class TextboxManagement(KeywordGroup):

	def get_textbox_text(self, locator):
		return self._get_element_with_type(locator, __TYPE__).text

	def get_textbox_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def get_textbox_location(self, locator):
		return self._get_element_with_type(locator, __TYPE__).location

	def get_textbox_size(self, locator):
		return self._get_element_with_type(locator, __TYPE__).size

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
		if not self.is_textbox_enabled(locator):
			raise AssertionError("Textbox '{}' is not enabled".format(locator))

	def textbox_should_be_disabled(self, locator):
		if self.is_textbox_enabled(locator):
			raise AssertionError("Textbox '{}' is not disabled".format(locator))

	def textbox_should_be_visible(self, locator):
		if not self.is_textbox_visible(locator):
			raise AssertionError("Textbox '{}' is not visible".format(locator))

	def textbox_should_not_be_visible(self, locator):
		if self.is_textbox_visible(locator):
			raise AssertionError("Textbox '{}' is not hidden".format(locator))

	def textbox_text_should_equal_to(self, locator, text):
		actual = self.get_textbox_text(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("Textbox '{}' has Text: '{}'. Expected: '{}'.".format(locator, actual, text))

	def input_into_textbox(self, locator, text):
		try:
			self._get_element_with_type(locator, __TYPE__).send_keys(text)
		except Exception as e:
			raise AssertionError("Cannot input '{}' into Textbox '{}'. Exception: {}".format(text, locator, e))

	def clear_textbox(self, locator):
		try:
			self._get_element_with_type(locator, __TYPE__).clear()
		except Exception as e:
			raise AssertionError("Cannot clear Textbox '{}'. Exception: {}".format(locator, e))
