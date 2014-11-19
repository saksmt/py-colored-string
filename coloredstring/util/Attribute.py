from ._protected.ColorInterface import ColorInterface

__author__ = 'smt'


class Attribute(ColorInterface):

    Bold = 1
    Dim = 2
    Underlined = 4
    Blink = 5
    Reverse = 7
    Hidden = 8
    Default = 0

    @classmethod
    def getColor(cls, colorCode):
        return "\033[" + str(colorCode) + "m"