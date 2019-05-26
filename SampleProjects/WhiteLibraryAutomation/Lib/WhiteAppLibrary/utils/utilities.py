import re
import os
import datetime


class Utilities(object):

    @staticmethod
    def format_os_path(path):
        return path.replace('\\', '/') if os.sep == '/' else path.replace('/', '\\')

    @staticmethod
    def format_executable_path(path):
        return Utilities.format_os_path(path if ".exe" in path else path + ".exe")

    @staticmethod
    def get_project_path():
        """
        Get the root directory of the project
        """
        return os.getcwd()

    @staticmethod
    def convert_rgb_to_hex(rgb_string):
        color_tuple = rgb_string.replace("rgba(", "").replace("rgb(", "").replace(")", "").replace(" ", "")
        color_tuple = color_tuple.split(",")
        rgb = (int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2]))
        hex_str = Utilities.rgb_to_hex(rgb)
        return hex_str

    @staticmethod
    def is_rgb_color(color_str):
        r = r"rgb\((\d+),\s*(\d+),\s*(\d+)\)"
        r2 = r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*(\d+)\)"
        return re.match(r, color_str) or re.match(r2, color_str)

    @staticmethod
    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))

    @staticmethod
    def rgb_to_hex(rgb):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        return '#%02X%02X%02X' % (r, g, b)

    @staticmethod
    def is_sublist(m_list, sublist):
        for i in sublist:
            if not (i in m_list):
                return False
        return True

    @staticmethod
    def is_directory_not_empty(directory):
        try:
            list_files = os.listdir(directory)
            return list_files != []
        except:
            return False

    @staticmethod
    def is_downloaded_file_has_extension(directory, ext):
        try:
            list_files = os.listdir(directory)
            if list_files != []:
                for f in list_files:
                    if f.endswith(ext):
                        return True
            return False
        except:
            return False

    @staticmethod
    def get_current_datetime_as_name():
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
