from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import UiItemKeywords

__version__ = '1.0.1'


class ElementManagementKeywords(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.element_management = UiItemKeywords(ctx)

    @keyword
    def click_item_on_application(self, locator):
        self.element_management.click_item(locator)

    @keyword
    def element_should_be_visible(self, locator):
        item = self.element_management.get_item(locator)
        if item is None:
            return False
        return True
