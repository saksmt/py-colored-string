py-colored-string
=================

Python library for colorizing strings in bash

API
---

 **Enumerations(via static class variables)**
 
*coloredstring.util.Foreground* & *coloredstring.util.Background*:

 * Red
 * Green
 * Blue
 * Yellow
 * Brown
 * Gray
 * White
 * Black
 * Magenta
 * Cyan
 * Default
 * DarkGray
 * LightRed
 * LightGreen
 * LightBlue
 * LightGray
 * LightMagenta
 * LightCyan
 
*coloredstring.util.Attribute*:

 * Bold
 * Dim
 * Underlined
 * Reverse
 * Blink
 * Hidden
 * Default
 
NOTE: Enumerations have method `getColor` for creating string with escape sequence

**Classes:**

*coloredstring.ColoredString*:

Methods:

 * Static:
  * `render(string)` - renders string in specified [format](format.md)
  * `SuccessMessage(message)` - renders message with leading green *" \* "*
  * `InfoMessage(message)` - renders message with leading cyan *" \* "*
  * `WarningMessage(message)` - renders message with leading yellow *" \* "*
  * `ErrorMessage(message)` - renders message with leading red *" \* "*
  * `QuestionMessage(message)` - renders message with leading bold white *">>> "*
  
 * Instance:
  * `setBackgroundColor(colorCode)` - set's background color for object, `colorCode` - code from enumeration
  * `setForegroundColor(colorCode)` - set's foreground color for object, `colorCode` - code from enumeration
  * `setAttribute(attributeCode)` - set's attribute for object, `attributeCode` - code from enumeration
