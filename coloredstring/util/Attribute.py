from ._protected.Color import Color

__author__ = 'smt'


class Attribute(Color):

    Bold = 1
    Dim = 2
    Underlined = 4
    Blink = 5
    Reverse = 7
    Hidden = 8
    Default = 0

    @classmethod
    def get_color(cls, color_code):
        return "\033[" + str(color_code) + "m"
