from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import UiItemKeywords
from System.Windows.Automation import TreeWalker
from TestStack.White.UIItems import UIItem

__version__ = '1.0.1'


class ElementManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.element_management = UiItemKeywords(ctx)

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

    @keyword
    def click_item(self, locator, x_offset=0, y_offset=0):
        self.element_management.click_item(locator, x_offset, y_offset)

    @keyword
    def right_click_item(self, locator, x_offset=0, y_offset=0):
        self.element_management.right_click_item(locator, x_offset, y_offset)

    @keyword
    def double_click_item(self, locator, x_offset=0, y_offset=0):
        self.element_management.double_click_item(locator, x_offset, y_offset)

    @keyword
    def get_items(self, locator):
        return self.element_management.get_items(locator)

    @keyword
    def get_item(self, locator):
        return self.element_management.get_item(locator)

    @keyword
    def item_should_be_enabled(self, locator):
        self.element_management.item_should_be_enabled(locator)

    @keyword
    def item_should_be_disabled(self, locator):
        self.element_management.item_should_be_disabled(locator)

    def get_child_ui_item(self, ui_item, child_locator):
        criteria = self.ctx.get_search_criteria(child_locator)
        child_automation_element = ui_item.GetElement(criteria)
        child_ui_element = UIItem(child_automation_element, None)
        return child_ui_element

    def get_ui_item_from_tree_walker(self, locator, next_or_first="next"):
        ele = self.ctx.get_item_by_locator(locator)
        if next_or_first == "next":
            ele_auto = TreeWalker.RawViewWalker.GetNextSibling(ele.AutomationElement)
        else:
            ele_auto = TreeWalker.RawViewWalker.GetFirstChild(ele.AutomationElement)
        return UIItem(ele_auto, None)

