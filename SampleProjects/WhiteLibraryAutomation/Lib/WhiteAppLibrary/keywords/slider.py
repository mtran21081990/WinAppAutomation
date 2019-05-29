from ..base import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.keywords.items import SliderKeywords
from TestStack.White.UIItems import Slider

__version__ = '1.0.1'


class SliderManagement(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.slider_management = SliderKeywords(ctx)

    @keyword
    def get_slider_name(self, locator):
        slider = self._get_slider(locator)
        return slider.Name

    @keyword
    def get_slider_help_text(self, locator):
        slider = self._get_slider(locator)
        return slider.HelpText

    @keyword
    def get_slider_access_key(self, locator):
        slider = self._get_slider(locator)
        return slider.AccessKey

    @keyword
    def get_slider_location(self, locator):
        slider = self._get_slider(locator)
        return slider.Location

    @keyword
    def get_slider_bound(self, locator):
        slider = self._get_slider(locator)
        return slider.Bounds

    @keyword
    def get_slider_image(self, locator):
        slider = self._get_slider(locator)
        return slider.VisibleImage

    @keyword
    def get_slider_value(self, locator):
        return self.slider_management.get_slider_value(locator)

    @keyword
    def get_slider_max_value(self, locator):
        slider = self._get_slider(locator)
        return slider.Maximum

    @keyword
    def get_slider_min_value(self, locator):
        slider = self._get_slider(locator)
        return slider.Minimum

    @keyword
    def is_slider_enabled(self, locator):
        slider = self._get_slider(locator)
        return slider.Enabled

    @keyword
    def is_slider_visible(self, locator):
        slider = self._get_slider(locator)
        return slider.Visible

    @keyword
    def is_slider_focused(self, locator):
        slider = self._get_slider(locator)
        return slider.IsFocussed

    @keyword
    def focus_on_slider(self, locator):
        slider = self._get_slider(locator)
        if not slider.Enabled:
            raise AssertionError("Slider '{}' is not enabled to be focused.".format(locator))
        slider.Focus()

    @keyword
    def set_slider_value(self, locator, value):
        self.slider_management.set_slider_value(locator, value)

    @keyword
    def verify_slider_value(self, locator, expected):
        self.slider_management.verify_slider_value(locator, expected)

    def _get_slider(self, locator):
        return self.ctx.get_typed_item_by_locator(Slider, locator)
