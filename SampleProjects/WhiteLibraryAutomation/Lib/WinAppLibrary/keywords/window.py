from ..base import LibraryComponent
import logging
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords import WindowKeywords
from TestStack.White.UIItems.Finders import SearchCriteria
from System.Windows.Automation import AutomationElement, PropertyCondition, TreeScope, Condition

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
        """try:
            item = self.window_management.state.window.Get(SearchCriteria.ByText("Item1"))
            logging.info("Using UIItem. Item with text = Item1: ")
            logging.info(item)
            logging.info("Using UIItem. Bound of Item1: ")
            logging.info(item.Bounds)
        except Exception:
            logging.debug("Using UIItem. Exception on getting Item1")
        try:
            itemTemp = self.window_management.state.window.AutomationElement.FindAll(TreeScope.Subtree, PropertyCondition(
                AutomationElement.NameProperty, "Item1"))
            item = itemTemp[0]
            logging.info("Using AutomationItem. Item with text = Item1: ")
            logging.info(item)
            logging.info("Using AutomationItem. Bound of Item1: ")
            logging.info(item.BoundingRectangleProperty)
        except Exception:
            logging.debug("Using AutomationItem. Exception on getting Item1")
        """
        try:
            items = self.window_management.state.window.AutomationElement.FindAll(TreeScope.Descendants, Condition.TrueCondition)
            #logging.info("List of Items: ")
            #logging.info(items)
            logging.info("Total Items: " + str(items.Count))
            logging.info("Name of every Items: ")
            for itm in items:
                logging.info(str(itm.Current.Name))
        except Exception:
            logging.debug("Exception on getting list of items")

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
