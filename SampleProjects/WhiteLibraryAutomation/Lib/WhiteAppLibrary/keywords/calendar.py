import clr
clr.AddReference('UIAutomationClient')
clr.AddReference('UIAutomationTypes')
from System.Windows.Automation import *
from datetime import datetime
from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from System import DateTime
from TestStack.White.UIItems.TableItems import Table

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
        calendar = self._get_calendar(locator)
        calendar.Date = DateTime.Parse(date)

    @keyword
    def get_calendar_date(self, locator):
        calendar = self._get_calendar(locator)
        return calendar.Property(AutomationElement.ValueProperty)

    def _get_calendar(self, locator):
        return self.ctx.get_item_by_locator(locator)

