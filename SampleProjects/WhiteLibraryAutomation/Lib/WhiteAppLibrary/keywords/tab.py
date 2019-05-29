from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import TabKeywords
from TestStack.White.UIItems.TabItems import Tab

__version__ = '1.0.1'


class TabManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.tab_management = TabKeywords(ctx)

    @keyword
    def get_tab_name(self, locator):
        tab = self._get_tab(locator)
        return tab.Name

    @keyword
    def get_tab_help_text(self, locator):
        tab = self._get_tab(locator)
        return tab.HelpText

    @keyword
    def get_tab_access_key(self, locator):
        tab = self._get_tab(locator)
        return tab.AccessKey

    @keyword
    def get_tab_location(self, locator):
        tab = self._get_tab(locator)
        return tab.Location

    @keyword
    def get_tab_bound(self, locator):
        tab = self._get_tab(locator)
        return tab.Bounds

    @keyword
    def get_tab_image(self, locator):
        tab = self._get_tab(locator)
        return tab.VisibleImage

    @keyword
    def is_tab_enabled(self, locator):
        tab = self._get_tab(locator)
        return tab.Enabled

    @keyword
    def is_tab_visible(self, locator):
        tab = self._get_tab(locator)
        return tab.Visible

    @keyword
    def is_tab_focused(self, locator):
        tab = self._get_tab(locator)
        return tab.IsFocussed

    @keyword
    def focus_on_tab(self, locator):
        tab = self._get_tab(locator)
        if not tab.Enabled:
            raise AssertionError("Tab '{}' is not enabled to be focused.".format(locator))
        tab.Focus()

    @keyword
    def focus_on_tab_page(self, locator, title):
        tab = self._get_tab(locator)
        if not tab.Enabled:
            raise AssertionError("Tab '{}' is not enabled to be focused.".format(locator))
        tab_pages = tab.Pages
        is_found = False
        for page in tab_pages:
            if page.Name == title:
                is_found = True
                if not page.Enabled:
                    raise AssertionError("Tab Page '{}' is not enabled to be focused.".format(title))
                page.Focus()
        if not is_found:
            raise AssertionError("Cannot find Tab Page '{}' in Tab {}".format(title, locator))

    @keyword
    def select_tab_page_by_title(self, locator, title):
        self.tab_management.select_tab_page(locator, title)

    @keyword
    def select_tab_page_by_index(self, locator, index):
        self.tab_management.select_tab_page_by_index(locator, index)

    @keyword
    def get_tab_pages(self, locator):
        return self.tab_management.get_tab_pages(locator)

    @keyword
    def selected_tab_page_should_be(self, locator, title):
        tab = self._get_tab(locator)
        selected_tab_page = tab.SelectedTab
        if selected_tab_page.Name != title:
            raise AssertionError("Selected Tab Page is '{}', not {}.".format(selected_tab_page.Name, title))

    @keyword
    def selected_tab_page_should_not_be(self, locator, title):
        tab = self._get_tab(locator)
        selected_tab_page = tab.SelectedTab
        if selected_tab_page.Name == title:
            raise AssertionError("Selected Tab Page should not be {}.".format(title))

    def _get_tab(self, locator):
        return self.ctx.get_typed_item_by_locator(Tab, locator)
