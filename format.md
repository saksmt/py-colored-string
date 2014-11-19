Format reference
================

Base template: `{{ "STRING" | type=value }}`, where `|type=value` named expression.

`"STRING"`
----------

String to apply expressions

`expression`
------------

Expression to apply on string, template can have more than one expression

`type`
------

Type of expression, currently one of `bg`, `fg` or `attr`.

Explanation:

 * `bg` for `BackgroundColor` enumeration
 * `fg` for `ForegroundColor` enumeration
 * `attr` for `Attribute` enumeration

`value`
-------

Value of expression, variable name of enumeration with lowercased first letter for readability

Notes
=====

1. Strings in this format can be rendered by `coloredstring.ColoredString.render(string)` or by constructing new object of `coloredstring.ColoredString` class.

2. Invalid syntax ignored, so by providing template like this: `'{{ "Hello world"|fg=**invalid** }}'` you'll get `"Hello world"` after rendering.

Example
=======

`'{{ "Hello world"|fg=black|bg=white|attr=underlined }}'` - result would be black underlined string on white background
