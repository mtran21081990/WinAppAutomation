from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__TYPE__ = "Slider"


class SliderManagement(KeywordGroup):

	def get_slider_helptext(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "HelpText")

	def get_slider_maximum_value(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "RangeValue.Maximum")

	def get_slider_minimum_value(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "RangeValue.Minimum")

	def get_slider_large_change(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "RangeValue.LargeChange")

	def get_slider_small_change(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "RangeValue.SmallChange")

	def get_slider_value(self, locator):
		return self._get_element_attribute(locator, __TYPE__, "RangeValue.Value")

	def is_slider_enabled(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsEnabled")
		if str(is_enabled).lower() != "true":
			return False
		return True

	def is_slider_visible(self, locator):
		is_enabled = self._get_element_attribute(locator, __TYPE__, "IsOffscreen")
		if str(is_enabled).lower() != "false":
			return False
		return True

	def slider_should_be_enabled(self, locator):
		if not self.is_slider_enabled:
			raise AssertionError("Slider '{}' is not enabled".format(locator))

	def slider_should_be_disabled(self, locator):
		if self.is_slider_enabled:
			raise AssertionError("Slider '{}' is not disabled".format(locator))

	def slider_should_be_visible(self, locator):
		if not self.is_slider_visible:
			raise AssertionError("Slider '{}' is not visible".format(locator))

	def slider_should_not_be_visible(self, locator):
		if self.is_slider_visible:
			raise AssertionError("Slider '{}' is not hidden".format(locator))

	def slider_value_should_equal_to(self, locator, expected):
		actual = self.get_slider_value(locator)
		if str(expected).lower() != actual.lower():
			raise AssertionError("Slider '{}' has Value: '{}'. Expected: '{}'.".format(locator, actual, expected))

	def click_on_slider(self, locator):
		try:
			self._get_element_with_type(locator, __TYPE__).click()
		except Exception as e:
			raise AssertionError("Cannot click on slider '{}'. Exception: {}".format(locator, e))

	def set_slider_value(self, locator, value):
		slider = self._get_element_with_type(locator, __TYPE__)
		max_value = slider.get_attribute("RangeValue.Maximum")
		min_value = slider.get_attribute("RangeValue.Minimum")
		if not (min_value <= value <= max_value):
			raise AssertionError("Input value exceeds Slider '{}' range [{},{}].".format(locator, min_value, max_value))
