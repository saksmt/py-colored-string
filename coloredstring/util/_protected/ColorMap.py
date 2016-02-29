from .Color import Color

__author__ = 'smt'


class ColorMap(Color):

    Black = 0
    Red = 1
    Green = 2
    Brown = 3
    Blue = 4
    Magenta = 5
    Cyan = 6
    Gray = 7
    DarkGray = 60
    LightRed = 61
    LightGreen = 62
    Yellow = 63
    LightBlue = 64
    LightMagenta = 65
    LightCyan = 66
    White = 67
    Default = 9

    _base = 0

    @classmethod
    def get_color(cls, color_code):
        if color_code == cls.Default:
            color_code = -cls._base
        return "\033[" + str(cls._base + color_code) + "m"
