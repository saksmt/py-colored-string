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
 
NOTE: Enumerations have method `get_color` for creating string with escape sequence

**Classes:**

*coloredstring.ColoredString*:

Methods:

 * Static:
  * `render(string)` - renders string in specified [format](format.md)
  * `success_message(message)` - renders message with leading green *" \* "*
  * `info_message(message)` - renders message with leading cyan *" \* "*
  * `warning_message(message)` - renders message with leading yellow *" \* "*
  * `error_message(message)` - renders message with leading red *" \* "*
  * `question_message(message)` - renders message with leading bold white *">>> "*
  
 * Instance:
  * `set_background_color(color_code)` - set's background color for object, `color_code` - code from enumeration
  * `set_foreground_color(color_code)` - set's foreground color for object, `color_code` - code from enumeration
  * `set_attribute(attribute_code)` - set's attribute for object, `attribute_code` - code from enumeration
