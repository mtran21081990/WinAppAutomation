from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "TabControl"
__ITEM_TYPE__ = "TabItem"


class TabManagement(KeywordGroup):

	def get_tab_control_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def get_tab_control_selection_item(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "Selection.Selection")

	def is_tab_control_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_tab_control_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def tab_control_should_be_enabled(self, locator):
		if not self.is_tab_enabled(locator):
			raise AssertionError("Tab Control '{}' is not enabled".format(locator))

	def tab_control_should_be_disabled(self, locator):
		if self.is_tab_enabled(locator):
			raise AssertionError("Tab Control '{}' is not disabled".format(locator))

	def tab_control_should_be_visible(self, locator):
		if not self.is_tab_visible(locator):
			raise AssertionError("Tab Control '{}' is not visible".format(locator))

	def tab_control_should_not_be_visible(self, locator):
		if self.is_tab_visible(locator):
			raise AssertionError("Tab Control '{}' is not hidden".format(locator))

	def get_tab_name(self, tab_name):
		return self._get_element_attribute("name="+tab_name, __ITEM_TYPE__, "Name")

	def get_tab_helptext(self, tab_name):
		return self._get_element_attribute("name="+tab_name, __ITEM_TYPE__, "HelpText")

	def get_tab_selection_state(self, tab_name):
		return self._get_element_attribute("name="+tab_name, __ITEM_TYPE__, "SelectionItem.IsSelected")

	def is_tab_enabled(self, tab_name):
		is_enabled = self._get_element_attribute("name="+tab_name, __ITEM_TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_tab_visible(self, tab_name):
		is_enabled = self._get_element_attribute("name="+tab_name, __ITEM_TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def tab_should_be_enabled(self, tab_name):
		if not self.is_tab_enabled(tab_name):
			raise AssertionError("Tab '{}' is not enabled".format(tab_name))

	def tab_should_be_disabled(self, tab_name):
		if self.is_tab_enabled(tab_name):
			raise AssertionError("Tab '{}' is not disabled".format(tab_name))

	def tab_should_be_visible(self, tab_name):
		if not self.is_tab_visible(tab_name):
			raise AssertionError("Tab '{}' is not visible".format(tab_name))

	def tab_should_not_be_visible(self, tab_name):
		if self.is_tab_visible(tab_name):
			raise AssertionError("Tab '{}' is not hidden".format(tab_name))

	def tab_name_should_equal_to(self, tab_name, text):
		actual = self.get_tab_name(tab_name)
		if str(text).lower() != actual.lower():
			raise AssertionError("Tab '{}' has Text: '{}'. Expected: '{}'.".format(tab_name, actual, text))

	def tab_should_be_selected(self, tab_name):
		state = self.get_tab_selection_state(tab_name)
		if int(state) != 1:
			raise AssertionError("Tab '{}' is not selected. Selection State value: '{}'.".format(tab_name, state))

	def tab_should_not_be_selected(self, tab_name):
		state = self.get_tab_selection_state(tab_name)
		if int(state) == 1:
			raise AssertionError("Tab '{}' should not be selected. Selection State value: '{}'.".format(tab_name, state))

	def click_on_tab(self, tab_name):
		try:
			self._get_element_with_type("name="+tab_name, __ITEM_TYPE__).click()
		except Exception as e:
			raise AssertionError("Cannot click on Tab '{}'. Exception: {}".format(tab_name, e))

	def double_click_tab(self, tab_name):
		try:
			ele = self._get_element_with_type("name="+tab_name, __ITEM_TYPE__)
			self._double_click(ele)
		except Exception as e:
			raise AssertionError("Cannot double click on Tab '{}'. Exception: {}".format(tab_name, e))

	def right_click_tab(self, tab_name):
		try:
			ele = self._get_element_with_type("name="+tab_name, __ITEM_TYPE__)
			self._right_click(ele)
		except Exception as e:
			raise AssertionError("Cannot right click on Tab '{}'. Exception: {}".format(tab_name, e))
