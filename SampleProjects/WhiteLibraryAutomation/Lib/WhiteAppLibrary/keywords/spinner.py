from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems import Spinner

__version__ = '1.0.1'


class SpinnerManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)

    @keyword
    def get_spinner_name(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.Name

    @keyword
    def get_spinner_help_text(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.HelpText

    @keyword
    def get_spinner_access_key(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.AccessKey

    @keyword
    def get_spinner_location(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.Location

    @keyword
    def get_spinner_bound(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.Bounds

    @keyword
    def get_spinner_image(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.VisibleImage

    @keyword
    def get_spinner_value(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.Value

    @keyword
    def increase_spinner_value(self, locator):
        spinner = self._get_spinner(locator)
        spinner.Increment()

    @keyword
    def decrease_spinner_value(self, locator):
        spinner = self._get_spinner(locator)
        spinner.Decrement()

    @keyword
    def is_spinner_enabled(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.Enabled

    @keyword
    def is_spinner_visible(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.Visible

    @keyword
    def is_spinner_focused(self, locator):
        spinner = self._get_spinner(locator)
        return spinner.IsFocussed

    @keyword
    def focus_on_spinner(self, locator):
        spinner = self._get_spinner(locator)
        if not spinner.Enabled:
            raise AssertionError("Spinner '{}' is not enabled to be focused.".format(locator))
        spinner.Focus()

    @keyword
    def set_spinner_value(self, locator, value):
        spinner = self._get_spinner(locator)
        spinner.Value = value

    @keyword
    def verify_spinner_value(self, locator, expected, case_sensitive=True):
        spinner = self._get_spinner(locator)
        self.ctx.verify_string_value(expected, spinner.Value, case_sensitive)

    def _get_spinner(self, locator):
        return self.ctx.get_typed_item_by_locator(Spinner, locator)
