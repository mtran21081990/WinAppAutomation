from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "Button"


class ButtonManagement(KeywordGroup):

	def get_button_text(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "Name")

	def get_button_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def get_button_toggle_state(self, locator):
		if self.is_button_toggleable:
			return self._get_element_attribute(locator, __TYPE__, "Toggle.ToggleState")
		return None

	def is_button_toggleable(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsTogglePatternAvailable")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_button_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_button_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
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

	def button_should_be_toggled(self, locator):
		state = self.get_button_toggle_state(locator)
		if int(state) != 1:
			raise AssertionError("Button '{}' is not toggled. Toggle State value: '{}'.".format(locator, state))

	def button_should_not_be_toggled(self, locator):
		state = self.get_button_toggle_state(locator)
		if int(state) == 1:
			raise AssertionError("Button '{}' should not be toggled. Toggle State value: '{}'.".format(locator, state))

	def click_on_button(self, locator):
		try:
			self._get_element_with_type(locator, __TYPE__).click()
		except Exception:
			raise AssertionError("Cannot click on Button '{}'.".format(locator))

	def double_click_button(self, locator):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			self._double_click(ele)
		except Exception:
			raise AssertionError("Cannot double click on Button '{}'.".format(locator))

	def right_click_button(self, locator):
		try:
			ele = self._get_element_with_type(locator, __TYPE__)
			self._right_click(ele)
		except Exception:
			raise AssertionError("Cannot right click on Button '{}'.".format(locator))
