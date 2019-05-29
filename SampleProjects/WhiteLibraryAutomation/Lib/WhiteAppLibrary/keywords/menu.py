from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import MenuKeywords
from WhiteLibrary.utils.click import Clicks
from TestStack.White.UIItems.MenuItems import Menu

__version__ = '1.0.1'


class MenuManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.menu_management = MenuKeywords(ctx)

    @keyword
    def get_menu_name(self, locator):
        menu = self._get_menu(locator)
        return menu.Name

    @keyword
    def get_menu_help_text(self, locator):
        menu = self._get_menu(locator)
        return menu.HelpText

    @keyword
    def get_menu_access_key(self, locator):
        menu = self._get_menu(locator)
        return menu.AccessKey

    @keyword
    def get_menu_location(self, locator):
        menu = self._get_menu(locator)
        return menu.Location

    @keyword
    def get_menu_bound(self, locator):
        menu = self._get_menu(locator)
        return menu.Bounds

    @keyword
    def get_menu_image(self, locator):
        menu = self._get_menu(locator)
        return menu.VisibleImage

    @keyword
    def is_menu_enabled(self, locator):
        menu = self._get_menu(locator)
        return menu.Enabled

    @keyword
    def is_menu_visible(self, locator):
        menu = self._get_menu(locator)
        return menu.Visible

    @keyword
    def is_menu_focused(self, locator):
        menu = self._get_menu(locator)
        return menu.IsFocussed

    @keyword
    def focus_on_menu(self, locator):
        menu = self._get_menu(locator)
        if not menu.Enabled:
            raise AssertionError("Menu '{}' is not enabled to be focused.".format(locator))
        menu.Focus()

    @keyword
    def verify_menu_name(self, locator, expected):
        self.menu_management.verify_menu(locator, expected)

    @keyword
    def click_menu_button(self, locator, *text_path):
        self.menu_management.click_menu_button(locator, 0, 0)
        self.menu_management.click_item_in_popup_menu(*text_path)

    @keyword
    def get_popup_menu_name(self):
        popup_menu = self._get_popup_menu()
        return popup_menu.Name

    @keyword
    def get_popup_menu_help_text(self):
        popup_menu = self._get_popup_menu()
        return popup_menu.HelpText

    @keyword
    def get_popup_menu_access_key(self):
        popup_menu = self._get_popup_menu()
        return popup_menu.AccessKey

    @keyword
    def get_popup_menu_location(self):
        popup_menu = self._get_popup_menu()
        return popup_menu.Location

    @keyword
    def get_popup_menu_bound(self):
        popup_menu = self._get_popup_menu()
        return popup_menu.Bounds

    @keyword
    def get_popup_menu_image(self):
        popup_menu = self._get_popup_menu()
        return popup_menu.VisibleImage

    @keyword
    def is_popup_menu_visible(self):
        popup_menu = self._get_popup_menu()
        return popup_menu.Visible

    @keyword
    def click_item_in_popup_menu(self, *text_path):
        self.menu_management.click_item_in_popup_menu(*text_path)

    def _get_popup_menu(self):
        popup_menu = self.ctx.window.Popup
        if popup_menu is None:
            raise AssertionError("There is no Popup Menu")
        return popup_menu

    def _get_menu(self, locator):
        return self.ctx.get_typed_item_by_locator(Menu, locator)
