from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from System import DateTime
from datetime import datetime

__version__ = '1.0.1'


class CalendarManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)

    @keyword
    def get_calendar_name(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.Name

    @keyword
    def get_calendar_help_text(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.HelpText

    @keyword
    def get_calendar_access_key(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.AccessKey

    @keyword
    def get_calendar_location(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.Location

    @keyword
    def get_calendar_bound(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.Bounds

    @keyword
    def get_calendar_image(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.VisibleImage

    @keyword
    def get_calendar_selection(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.Date

    @keyword
    def is_calendar_enabled(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.Enabled

    @keyword
    def is_calendar_visible(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.Visible

    @keyword
    def is_calendar_focused(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.IsFocussed

    @keyword
    def focus_on_calendar(self, locator):
        calendar = self._get_calendar(locator)
        if not calendar.Enabled:
            raise AssertionError("Calendar '{}' is not enabled to be focused.".format(locator))
        calendar.Focus()

    @keyword
    def set_calendar(self, locator, date):
        """TODO"""

    @keyword
    def get_calendar_date(self, locator):
        """TODO"""

    def _get_calendar(self, locator):
        return self.ctx.element_manager.get_ui_item_from_tree_walker(locator)
