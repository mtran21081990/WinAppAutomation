from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems import DateTimePicker
from System import DateTime

__version__ = '1.0.1'


class DateTimePickerManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)

    @keyword
    def get_datetime_picker_name(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.Name

    @keyword
    def get_datetime_picker_help_text(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.HelpText

    @keyword
    def get_datetime_picker_access_key(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.AccessKey

    @keyword
    def get_datetime_picker_location(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.Location

    @keyword
    def get_datetime_picker_bound(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.Bounds

    @keyword
    def get_datetime_picker_image(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.VisibleImage

    @keyword
    def get_datetime_picker_selection(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.Date

    @keyword
    def is_datetime_picker_enabled(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.Enabled

    @keyword
    def is_datetime_picker_visible(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.Visible

    @keyword
    def is_datetime_picker_focused(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.IsFocussed

    @keyword
    def focus_on_datetime_picker(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        if not datetime_picker.Enabled:
            raise AssertionError("Tree '{}' is not enabled to be focused.".format(locator))
        datetime_picker.Focus()

    @keyword
    def set_datetime_picker(self, locator, date):
        datetime_picker = self._get_datetime_picker(locator)
        datetime_picker.Date = DateTime.Parse(date)

    @keyword
    def get_datetime_picker_date(self, locator):
        datetime_picker = self._get_datetime_picker(locator)
        return datetime_picker.Date

    def _get_datetime_picker(self, locator):
        return self.ctx.get_typed_item_by_locator(DateTimePicker, locator)

