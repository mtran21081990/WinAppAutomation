from SikuliLibrary import SikuliLibrary
from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__version__ = '1.0.0'


class SikuliWrapperKeywords(KeywordGroup):

    def __init__(self):
        self.sikuli = SikuliLibrary(mode='NEW')

    def add_image_path(self, path):
        arguments = [path]
        self.sikuli.run_keyword("addImagePath", arguments)

    def capture_screen(self):
        return self.sikuli.run_keyword("captureScreen")

    def change_screen_id(self, screen_id):
        arguments = [screen_id]
        self.sikuli.run_keyword("changeScreenId", arguments)

    def clear_all_highlights_on_screen(self):
        self.sikuli.run_keyword("clearAllHighlights")

    def clear_highlight(self, image_name):
        arguments = [image_name]
        self.sikuli.run_keyword("clearHighlight", arguments)

    def click_on_image(self, image_name, x_offset=0, y_offset=0):
        arguments = [image_name, x_offset, y_offset]
        self.sikuli.run_keyword("click", arguments)

    def click_on_target_image_in_an_area_image(self, target_image_name, area_image_name):
        arguments = [area_image_name, target_image_name]
        self.sikuli.run_keyword("clickIn", arguments)

    def click_on_region(self, x_pos, y_pos, width, height, wait=0, timeout=30):
        coordinates = [x_pos, y_pos, width, height]
        arguments = [coordinates, wait, timeout]
        self.sikuli.run_keyword("clickRegion", arguments)

    def double_click_on_image(self, image_name, x_offset=0, y_offset=0):
        arguments = [image_name, x_offset, y_offset]
        self.sikuli.run_keyword("doubleClick", arguments)

    def double_click_on_target_image_in_an_area_image(self, target_image_name, area_image_name):
        arguments = [area_image_name, target_image_name]
        self.sikuli.run_keyword("doubleClickIn", arguments)

    def drag_source_image_to_target_image(self, source_image_name, target_image_name):
        arguments = [source_image_name, target_image_name]
        self.sikuli.run_keyword("dragAndDrop", arguments)

    def drag_source_image_by_offset(self, source_image_name, x_offset, y_offset):
        arguments = [source_image_name, x_offset, y_offset]
        self.sikuli.run_keyword("dragAndDropByOffset", arguments)

    def image_exists(self, image_name, timeout=30):
        arguments = [image_name, timeout]
        return self.sikuli.run_keyword("exists", arguments)

    def get_current_screen_id(self):
        return self.sikuli.run_keyword("getCurrentScreenId")

    def get_image_coordinates(self, image_name, coordinates=None):
        arguments = [image_name, coordinates]
        return self.sikuli.run_keyword("getImageCoordinates", arguments)

    def get_number_of_screen(self):
        return self.sikuli.run_keyword("getNumberOfScreens")

    def get_text_from_image(self, image_name):
        self._set_ocr_text_read(True)
        arguments = [image_name]
        text = self.sikuli.run_keyword("getText", arguments)
        self._set_ocr_text_read(False)
        return text

    def highlight_image(self, image_name, timeout=3):
        arguments = [image_name, timeout]
        self.sikuli.run_keyword("highlight", arguments)

    def highlight_region(self, x_pos, y_pos, width, height, timeout=3):
        coordinates = [x_pos, y_pos, width, height]
        arguments = [coordinates, timeout]
        self.sikuli.run_keyword("highlightRegion", arguments)

    def input_text_on_image(self, image_name, text=None):
        arguments = [image_name, text]
        self.sikuli.run_keyword("inputText", arguments)

    def mouse_move_to_image(self, image_name):
        arguments = [image_name]
        self.sikuli.run_keyword("mouseMove", arguments)

    def mouse_down(self, *mouse_buttons):
        arguments = [*mouse_buttons]
        self.sikuli.run_keyword("mouseDown", arguments)

    def mouse_up(self, *mouse_buttons):
        arguments = [*mouse_buttons]
        self.sikuli.run_keyword("mouseUp", arguments)

    def mouse_wheel_down(self, image_name, step):
        arguments = [step, image_name]
        self.sikuli.run_keyword("wheelDown", arguments)

    def mouse_wheel_up(self, image_name, step):
        arguments = [step, image_name]
        self.sikuli.run_keyword("wheelUp", arguments)

    def sikuli_open_application(self, app_path):
        arguments = [app_path]
        self.sikuli.run_keyword("openApplication", arguments)

    def sikuli_close_application(self, app_name):
        arguments = [app_name]
        self.sikuli.run_keyword("closeApplication", arguments)

    def paste_text_into_image(self, image_name, text):
        arguments = [image_name, text]
        self.sikuli.run_keyword("pasteText", arguments)

    def press_special_key(self, key):
        arguments = [key]
        self.sikuli.run_keyword("pressSpecialKey", arguments)

    def read_text_from_region(self, region):
        arguments = [region]
        return self.sikuli.run_keyword("readTextFromRegion", arguments)

    def remove_image_path(self, path):
        arguments = [path]
        self.sikuli.run_keyword("removeImagePath", arguments)

    def right_click_on_image(self, image_name):
        arguments = [image_name]
        self.sikuli.run_keyword("rightClick", arguments)

    def right_click_on_target_image_in_area_image(self, target_image_name, area_image_name):
        arguments = [target_image_name, area_image_name]
        self.sikuli.run_keyword("rightClickIn", arguments)

    def screen_should_contain(self, image_name):
        arguments = [image_name]
        return self.sikuli.run_keyword("screenShouldContain", arguments)

    def screen_should_not_contain(self, image_name):
        arguments = [image_name]
        return self.sikuli.run_keyword("screenShouldNotContain", arguments)

    def select_and_capture_region(self, message):
        arguments = [message]
        return self.sikuli.run_keyword("selectRegion", arguments)

    def set_capture_image_directory(self, path):
        arguments = [path]
        self.sikuli.run_keyword("setCaptureFolder", arguments)

    def set_move_mouse_delay(self, delay):
        arguments = [delay]
        self.sikuli.run_keyword("setMoveMouseDelay", arguments)

    def set_slow_motion_delay(self, delay):
        arguments = [delay]
        self.sikuli.run_keyword("setSlowMotionDelay", arguments)

    def set_timeout(self, timeout=30):
        arguments = [timeout]
        self.sikuli.run_keyword("setTimeout", arguments)

    def wait_for_image(self, wanted_image, not_wanted_image, timeout=30):
        arguments = [wanted_image, not_wanted_image, timeout]
        self.sikuli.run_keyword("waitForImage", arguments)

    def wait_for_images(self, wanted_images, not_wanted_images, timeout=30, time_between_check=10):
        arguments = [timeout, time_between_check, wanted_images, not_wanted_images]
        self.sikuli.run_keyword("waitForMultipleImages", arguments)

    def wait_until_screen_contains(self, image_name, timeout=30):
        arguments = [image_name, timeout]
        self.sikuli.run_keyword("waitUntilScreenContain", arguments)

    def wait_until_screen_not_contains(self, image_name, timeout=30):
        arguments = [image_name, timeout]
        self.sikuli.run_keyword("waitUntilScreenNotContain", arguments)

    def capture_region_of_interest(self):
        return self.sikuli.run_keyword("captureRoi")

    def highlight_region_of_interest(self, timeout=3):
        arguments = [timeout]
        self.sikuli.run_keyword("highlightRoi", arguments)

    def reset_region_of_interest(self):
        self.sikuli.run_keyword("resetRoi")

    def set_region_of_interest(self, x_pos, y_pos, width, height, timeout=3):
        coordinates = [x_pos, y_pos, width, height]
        arguments = [coordinates, timeout]
        self.sikuli.run_keyword("setRoi", arguments)

    def _set_ocr_text_read(self, true_or_false):
        arguments = [true_or_false]
        self.sikuli.run_keyword("setOcrTextRead", arguments)
