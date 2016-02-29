from .util.Attribute import Attribute
from .util.BackgroundColor import BackgroundColor
from .util.ForegroundColor import ForegroundColor
import re

__author__ = 'smt'


class ColoredString(object):

    _matcher = re.compile('\{\{"(?P<content>.*?)"\s*(?P<expression>.*?)\}\}')
    _subMatcher = re.compile('\s*\|(?P<type>(bg)|(fg)|(attr))=(?P<colorName>[a-zA-Z]+)\s*')
    _successMessagePrompt = ' {{"*"|fg=green}} '
    _warningMessagePrompt = ' {{"*"|fg=yellow}} '
    _errorMessagePrompt = ' {{"*"|fg=red}} '
    _infoMessagePrompt = ' {{"*"|fg=cyan}} '
    _questionPrompt = '{{">>>"|fg=white|attr=bold}} '

    @classmethod
    def success_message(cls, message):
        return cls._create_message(message, cls._successMessagePrompt)

    @classmethod
    def warning_message(cls, message):
        return cls._create_message(message, cls._warningMessagePrompt)

    @classmethod
    def error_message(cls, message):
        return cls._create_message(message, cls._errorMessagePrompt)

    @classmethod
    def info_message(cls, message):
        return cls._create_message(message, cls._infoMessagePrompt)

    @classmethod
    def question_message(cls, message):
        return cls._create_message(message, cls._questionPrompt)

    @classmethod
    def _create_message(cls, message, prompt):
        return str(cls(prompt)) + str(cls(message))

    def __add__(self, other):
        return str(self) + str(other)

    def __init__(self, string=""):
        self.__string = string

    def __str__(self):
        return self.render(self.__string)

    def set_foreground_color(self, color_code):
        return self.__set_color(ForegroundColor.get_color(color_code))

    def set_background_color(self, color_code):
        return self.__set_color(BackgroundColor.get_color(color_code))

    def set_attribute(self, attribute_code):
        return self.__set_color(Attribute.get_color(attribute_code))

    @classmethod
    def render(cls, string_to_render):
        result = string_to_render
        parts = cls._matcher.finditer(string_to_render)
        for part in parts:
            subparts = cls._subMatcher.finditer(part.group('expression'))
            subresult = part.group('content')
            for subpart in subparts:
                subresult = str(cls.__wrap_with_color(subpart, subresult))
            result = result.replace(part.group(0), str(subresult))
        return result + ForegroundColor.get_color(ForegroundColor.Default)

    @classmethod
    def __wrap_with_color(cls, regex_match, string):
        color_name = regex_match.group('colorName')
        color_type = regex_match.group('type')
        if color_name is None or color_type is None:
            return string
        return cls(string).__set_color(cls.__get_color_by_name(color_name, color_type))

    @classmethod
    def __get_color_by_name(cls, color_name, color_type):
        if color_type == 'bg':
            color_type = BackgroundColor
        elif color_type == 'fg':
            color_type = ForegroundColor
        else:
            color_type = Attribute
        color_name = color_name[0].upper() + color_name[1:]
        color = color_type.mro()[-3].__dict__.get(color_name)
        if color is None:
            color = color_type.Default
        return color_type.get_color(color)

    def __set_color(self, color):
        self.__string += color
        return self
