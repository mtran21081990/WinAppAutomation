from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import LabelKeywords
from WhiteLibrary.utils.click import Clicks
from WhiteLibrary.utils.click import Clicks
from TestStack.White.UIItems import Label

__version__ = '1.0.1'


class LabelManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.label_management = LabelKeywords(ctx)

    @keyword
    def get_label_text(self, locator):
        return self.label_management.get_text_from_label(locator)

    @keyword
    def get_label_location(self, locator):
        label = self._get_label(locator)
        return label.Location

    @keyword
    def get_label_bound(self, locator):
        label = self._get_label(locator)
        return label.Bounds

    @keyword
    def get_label_image(self, locator):
        label = self._get_label(locator)
        return label.VisibleImage

    @keyword
    def is_label_enabled(self, locator):
        label = self._get_label(locator)
        return label.Enabled

    @keyword
    def is_label_visible(self, locator):
        label = self._get_label(locator)
        return label.Visible

    @keyword
    def click_label(self, locator):
        Clicks.click(locator, 1, 1)

    @keyword
    def right_click_label(self, locator):
        label = self._get_label(locator)
        Clicks.right_click(label, 1, 1)

    @keyword
    def double_click_label(self, locator):
        label = self._get_label(locator)
        Clicks.double_click(label, 1, 1)

    @keyword
    def label_text_should_be(self, locator, expected):
        self.label_management.verify_label(locator, expected)

    @keyword
    def label_text_should_contain(self, locator, expected_text, case_sensitive=True):
        label = self._get_label(locator)
        self.ctx.contains_string_value(expected_text, label.Text, case_sensitive)

    def _get_label(self, locator):
        return self.ctx.get_typed_item_by_locator(Label, locator)
