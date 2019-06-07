from AppiumLibrary.keywords.keywordgroup import KeywordGroup
from selenium.webdriver.common.keys import Keys
import logging

__TYPE__ = "ListBox"
__ITEM_TYPE__ = "ListBoxItem"


class ListboxManagement(KeywordGroup):

	def get_listbox_selection(self, locator):
		return self._get_element_with_type(locator, __TYPE__).text

	def get_listbox_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def get_listbox_items(self, locator):
		x_locator = "//*[@ClassName='" + __TYPE__ + "'][" + self._change_locator_to_xpath(locator) + "]"
		locator_item = x_locator + "/*[@ClassName='" + __ITEM_TYPE__ + "']"
		eles = self._get_elements(locator_item)
		return eles

	def is_listbox_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_listbox_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def listbox_should_be_enabled(self, locator):
		if not self.is_listbox_enabled(locator):
			raise AssertionError("ListBox '{}' is not enabled".format(locator))

	def listbox_should_be_disabled(self, locator):
		if self.is_listbox_enabled(locator):
			raise AssertionError("ListBox '{}' is not disabled".format(locator))

	def listbox_should_be_visible(self, locator):
		if not self.is_listbox_visible(locator):
			raise AssertionError("ListBox '{}' is not visible".format(locator))

	def listbox_should_not_be_visible(self, locator):
		if self.is_listbox_visible(locator):
			raise AssertionError("Listbox '{}' is not hidden".format(locator))

	def listbox_selection_should_equal_to(self, locator, text):
		actual = self.get_listbox_selection(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("ListBox '{}' has Selection: '{}'. Expected: '{}'.".format(locator, actual, text))

	def select_item_on_listbox(self, locator, value):
		try:
			x_locator = "//*[@ClassName='"+__TYPE__+"']["+self._change_locator_to_xpath(locator)+"]"
			locator_item = x_locator + "/*[@ClassName='"+__ITEM_TYPE__+"'][@Name='"+value+"']"
			self.click_element(locator_item)
		except ValueError:
			self._loop_through_listbox_items(locator)
			list_items = self.get_listbox_items(locator)
			for item in list_items:
				if str(item.get_attribute("Name")).lower() == str(value).lower():
					item.click()
					break

	def _loop_through_listbox_items(self, locator):
		ele = self._get_element_with_type(locator, __TYPE__)
		self._double_click(ele)
		self._send_keys_on_element(Keys.END)
		self._send_keys_on_element(Keys.HOME)
