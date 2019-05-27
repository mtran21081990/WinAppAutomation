from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import UiItemKeywords

__version__ = '1.0.1'


class ElementManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.element_management = UiItemKeywords(ctx)

    @keyword
    def click_item_on_application(self, locator):
        self.element_management.click_item(locator)

    @keyword
    def element_should_be_visible(self, locator):
        item = self.element_management.get_item(locator)
        if not item.Visible:
            return False
        return True

    @keyword
    def element_should_not_be_visible(self, locator):
        item = self.element_management.get_item(locator)
        if item.Visible:
            return True
        return False
