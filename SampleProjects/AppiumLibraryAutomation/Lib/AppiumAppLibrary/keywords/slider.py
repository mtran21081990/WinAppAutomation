from AppiumLibrary.keywords.keywordgroup import KeywordGroup
from selenium.webdriver.common.keys import Keys
import logging
import time

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
		if "." in expected:
			if float(expected) != float(actual):
				raise AssertionError("Slider '{}' has Value: '{}'. Expected: '{}'.".format(locator, float(actual), expected))
		else:
			if int(expected) != int(actual):
				raise AssertionError("Slider '{}' has Value: '{}'. Expected: '{}'.".format(locator, int(actual), expected))

	def click_on_slider(self, locator):
		try:
			self._get_element_with_type(locator, __TYPE__).click()
		except Exception as e:
			raise AssertionError("Cannot click on slider '{}'. Exception: {}".format(locator, e))

	def set_slider_value(self, locator, value):
		try:
			# Get Slider element
			slider = self._get_element_with_type(locator, __TYPE__)

			# Check type of Slider value
			is_float = False
			temp = slider.get_attribute("RangeValue.LargeChange")
			if temp == "0.1":
				temp = slider.get_attribute("RangeValue.SmallChange")
			if "." in temp:
				is_float = True

			logging.warning("HERE 1")

			# Verify whether Slider value is float or integer
			if is_float:
				max_value = float(slider.get_attribute("RangeValue.Maximum"))
				min_value = float(slider.get_attribute("RangeValue.Minimum"))
				cur_value = float(slider.get_attribute("RangeValue.Value"))
				inp_value = float(value)
				avg_value = float((max_value - min_value) / 2)
			else:
				max_value = int(slider.get_attribute("RangeValue.Maximum"))
				min_value = int(slider.get_attribute("RangeValue.Minimum"))
				cur_value = int(slider.get_attribute("RangeValue.Value"))
				inp_value = int(value)
				avg_value = int((max_value - min_value) / 2)

			logging.warning("HERE 2")

			# Return or raise exception if input value is not valid
			if not (min_value <= inp_value <= max_value):
				raise AssertionError("Input value exceeds Slider '{}' range [{},{}].".format(locator, min_value, max_value))
			if inp_value == cur_value:
				return

			logging.warning("HERE 3")

			# Click on Thump button of Slider
			thump_button = self._get_thump_button(locator)
			thump_button.click()

			logging.warning("HERE 4")

			if is_float:
				logging.warning("HERE 5.1")
				if cur_value < inp_value:
					while inp_value != float(self.get_slider_value(locator)):
						self._send_keys_on_element(Keys.UP)
						time.sleep(2)
				else:
					while inp_value != float(self.get_slider_value(locator)):
						self._send_keys_on_element(Keys.DOWN)
						time.sleep(2)
			else:
				logging.warning("HERE 5.2")
				if cur_value < inp_value:
					while inp_value != int(self.get_slider_value(locator)):
						self._send_keys_on_element(Keys.UP)
						time.sleep(2)
				else:
					while inp_value != int(self.get_slider_value(locator)):
						self._send_keys_on_element(Keys.DOWN)
						time.sleep(2)

		except Exception as e:
			raise e

	def _get_decrease_button(self, slider_locator):
		temp = "//*[@ClassName='" + __TYPE__ + "'][" + self._change_locator_to_xpath(slider_locator) + "]"
		temp = temp + "/*[@AutomationId='DecreaseLarge']"
		return self._get_element(temp)

	def _get_increase_button(self, slider_locator):
		temp = "//*[@ClassName='" + __TYPE__ + "'][" + self._change_locator_to_xpath(slider_locator) + "]"
		temp = temp + "/*[@AutomationId='IncreaseLarge']"
		return self._get_element(temp)

	def _get_thump_button(self, slider_locator):
		temp = "//*[@ClassName='" + __TYPE__ + "'][" + self._change_locator_to_xpath(slider_locator) + "]"
		temp = temp + "/*[@ClassName='Thumb']"
		return self._get_element(temp)
