# learning-python

My journey learning Python. I'm learning version 2 (specifically 2.7) of the language (current version is 3)

## Installation

The official python download is [here](https://www.python.org/downloads/).

## Hello World

Since python is an interpreted language, it's pretty easy to take the first step. Just open a console window an enter `python`, and after some introduction you will get a prompt of `>>>`. Write `print "Hello"` and hit enter. Python "Hello"s you back:

```python
>>> print "hello"
hello
>>>
```

## Variables, Type System, and Basic Types

### Type System

Python is [dynamically typed](https://en.wikipedia.org/wiki/Type_system#Dynamic_type_checking_and_runtime_type_information). 
This means that you don't need to state the type of variables, parameters, or return values, where makes code shorter and simpler, but at the same time you don't have a compiler that is looking behind your back so you don't do stupid things. Everything has a price in life :-).

### Variables

*Declaration*: Variables can be declared anywhere in a python script. Variables are declared when they are assigned a value so there is no way to have a variable without a value (although you can assign a None type to a variable, but the variable still has a value).

*Scope*: Variables declared outside all classes and functions are _global_ variables accessible from any part of the program. A variable defined inside a function is _local_ to the function and only accessible from inside the function. If a _local_ variable has the same name as a _global_ variable, the _local_ variable hides the _global_ variable inside its scope. This can cause confusion so it's better to have unique variable names all around. Variables can be declared in the body of a class, outside of any class method, making them _class_ variables. They are shared by all class instances and can also be used without a class instance (we'll talk more about classes later).

### Basic Built-in Types

#### Numbers

The two basic numerical types are `int` and `float`.

```python
>>> 5           # this is an int
5
>>> 4.5         # this is a float
4.5
>>> foo = 42    # assign the int value 42 to the variable foo
>>> bar = 3.14  # assign the float value 3.14 to the variable bar
```

these types support basic mathematical operations: `+`, `-`, `*`, `/`, `%` (remainder), `**` (power). Division of two `int`s yields an `int` that is the floor of the division operation (round down). For all operations where there are `int` and `float` mixed, the `int` is converted to a `float` and the result is a `float`.

#### Strings

Python supports strings surrounded by single ('...') or double ("...") quotes. The backslash ('\') character is used to escape quotes.

```python
>>> "This is a string"
'This is a string'
>>> 'This is also a string'
'This is also a string'
>>> 'No we can\'t'
"No we can't"
```

Special characters like '\n' (newline) and '\t' (tab) are supported as expected. You can disable special characters by creating _raw strings_ which are strings preceded by the letter `r`.

```python
>>> "Line 1\nLine2"
'Line 1\nLine2'
>>> r"c:\new\time"
'c:\\new\\time'
```

A string can span multiple lines by using triple quotes (''' or """). The new lines in the string are kept except if the line ends with a '\'.

```python
>>> """\    # this new line is ignored
>>> Hello
>>> World
>>> """
'Hello\nWorld\n'
```

Strings can be concatenated using the `+` operator and repeated using the `*` operator (not sure who came up with the idea that this was good, but that's life).

```python
>>> "Hello " + "World"
'Hello World'
>>> "Na" * 18 + " Batman!"  # WAT - https://www.destroyallsoftware.com/talks/wat
'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa Batman!'  
```

Lastly, the contents of a string can be indexed using square brackets (`[]`) and sliced using a colon (`:`) inside the brackets. The first letter in the string is index `0`. Negative numbers can also be used as indexes, where `-1` is the last character from the end from the string, decreasing towards the beginning of the string. When indexing a single string character, the result is also a string of one letter. You can leave out the initial or final index of the slice, which translates to slicing from the start or to the end of the string. When slicing, the first index is always included, and the last excluded. Indexing a non-exiting element in a string results in an error, but slicing on non-existing indexes will fail silently (at least from my POV) returning an empty string.

```python
>>> foo = "Ironman sucks"
>>> foo[5]
'a'
>>> foo[4:7]
'man'
>>> foo[:7]
'Ironman'
>>> foo[-1]
's'
>>> foo[-5:]
'sucks
>>> foo[54:]
''
```

Strings are immutable, so don't try to assign a value to a string index. You need to create a new string for this.

#### Lists

Python has built-in support for lists, written as comma separated elements inside square brackets.

```python
>>>> favoriteCities = ["London", "Copenhagen", "Boston"]
>>> numberOfVisits = [6, 1, 3]
>>> mixingBoth = ["London", 6, "Copenhagen", 1, "Boston", 3]
```

As you can see in the last example, lists can contain elements of different types.

Similarly to strings (because both of theme are `sequence`s), lists support slicing and indexing. Unlike strings, lists are mutable, so new items can be added and removed from the list using a single index or a slice.

```python
>>> favoriteCities[1]
'Copenhagen'
>>> favoriteCities[-3]
'London'
>>> favoriteCities[3:4] = ['Haifa', 'Cali']
>>> favoriteCities
['London', 'Copenhagen', 'Boston', 'Haifa', 'Cali']
>>> favoriteCities[2:3] = []
>>> favoriteCities
['London', 'Copenhagen', 'Haifa', 'Cali']
>>> favoriteCities[2] = 'Madrid'
>>> favoriteCities
['London', 'Copenhagen', 'Madrid', 'Cali']
```

## Magic Variables

`_`: the value of the last printed expression in the interactive console.