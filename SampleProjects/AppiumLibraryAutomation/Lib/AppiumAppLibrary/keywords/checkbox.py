from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "CheckBox"


class CheckboxManagement(KeywordGroup):

	def get_checkbox_text(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "Name")

	def get_checkbox_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def get_checkbox_check_state(self, locator):
		if self.is_checkbox_toggleable:
			return self._get_element_attribute(locator, __TYPE__, "Toggle.ToggleState")
		return None

	def is_checkbox_toggleable(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsTogglePatternAvailable")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_checkbox_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_checkbox_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def checkbox_should_be_enabled(self, locator):
		if not self.is_checkbox_enabled:
			raise AssertionError("CheckBox '{}' is not enabled".format(locator))

	def checkbox_should_be_disabled(self, locator):
		if self.is_checkbox_enabled:
			raise AssertionError("CheckBox '{}' is not disabled".format(locator))

	def checkbox_should_be_visible(self, locator):
		if not self.is_checkbox_visible:
			raise AssertionError("CheckBox '{}' is not visible".format(locator))

	def checkbox_should_not_be_visible(self, locator):
		if self.is_checkbox_visible:
			raise AssertionError("CheckBox '{}' is not hidden".format(locator))

	def checkbox_text_should_equal_to(self, locator, text):
		actual = self.get_checkbox_text(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("CheckBox '{}' has Text: '{}'. Expected: '{}'.".format(locator, text, actual))

	def checkbox_should_be_checked(self, locator):
		state = self.get_checkbox_check_state(locator)
		if int(state) != 1:
			raise AssertionError("CheckBox '{}' is not checked. Check State value: '{}'.".format(locator, state))

	def checkbox_should_not_be_checked(self, locator):
		state = self.get_checkbox_check_state(locator)
		if int(state) == 1:
			raise AssertionError("CheckBox '{}' should not be checked. Check State value: '{}'.".format(locator, state))

	def click_on_checkbox(self, locator):
		try:
			self._get_element_with_type(locator, __TYPE__).click()
		except Exception:
			raise AssertionError("Cannot click on CheckBox '{}'.".format(locator))

	def double_click_checkbox(self, locator):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			self._double_click(ele)
		except Exception:
			raise AssertionError("Cannot double click on CheckBox '{}'.".format(locator))

	def right_click_checkbox(self, locator):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			self._right_click(ele)
		except Exception:
			raise AssertionError("Cannot right click on CheckBox '{}'.".format(locator))
