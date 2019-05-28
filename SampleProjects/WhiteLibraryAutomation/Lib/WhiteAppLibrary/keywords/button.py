from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import ButtonKeywords
from WhiteLibrary.utils.click import Clicks
from TestStack.White.UIItems import Button, CheckBox, RadioButton

__version__ = '1.0.1'


class ButtonManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.button_management = ButtonKeywords(ctx)

    @keyword
    def get_button_text(self, locator):
        button = self._get_button(locator)
        return button.Text

    @keyword
    def get_button_name(self, locator):
        button = self._get_button(locator)
        return button.Name

    @keyword
    def get_button_help_text(self, locator):
        button = self._get_button(locator)
        return button.HelpText

    @keyword
    def get_button_access_key(self, locator):
        button = self._get_button(locator)
        return button.AccessKey

    @keyword
    def get_button_location(self, locator):
        button = self._get_button(locator)
        return button.Location

    @keyword
    def get_button_bound(self, locator):
        button = self._get_button(locator)
        return button.Bounds

    @keyword
    def get_button_image(self, locator):
        button = self._get_button(locator)
        return button.VisibleImage

    @keyword
    def is_button_enabled(self, locator):
        button = self._get_button(locator)
        return button.Enabled

    @keyword
    def is_button_visible(self, locator):
        button = self._get_button(locator)
        return button.Visible

    @keyword
    def is_button_focused(self, locator):
        button = self._get_button(locator)
        return button.IsFocussed

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
    def get_radio_button_text(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.Text

    @keyword
    def get_radio_button_name(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.Name

    @keyword
    def get_radio_button_help_text(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.HelpText

    @keyword
    def get_radio_button_access_key(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.AccessKey

    @keyword
    def get_radio_button_location(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.Location

    @keyword
    def get_radio_button_bound(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.Bounds

    @keyword
    def get_radio_button_image(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.VisibleImage

    @keyword
    def is_radio_button_enabled(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.Enabled

    @keyword
    def is_radio_button_visible(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.Visible

    @keyword
    def is_radio_button_focused(self, locator):
        radio_button = self._get_radio_button(locator)
        return radio_button.IsFocussed

    @keyword
    def select_radio_button(self, locator):
        self.button_management.select_radio_button(locator)

    @keyword
    def click_radio_button_text(self, locator):
        radio_button = self._get_radio_button(locator)
        child_text_element = self.ctx.element_manager.get_child_ui_item(radio_button, "class_name=TextBlock")
        Clicks.click(child_text_element, 1, 1)

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
    def radio_button_should_be_selected(self, locator):
        state = self.get_radio_button_state(locator)
        if not state:
            raise AssertionError("Radio button {} is not selected as expected".format(locator))

    @keyword
    def radio_button_should_be_unselect(self, locator):
        state = self.get_radio_button_state(locator)
        if state:
            raise AssertionError("Check box {} is not unselect as expected".format(locator))

    @keyword
    def get_check_box_text(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.Text

    @keyword
    def get_check_box_name(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.Name

    @keyword
    def get_check_box_help_text(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.HelpText

    @keyword
    def get_check_box_access_key(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.AccessKey

    @keyword
    def get_check_box_location(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.Location

    @keyword
    def get_check_box_bound(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.Bounds

    @keyword
    def get_check_box_image(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.VisibleImage

    @keyword
    def is_check_box_enabled(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.Enabled

    @keyword
    def is_check_box_visible(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.Visible

    @keyword
    def is_check_box_focused(self, locator):
        check_box = self._get_check_box(locator)
        return check_box.IsFocussed

    @keyword
    def toggle_check_box(self, locator):
        self.button_management.toggle_check_box(locator)

    @keyword
    def click_check_box_text(self, locator):
        check_box = self._get_check_box(locator)
        child_text_element = self.ctx.element_manager.get_child_ui_item(check_box, "class_name=TextBlock")
        Clicks.click(child_text_element, 1, 1)

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
    def check_box_should_be_checked(self, locator):
        state = self.get_check_box_state(locator)
        if not state:
            raise AssertionError("Check box {} is not checked as expected".format(locator))

    @keyword
    def check_box_should_be_uncheck(self, locator):
        state = self.get_check_box_state(locator)
        if state:
            raise AssertionError("Check box {} is not uncheck as expected".format(locator))

    @keyword
    def get_toggle_button_text(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.Text

    @keyword
    def get_toggle_button_name(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.Name

    @keyword
    def get_toggle_button_help_text(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.HelpText

    @keyword
    def get_toggle_button_access_key(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.AccessKey

    @keyword
    def get_toggle_button_location(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.Location

    @keyword
    def get_toggle_button_bound(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.Bounds

    @keyword
    def get_toggle_button_image(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.VisibleImage

    @keyword
    def is_toggle_button_enabled(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.Enabled

    @keyword
    def is_toggle_button_visible(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.Visible

    @keyword
    def is_toggle_button_focused(self, locator):
        toggle_button = self._get_toggle_button(locator)
        return toggle_button.IsFocussed

    @keyword
    def toggle_button(self, locator):
        button = self._get_toggle_button(locator)
        button.Toggle()

    @keyword
    def verify_toggle_button(self, locator, expected):
        toggle_button = self._get_toggle_button(locator)
        if toggle_button.State != expected:
            raise AssertionError("Toggle Button {} State is {}, not as expected {}.".format(locator,button.State, expected))

    @keyword
    def toggle_button_should_be_on(self, locator):
        toggle_button = self._get_toggle_button(locator)
        if toggle_button.State != 1:
            toggle_button.Capture()
            raise AssertionError("Toggle Button {} is not ON as expected".format(locator))

    @keyword
    def toggle_button_should_be_off(self, locator):
        toggle_button = self._get_toggle_button(locator)
        if toggle_button.State != 0:
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
