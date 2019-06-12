from AppiumLibrary.keywords.keywordgroup import KeywordGroup
import logging
import datetime

_APPLICATION_APPIUM_URL = "APPIUM_URL"
_APPLICATION_PATH = "PATH"
_APPLICATION_FIRST_PAGE_TITLE = "FIRST_PAGE_TITLE"


class ApplicationManagement(KeywordGroup):

	def __init__(self):
		self.appium_url = ""
		self.contexts = {}

	def setup_application(self, settings):
		"""
		Open application or attach the already-opened application
		APPIUM_URL: URL of Appium Desktop server
		PATH: Application directory path
		MAIN_PAGE_TITLE: Title of Main Page
		"""
		# Get setting value
		self.appium_url = settings.get(_APPLICATION_APPIUM_URL).strip().lower()
		application_path = settings.get(_APPLICATION_PATH, None)
		first_page_title = settings.get(_APPLICATION_FIRST_PAGE_TITLE, None)

		# init desktop session
		kwargs = {"platformName": "Windows", "deviceName": "tbd", "app": "Root"}
		self.contexts["Desktop"] = self.open_application(self.appium_url, None, **kwargs)

		# Init application-under-test
		kwargs = {"platformName": "Windows", "deviceName": "tbd", "app": application_path}
		self.contexts[first_page_title] = self.open_application(self.appium_url, None, **kwargs)

	def switch_window(self, window_locator, is_title=True):
		# If window_locator is title
		if is_title:
			# Switch to a newly opening Window
			if self.contexts.get(window_locator) is None:
				self.contexts[window_locator] = self._switch_window("name="+window_locator)
			# Switch to an existing window
			else:
				try:
					self.switch_application(self.contexts[window_locator])
				except ValueError:
					self.contexts[window_locator] = self._switch_window("name=" + window_locator)
		# If window_locator is a locator
		else:
			index = self._switch_window(window_locator)
			title = self.get_window_title(window_locator)
			self.contexts[title] = index

	def _switch_window(self, window_locator):
		self.switch_application(self.contexts["Desktop"])
		new_window = self._get_element(window_locator)
		new_window_handle = new_window.get_attribute("NativeWindowHandle")
		hex_handle = hex(int(new_window_handle))
		kwargs = {"platformName": "Windows", "deviceName": "tbd", "appTopLevelWindow": hex_handle}
		return self.open_application(self.appium_url, None, **kwargs)






