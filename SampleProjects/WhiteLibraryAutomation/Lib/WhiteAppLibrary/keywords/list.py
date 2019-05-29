from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import ListViewKeywords, ListKeywords
from WhiteLibrary.utils.click import Clicks
from TestStack.White.UIItems import ListView
from TestStack.White.UIItems.ListBoxItems import ComboBox, ListBox

__version__ = '1.0.1'


class ListManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.listview_management = ListViewKeywords(ctx)
        self.list_management = ListKeywords(ctx)

    @keyword
    def double_click_listview_cell(self, locator, column_name, row_index, x_offset=0, y_offset=0):
        self.listview_management.double_click_listview_cell(locator, column_name, row_index, x_offset, y_offset)

    @keyword
    def right_click_listview_cell(self, locator, column_name, row_index, x_offset=0, y_offset=0):
        self.listview_management.right_click_listview_cell(locator, column_name, row_index, x_offset, y_offset)

    @keyword
    def double_click_listview_cell_by_index(self, locator, row_index, column_index, x_offset=0, y_offset=0):
        self.listview_management.double_click_listview_cell_by_index(locator, row_index, column_index, x_offset,
                                                                     y_offset)

    @keyword
    def right_click_listview_cell_by_index(self, locator, row_index, column_index, x_offset=0, y_offset=0):
        self.listview_management.right_click_listview_cell_by_index(locator, row_index, column_index, x_offset,
                                                                    y_offset)

    @keyword
    def double_click_listview_row_by_cell_text(self, locator, column_name, cell_text, x_offset=0, y_offset=0):
        self.listview_management.double_click_listview_row(locator, column_name, cell_text, x_offset, y_offset)

    @keyword
    def right_click_listview_row_by_cell_text(self, locator, column_name, cell_text, x_offset=0, y_offset=0):
        self.listview_management.right_click_listview_row(locator, column_name, cell_text, x_offset, y_offset)

    @keyword
    def double_click_listview_row_by_row_index(self, locator, row_index, x_offset=0, y_offset=0):
        self.listview_management.double_click_listview_row_by_index(locator, row_index, x_offset, y_offset)

    @keyword
    def right_click_listview_row_by_row_index(self, locator, row_index, x_offset=0, y_offset=0):
        self.listview_management.right_click_listview_row_by_index(locator, row_index, x_offset, y_offset)

    @keyword
    def get_listview_cell_text_by_column_name(self, locator, row_index, column_name):
        return self.listview_management.get_listview_cell_text(locator, column_name, row_index)

    @keyword
    def get_listview_cell_text_by_column_index(self, locator, row_index, column_index):
        return self.listview_management.get_listview_cell_text_by_index(locator, row_index, column_index)

    @keyword
    def get_listview_row_text_by_cell_text(self, locator, column_name, cell_text):
        return self.listview_management.get_listview_row_text(locator, column_name, cell_text)

    @keyword
    def get_listview_row_text_by_row_index(self, locator, row_index):
        return self.listview_management.get_listview_row_text_by_index(locator, row_index)

    @keyword
    def listview_cell_at_column_index_should_contain(self, locator, row_index, column_index, expected):
        self.listview_management.listview_cell_at_index_should_contain(locator, row_index, column_index, expected)

    @keyword
    def listview_cell_at_column_index_should_not_contain(self, locator, row_index, column_index, expected):
        self.listview_management.listview_cell_at_index_should_not_contain(locator, row_index, column_index, expected)

    @keyword
    def listview_cell_at_column_name_should_contain(self, locator, row_index, column_name, expected):
        self.listview_management.listview_cell_should_contain(locator, column_name, row_index, expected)

    @keyword
    def listview_cell_at_column_name_should_not_contain(self, locator, row_index, column_name, expected):
        self.listview_management.listview_cell_should_not_contain(locator, column_name, row_index, expected)

    @keyword
    def listview_cell_at_column_index_should_be(self, locator, row_index, column_index, expected):
        self.listview_management.listview_cell_text_at_index_should_be(locator, row_index, column_index, expected)

    @keyword
    def listview_cell_at_column_index_should_not_be(self, locator, row_index, column_index, expected):
        self.listview_management.listview_cell_text_at_index_should_not_be(locator, row_index, column_index, expected)

    @keyword
    def listview_cell_at_column_name_should_be(self, locator, row_index, column_name, expected):
        self.listview_management.listview_cell_text_should_be(locator, column_name, row_index, expected)

    @keyword
    def listview_cell_at_column_name_should_not_be(self, locator, row_index, column_name, expected):
        self.listview_management.listview_cell_text_should_not_be(locator, column_name, row_index, expected)

    @keyword
    def listview_row_at_index_should_contain(self, locator, row_index, expected):
        self.listview_management.listview_row_at_index_should_contain(locator, row_index, expected)

    @keyword
    def listview_row_at_index_should_not_contain(self, locator, row_index, expected):
        self.listview_management.listview_row_at_index_should_not_contain(locator, row_index, expected)

    @keyword
    def listview_row_should_contain(self, locator, column_name, cell_text, expected):
        self.listview_management.listview_row_should_contain(locator, column_name, cell_text, expected)

    @keyword
    def listview_row_should_not_contain(self, locator, column_name, cell_text, expected):
        self.listview_management.listview_row_should_not_contain(locator, column_name, cell_text, expected)

    @keyword
    def select_listview_cell_by_column_name(self, locator, row_index, column_name):
        self.listview_management.select_listview_cell(locator, column_name, row_index)

    @keyword
    def select_listview_cell_by_column_index(self, locator, row_index, column_index):
        self.listview_management.select_listview_cell_by_index(locator, column_index, row_index)

    @keyword
    def select_listview_row_by_cell_text(self, locator, column_name, cell_text):
        self.listview_management.select_listview_row(locator, column_name, cell_text)

    @keyword
    def select_listview_row_by_row_index(self, locator, row_index):
        self.listview_management.select_listview_row_by_index(locator, row_index)

    @keyword
    def get_listbox_single_selection(self, locator):
        return self._get_listbox(locator).SelectedItemText

    @keyword
    def get_listbox_multiple_selection(self, locator):
        arr = self._get_listbox(locator).Items
        list_selected = []
        for itm in arr:
            if itm.IsSelected:
                list_selected.append(itm.Text)
        return list_selected

    @keyword
    def select_listbox_value(self, locator, value):
        self.list_management.select_listbox_value(locator, value)

    @keyword
    def select_listbox_index(self, locator, item_index):
        self.list_management.select_listbox_index(locator, item_index)

    @keyword
    def listbox_selection_should_be(self, locator, expected):
        self.list_management.listbox_selection_should_be(locator, expected)

    @keyword
    def listbox_should_contain(self, locator, expected):
        self.list_management.listbox_should_contain(locator, expected)

    @keyword
    def listbox_should_not_contain(self, locator, expected):
        self.list_management.listbox_should_not_contain(locator, expected)

    @keyword
    def select_combobox_value(self, locator, value):
        self.list_management.select_combobox_value(locator, value)

    @keyword
    def select_combobox_index(self, locator, item_index):
        self.list_management.select_combobox_index(locator, item_index)

    @keyword
    def verify_combobox_selection(self, locator, expected):
        combobox = self._get_combobox(locator)
        self.ctx.verify_value(expected, combobox.SelectedItemText)

    @keyword
    def get_combobox_selection(self, locator):
        return self._get_combobox(locator).SelectedItemText

    @keyword
    def combobox_should_contain(self, locator, expected):
        self.list_management.combobox_should_contain(locator, expected)

    @keyword
    def combobox_should_not_contain(self, locator, expected):
        self.list_management.combobox_should_not_contain(locator, expected)

    def _get_row(self, locator, column_name, cell_text):
        listview = self._get_listview(locator)
        return listview.Rows.Get(column_name, cell_text)

    def _get_row_by_index(self, locator, index):
        listview = self._get_listview(locator)
        return listview.Rows.Get(int(index))

    def _get_cell(self, locator, column_name, row_index):
        listview = self._get_listview(locator)
        return listview.Cell(column_name, int(row_index))

    def _get_cell_by_index(self, locator, row, column):
        listview = self._get_listview(locator)
        return listview.Rows.Get(int(row)).Cells[int(column)]

    def _get_combobox(self, locator):
        return self.ctx.get_typed_item_by_locator(ComboBox, locator)

    def _get_listbox(self, locator):
        return self.ctx.get_typed_item_by_locator(ListBox, locator)

    def _get_listview(self, locator):
        return self.ctx.get_typed_item_by_locator(ListView, locator)
