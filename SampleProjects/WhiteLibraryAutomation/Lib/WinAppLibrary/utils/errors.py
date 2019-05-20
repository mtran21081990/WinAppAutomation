class WinAppLibraryException(Exception):
    ROBOT_SUPPRESS_NAME = True


class ElementNotFound(WinAppLibraryException):
    pass


class WindowNotFound(WinAppLibraryException):
    pass


class CookieNotFound(WinAppLibraryException):
    pass


class NoOpenApplication(WinAppLibraryException):
    pass
