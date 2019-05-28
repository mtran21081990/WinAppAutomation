from ..base import LibraryComponent
from .element import ElementManagement
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import ButtonKeywords
from WhiteLibrary.utils.click import Clicks
from TestStack.White.UIItems import Button, CheckBox, RadioButton

__version__ = '1.0.1'


class ButtonManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.button_management = ButtonKeywords(ctx)
        self.element_manager = ElementManagement(ctx)

    @keyword
    def click_button(self, locator, x_offset=0, y_offset=0):
        self.button_management.click_button(locator, x_offset, y_offset)

    @keyword
    def right_click_button(self, locator, x_offset=0, y_offset=0):
        button = self._get_button(locator)
        Clicks.right_click(button, x_offset, y_offset)

    @keyword
    def double_click_button(self, locator, x_offset=0, y_offset=0):
        button = self._get_button(locator)
        Clicks.double_click(button, x_offset, y_offset)

    @keyword
    def button_text_should_be(self, locator, expected_text, case_sensitive=True):
        self.button_management.button_text_should_be(locator, expected_text, case_sensitive)

    @keyword
    def button_text_should_contain(self, locator, expected_text, case_sensitive=True):
        self.button_management.button_text_should_contain(locator, expected_text, case_sensitive)

    @keyword
    def select_radio_button(self, locator):
        self.button_management.select_radio_button(locator)

    @keyword
    def right_click_radio_button(self, locator, x_offset=0, y_offset=0):
        radio_button = self._get_radio_button(locator)
        Clicks.right_click(radio_button, x_offset, y_offset)

    @keyword
    def double_click_radio_button(self, locator, x_offset=0, y_offset=0):
        radio_button = self._get_radio_button(locator)
        Clicks.double_click(radio_button, x_offset, y_offset)

    @keyword
    def radio_button_text_should_be(self, locator, expected_text, case_sensitive=True):
        radio_button = self._get_radio_button(locator)
        self.ctx.verify_string_value(expected_text, radio_button.Text, case_sensitive)

    @keyword
    def radio_button_text_should_contain(self, locator, expected_text, case_sensitive=True):
        radio_button = self._get_radio_button(locator)
        self.ctx.contains_string_value(expected_text, radio_button.Text, case_sensitive)

    @keyword
    def verify_radio_button(self, locator, expected):
        self.button_management.verify_radio_button(locator, expected)

    @keyword
    def get_radio_button_state(self, locator):
        return self.button_management.get_radio_button_state(locator)

    @keyword
    def toggle_check_box(self, locator):
        self.button_management.toggle_check_box(locator)

    @keyword
    def right_click_check_box(self, locator, x_offset=0, y_offset=0):
        check_box = self._get_check_box(locator)
        Clicks.right_click(check_box, x_offset, y_offset)

    @keyword
    def double_click_check_box(self, locator, x_offset=0, y_offset=0):
        check_box = self._get_check_box(locator)
        Clicks.double_click(check_box, x_offset, y_offset)

    @keyword
    def check_box_text_should_be(self, locator, expected_text, case_sensitive=True):
        check_box = self._get_check_box(locator)
        self.ctx.verify_string_value(expected_text, check_box.Text, case_sensitive)

    @keyword
    def check_box_text_should_contain(self, locator, expected_text, case_sensitive=True):
        check_box = self._get_check_box(locator)
        self.ctx.contains_string_value(expected_text, check_box.Text, case_sensitive)

    @keyword
    def verify_check_box(self, locator, expected):
        self.button_management.verify_check_box(locator, expected)

    @keyword
    def get_check_box_state(self, locator):
        return self.button_management.get_check_box_state(locator)

    @keyword
    def check_box_is_checked(self, locator):
        state = self.get_check_box_state(locator)
        if not state:
            raise AssertionError("Check box {} is not checked as expected".format(locator))

    @keyword
    def check_box_is_uncheck(self, locator):
        state = self.get_check_box_state(locator)
        if state:
            raise AssertionError("Check box {} is not uncheck as expected".format(locator))

    @keyword
    def toggle_button(self, locator):
        button = self._get_toggle_button(locator)
        button.Toggle()

    @keyword
    def verify_toggle_button(self, locator, expected):
        button = self._get_toggle_button(locator)
        if button.State != expected:
            raise AssertionError("Toggle Button {} State is {}, not as expected {}.".format(locator,button.State, expected))

    @keyword
    def toggle_button_is_on(self, locator):
        button = self._get_toggle_button(locator)
        if button.State != 1:
            raise AssertionError("Toggle Button {} is not ON as expected".format(locator))

    @keyword
    def toggle_button_is_off(self, locator):
        button = self._get_toggle_button(locator)
        if button.State != 0:
            raise AssertionError("Toggle Button {} is not OFF as expected".format(locator))

    @keyword
    def get_toggle_button_state(self, locator):
        button = self._get_toggle_button(locator)
        return button.State

    def _get_check_box(self, locator):
        return self._get_button(locator, CheckBox)

    def _get_radio_button(self, locator):
        return self._get_button(locator, RadioButton)

    def _get_toggle_button(self, locator):
        return self._get_button(locator)

    def _get_button(self, locator, button_type=Button):
        return self.ctx.get_typed_item_by_locator(button_type, locator)
