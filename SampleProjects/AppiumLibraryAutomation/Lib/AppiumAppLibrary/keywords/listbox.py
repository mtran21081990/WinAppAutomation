from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "ListBox"


class ListboxManagement(KeywordGroup):

	def get_listbox_selection(self, locator):
		return self._get_element_with_type(locator, __TYPE__).text

	def get_listbox_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

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
		if not self.is_listbox_enabled:
			raise AssertionError("ListBox '{}' is not enabled".format(locator))

	def listbox_should_be_disabled(self, locator):
		if self.is_listbox_enabled:
			raise AssertionError("ListBox '{}' is not disabled".format(locator))

	def listbox_should_be_visible(self, locator):
		if not self.is_listbox_visible:
			raise AssertionError("ListBox '{}' is not visible".format(locator))

	def listbox_should_not_be_visible(self, locator):
		if self.is_listbox_visible:
			raise AssertionError("Listbox '{}' is not hidden".format(locator))

	def listbox_selection_should_equal_to(self, locator, text):
		actual = self.get_listbox_selection(locator)
		if str(text).lower() != actual.lower():
			raise AssertionError("ListBox '{}' has Selection: '{}'. Expected: '{}'.".format(locator, text, actual))

	def select_item_on_listbox(self, locator, item):
		try:
			self.element_click("name="+item)
		except Exception:
			raise AssertionError("Cannot select '{}' on Listbox '{}'.".format(item, locator))
