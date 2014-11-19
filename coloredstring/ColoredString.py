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
    def SuccessMessage(cls, message):
        return cls._createMessage(message, cls._successMessagePrompt)

    @classmethod
    def WarningMessage(cls, message):
        return cls._createMessage(message, cls._warningMessagePrompt)

    @classmethod
    def ErrorMessage(cls, message):
        return cls._createMessage(message, cls._errorMessagePrompt)

    @classmethod
    def InfoMessage(cls, message):
        return cls._createMessage(message, cls._infoMessagePrompt)

    @classmethod
    def QuestionMessage(cls, message):
        return cls._createMessage(message, cls._questionPrompt)

    @classmethod
    def _createMessage(cls, message, prompt):
        return str(cls(prompt)) + str(cls(message))

    def __add__(self, other):
        return str(self) + str(other)

    def __init__(self, string=""):
        self.__string = string

    def __str__(self):
        return self.render(self.__string)

    def setForegroundColor(self, colorCode):
        return self.__setColor(ForegroundColor.getColor(colorCode))

    def setBackgroundColor(self, colorCode):
        return self.__setColor(BackgroundColor.getColor(colorCode))

    def setAttribute(self, attributeCode):
        return self.__setColor(Attribute.getColor(attributeCode))

    @classmethod
    def render(cls, stringToRender):
        result = stringToRender
        parts = cls._matcher.finditer(stringToRender)
        for part in parts:
            subparts = cls._subMatcher.finditer(part.group('expression'))
            subresult = part.group('content')
            for subpart in subparts:
                subresult = str(cls.__wrapWithColor(subpart, subresult))
            result = result.replace(part.group(0), str(subresult))
        return result + ForegroundColor.getColor(ForegroundColor.Default)

    @classmethod
    def __wrapWithColor(cls, regexMatch, string):
        colorName = regexMatch.group('colorName')
        colorType = regexMatch.group('type')
        if colorName is None or colorType is None:
            return string
        return cls(string).__setColor(cls.__getColorByName(colorName, colorType))

    @classmethod
    def __getColorByName(cls, colorName, colorType):
        if colorType == 'bg':
            colorType = BackgroundColor
        elif colorType == 'fg':
            colorType = ForegroundColor
        else:
            colorType = Attribute
        colorName = colorName[0].upper() + colorName[1:]
        color = colorType.mro()[-3].__dict__.get(colorName)
        if color is None:
            color = colorType.Default
        return colorType.getColor(color)

    def __setColor(self, color):
        self.__string = color + self.__string
        return self