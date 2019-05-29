from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import TextBoxKeywords
from TestStack.White.UIItems import TextBox

__version__ = '1.0.1'


class TextBoxManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.textbox_management = TextBoxKeywords(ctx)

    @staticmethod
    def get_textbox_from_ui_item(ui_item):
        textbox = TextBox(ui_item.AutomationElement, None)
        return textbox

    @keyword
    def get_textbox_text(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.Text

    @keyword
    def get_textbox_name(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.Name

    @keyword
    def get_textbox_help_text(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.HelpText

    @keyword
    def get_textbox_access_key(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.AccessKey

    @keyword
    def get_textbox_location(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.Location

    @keyword
    def get_textbox_bound(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.Bounds

    @keyword
    def get_textbox_image(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.VisibleImage

    @keyword
    def is_textbox_enabled(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.Enabled

    @keyword
    def is_textbox_visible(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.Visible

    @keyword
    def is_textbox_focused(self, locator):
        textbox = self._get_textbox(locator)
        return textbox.IsFocussed

    @keyword
    def focus_on_textbox(self, locator):
        textbox = self._get_textbox(locator)
        if not textbox.Enabled:
            raise AssertionError("Textbox '{}' is not enabled to be focused.".format(locator))
        textbox.Focus()

    @keyword
    def input_text_to_textbox(self, locator, input_value):
        self.textbox_management.input_text_to_textbox(locator, input_value)

    @keyword
    def clear_textbox(self, locator):
        self.input_text_to_textbox(locator, "")

    @keyword
    def textbox_text_should_be(self, locator, expected_text, case_sensitive=True):
        self.textbox_management.verify_text_in_textbox(locator, expected_text, case_sensitive)

    @keyword
    def textbox_text_should_not_be(self, locator, expected_text):
        text = self.get_textbox_text(locator)
        if expected_text == text:
            raise AssertionError("Textbox '{}' Text should not be {}.".format(locator, text))

    @keyword
    def textbox_text_should_contain(self, locator, expected):
        text = self.get_textbox_text(locator)
        if expected not in text:
            raise AssertionError("Text '{}' is not in {}.".format(expected, text))

    @keyword
    def textbox_text_should_not_contain(self, locator, expected):
        text = self.get_textbox_text(locator)
        if expected in text:
            raise AssertionError("Text '{}' should not be in {}.".format(expected, text))

    def _get_textbox(self, locator):
        return self.ctx.get_typed_item_by_locator(TextBox, locator)
