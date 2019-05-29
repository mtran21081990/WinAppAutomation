from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import TreeKeywords
from TestStack.White.UIItems.TreeItems import Tree

__version__ = '1.0.1'


class TreeManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.tree_management = TreeKeywords(ctx)

    @keyword
    def get_tree_name(self, locator):
        tree = self._get_tree(locator)
        return tree.Name

    @keyword
    def get_tree_help_text(self, locator):
        tree = self._get_tree(locator)
        return tree.HelpText

    @keyword
    def get_tree_access_key(self, locator):
        tree = self._get_tree(locator)
        return tree.AccessKey

    @keyword
    def get_tree_location(self, locator):
        tree = self._get_tree(locator)
        return tree.Location

    @keyword
    def get_tree_bound(self, locator):
        tree = self._get_tree(locator)
        return tree.Bounds

    @keyword
    def get_tree_image(self, locator):
        tree = self._get_tree(locator)
        return tree.VisibleImage

    @keyword
    def get_tree_selection(self, locator):
        tree = self._get_tree(locator)
        return tree.SelectedNode.Text

    @keyword
    def is_tree_enabled(self, locator):
        tree = self._get_tree(locator)
        return tree.Enabled

    @keyword
    def is_tree_visible(self, locator):
        tree = self._get_tree(locator)
        return tree.Visible

    @keyword
    def is_tree_focused(self, locator):
        tree = self._get_tree(locator)
        return tree.IsFocussed

    @keyword
    def focus_on_tree(self, locator):
        tree = self._get_tree(locator)
        if not tree.Enabled:
            raise AssertionError("Tree '{}' is not enabled to be focused.".format(locator))
        tree.Focus()

    @keyword
    def select_tree_node(self, locator, *node_path):
        self.tree_management.select_tree_node(locator, *node_path)

    @keyword
    def expand_tree_node(self, locator, *node_path):
        self.tree_management.expand_tree_node(locator, *node_path)

    @keyword
    def double_click_tree_node(self, locator, *node_path):
        self.tree_management.double_click_tree_node(locator, *node_path)

    @keyword
    def right_click_tree_node(self, locator, *node_path):
        self.tree_management.right_click_tree_node(locator, *node_path)

    @keyword
    def verify_tree_selection(self, locator, expected, case_sensitive=True):
        tree_selection = self.get_tree_selection(locator)
        self.ctx.verify_string_value(expected, tree_selection, case_sensitive)

    def _get_tree(self, locator):
        return self.ctx.get_typed_item_by_locator(Tree, locator)
