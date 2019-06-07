from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "RadioButton"


class RadioButtonManagement(KeywordGroup):

	def get_radio_button_text(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "Name")

	def get_radio_button_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def is_radio_button_selected(self, locator):
		state = self._get_element_attribute(locator, __TYPE__, "SelectionItem.IsSelected")
		if str(state).lower() != "true":
			return False
		return True

	def is_radio_button_enabled(self, locator):
		state = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(state).lower() != "true":
			return False
		return True

	def is_radio_button_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def radio_button_should_be_enabled(self, locator):
		if not self.is_radio_button_enabled(locator):
			raise AssertionError("RadioButton '{}' is not enabled".format(locator))

	def radio_button_should_be_disabled(self, locator):
		if self.is_radio_button_enabled(locator):
			raise AssertionError("RadioButton '{}' is not disabled".format(locator))

	def radio_button_should_be_visible(self, locator):
		if not self.is_radio_button_visible(locator):
			raise AssertionError("RadioButton '{}' is not visible".format(locator))

	def radio_button_should_not_be_visible(self, locator):
		if self.is_radio_button_visible(locator):
			raise AssertionError("RadioButton '{}' is not hidden".format(locator))

	def radio_button_text_should_equal_to(self, locator, text):
		actual = self.get_radio_button_text(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("RadioButton '{}' has Text: '{}'. Expected: '{}'.".format(locator, actual, text))

	def radio_button_should_be_selected(self, locator):
		if not self.is_radio_button_selected(locator):
			raise AssertionError("RadioButton '{}' is not selected.".format(locator))

	def radio_button_should_not_be_selected(self, locator):
		if self.is_radio_button_selected(locator):
			raise AssertionError("RadioButton '{}' should not be selected.".format(locator))

	def click_on_radio_button(self, locator):
		try:
			self._get_element_with_type(locator, __TYPE__).click()
		except Exception:
			raise AssertionError("Cannot click on RadioButton '{}'.".format(locator))

	def double_click_radio_button(self, locator):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			self._double_click(ele)
		except Exception as e:
			raise AssertionError("Cannot double click on RadioButton '{}'. Exception: {}".format(locator, e))

	def right_click_radio_button(self, locator):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			self._right_click(ele)
		except Exception as e:
			raise AssertionError("Cannot right click on RadioButton '{}'. Exception: {}".format(locator, e))
