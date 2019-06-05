from AppiumLibrary.keywords.keywordgroup import KeywordGroup
import logging
import datetime

_APPLICATION_APPIUM_URL_KEY = "APPIUM_URL"
_APPLICATION_PATH_KEY = "PATH"


class ApplicationManagement(KeywordGroup):

	def __init__(self):
		self.appium_url = ""
		self.current_context = None
		self.desktop_context = None

	def setup_application(self, settings):
		"""
		Open application or attach the already-opened application
		:settings: dictionary of browser setting. Sample:
		APPLICATION:
		TYPE: wpf
		ALREADY_OPENED: No
		NAME: WpfTestApplication
		PATH: absolute/path/to/app.exe
		DEFAULT_USERNAME: admin
		DEFAULT_PASSWORD: password
		"""
		# Get setting value
		self.appium_url = settings.get(_APPLICATION_APPIUM_URL_KEY).strip().lower()
		application_path = settings.get(_APPLICATION_PATH_KEY, None)

		# init desktop session
		kwargs = {"platformName": "Windows", "deviceName": "tbd", "app": "Root"}
		index = self.open_application(self.appium_url, "Root", **kwargs)
		self.desktop_context = self._cache.get_connection(index)

		# Init application-under-test
		kwargs = {"platformName": "Windows", "deviceName": "tbd", "app": application_path}
		self.open_application(self.appium_url, "Main", **kwargs)
		self.current_context = self._cache.get_connection(index)

	def switch_to_new_window(self, new_window_locator, new_window_alias):
		self.switch_application("Root")
		new_window = self._element_find(new_window_locator, False, True)
		new_window_handle = new_window.get_attribute("NativeWindowHandle")
		hex_handle = hex(int(new_window_handle))
		kwargs = {"platformName": "Windows", "deviceName": "tbd", "appTopLevelWindow": hex_handle}
		self.open_application(self.appium_url, new_window_alias, **kwargs)


