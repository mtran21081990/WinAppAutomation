from AppiumLibrary.keywords.keywordgroup import KeywordGroup
import time

__TYPE__ = "ComboBox"


class ComboboxManagement(KeywordGroup):

	def get_combobox_selection(self, locator):
		return self._get_element_with_type(locator, __TYPE__).text

	def get_combobox_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def is_combobox_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_combobox_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def combobox_should_be_enabled(self, locator):
		if not self.is_combobox_enabled:
			raise AssertionError("ComboBox '{}' is not enabled".format(locator))

	def combobox_should_be_disabled(self, locator):
		if self.is_combobox_enabled:
			raise AssertionError("ComboBox '{}' is not disabled".format(locator))

	def combobox_should_be_visible(self, locator):
		if not self.is_combobox_visible:
			raise AssertionError("ComboBox '{}' is not visible".format(locator))

	def combobox_should_not_be_visible(self, locator):
		if self.is_combobox_visible:
			raise AssertionError("ComboBox '{}' is not hidden".format(locator))

	def combobox_selection_should_equal_to(self, locator, text):
		actual = self.get_combobox_selection(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("ComboBox '{}' has Selection: '{}'. Expected: '{}'.".format(locator, text, actual))

	def select_value_on_combobox(self, locator, value):
		try:
			self._get_element_with_type(locator, __TYPE__).click()
			time.sleep(1)
			self.click_element("name="+value)
		except Exception:
			raise AssertionError("Cannot select value '{}' on ComboBox '{}'.".format(value, locator))
