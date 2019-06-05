from AppiumLibrary.keywords.keywordgroup import KeywordGroup
from selenium.webdriver.common.keys import Keys
import logging
import time

__TYPE__ = "ComboBox"
__POPUP_TYPE__ = "Popup"
__ITEM_TYPE__ = "ListBoxItem"


class ComboboxManagement(KeywordGroup):

	def get_combobox_selection(self, locator):
		return self._get_element_with_type(locator, __TYPE__).text

	def get_combobox_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def get_combobox_items(self):
		popup_xpath = "/*[@ClassName='" + __POPUP_TYPE__ + "']"
		item_xpath = popup_xpath + "/*[@ClassName='" + __ITEM_TYPE__ + "']"
		eles = self._get_elements(item_xpath)
		return eles

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
			raise AssertionError("ComboBox '{}' has Selection: '{}'. Expected: '{}'.".format(locator, actual, text))

	def select_value_on_combobox(self, locator, value):
		# Open the Combobox
		self._get_element_with_type(locator, __TYPE__).click()
		time.sleep(1)

		# Switch to Popup window
		popup_xpath = "//*[@ClassName='" + __POPUP_TYPE__ + "']"
		self.switch_to_new_window(popup_xpath, "Popup")

		try:
			self.click_element("name=" + value)
		except Exception:
			self._send_keys_on_element(Keys.END)
			self._send_keys_on_element(Keys.HOME)
			list_items = self.get_combobox_items()
			for item in list_items:
				if str(item.get_attribute("Name")).lower() == str(value).lower():
					item.click()
					break
