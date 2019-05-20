from ..base import keyword, LibraryComponent
from WhiteLibrary.keywords import WindowKeywords

__version__ = '1.0.1'
_APPLICATION_MAIN_WINDOW_NAME_KEY = "MAIN_WINDOW_NAME"


class WindowManagementKeywords(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.window_management = WindowKeywords(ctx)

    @keyword
    def attach_main_window(self, settings):
        main_window_name = settings.get(_APPLICATION_MAIN_WINDOW_NAME_KEY, None)
        self.window_management.attach_window(main_window_name)

    @keyword
    def get_window_full_title(self):
        title = self.window_management.get_window_title()
        if title is not None or title != '':
            return title

        title = self.window_management.state.window.Name
        if title is not None or title != '':
            return title

        return ""

    @keyword
    def window_title_should_equal_to(self, title):
        full_title = self.get_window_full_title()
        if full_title == title:
            return True
        return False