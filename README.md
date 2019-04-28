# learning-Python

My journey learning Python. I'm learning version 2 (specifically 2.7) of the language (current version is 3)

## Installation

The official Python download is [here](https://www.python.org/downloads/).

## Hello World

Since Python is an interpreted language, it's pretty easy to take the first step. Just open a console window an enter `python`, and after some introduction you will get a prompt of `>>>`. Write `print "Hello"` and hit enter. Python "Hello"s you back:

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

*Declaration*: Variables can be declared anywhere in a Python script. Variables are declared when they are assigned a value so there is no way to have a variable without a value (although you can assign a None type to a variable, but the variable still has a value).

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

Python supports `string`s surrounded by single ('...') or double ("...") quotes. The backslash ('\') character is used to escape quotes.

```python
>>> "This is a string"
'This is a string'
>>> 'This is also a string'
'This is also a string'
>>> 'No we can\'t'
"No we can't"
```

Special characters like '\n' (newline) and '\t' (tab) are supported as expected. You can disable special characters by creating _raw strings_ which are `string`s preceded by the letter `r`.

```python
>>> "Line 1\nLine2"
'Line 1\nLine2'
>>> r"c:\new\time"
'c:\\new\\time'
```

A `string` can span multiple lines by using triple quotes (''' or """). The new lines in the `string` are kept except if the line ends with a '\'.

```python
>>> """\    # this new line is ignored
>>> Hello
>>> World
>>> """
'Hello\nWorld\n'
```

`String`s can be concatenated using the `+` operator and repeated using the `*` operator (not sure who came up with the idea that this was good, but that's life).

```python
>>> "Hello " + "World"
'Hello World'
>>> "Na" * 18 + " Batman!"  # WAT - https://www.destroyallsoftware.com/talks/wat
'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa Batman!'  
```

Lastly, the contents of a `string` can be indexed using square brackets (`[]`) and sliced using a colon (`:`) inside the brackets. The first letter in the `string` is index `0`. Negative numbers can also be used as indexes, where `-1` is the last character from the end from the `string`, decreasing towards the beginning. When indexing a single `string` character, the result is a `string` of one letter. You can omit the initial or final index of the slice, which translates to slicing from the start or to the end of the `string`. When slicing, the first index is always included, and the last excluded. Indexing a non-exiting element in a `string` results in an error, but slicing on non-existing indexes will fail silently (at least from my POV), returning an empty `string`.

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

`String`s are immutable, so don't try to assign a value to a `string` index. You need to create a new `string` for this.

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

The slice `[:]` of a sequence returns a full copy of the sequence.

Lists that could be build as a function over a range or some other list of values can be created using a syntactic sugar called list comprehension. This is basically a mix of the `map` function and `for` loop in one place. This is useful but some times syntactic sugar makes the code harder to read, so use it wisely.

```python
>>> doubles = [x**2 for x in range(10)]
>>> doubles
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> new_doubles = [x*x for x in range(10) if (x*x)%2 != 0]
>>> new_doubles
[1, 9, 25, 49, 81]
```

#### Tuples

A tuple is an immutable group of values, which can have 0 or more values. Tuples can also contain other tuples. Creating a tuple with values is called _tuple packing_. They can be _unpacked_ by putting multiple identifiers on the right side of an assignment, one for each element of the tuple. This actually works for any type of sequence.

```python
>>> a = ()  # empty tuple
>>> a
()
>>> b = 1,  # tuple with one value. Note that you can't use () here because it's interpreted as grouping of expressions
>>> b
(1,)
>>> c = 1,2,3
>>> c
(1, 2, 3)
>>> d = a,b,c
>>> d
((), (1,), (1, 2, 3))
>>> x,y,z = d
>>> x
()
>>> y
(1,)
>>> z
(1, 2, 3)
```

#### Sets

A set is an unordered collection of elements with no duplicates. They support set operations: `'` (union), `&` (intersection), `-` (difference), and `&` (symmetric difference).

```python
>>> left = set(range(0,6))
>>> left
set([0, 1, 2, 3, 4, 5])
>>> right = set(range(4,10))
>>> right
set([4, 5, 6, 7, 8, 9])
>>> left | right
set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> left - right
set([0, 1, 2, 3])
>>> left & right
set([4, 5])
>>> left ^ right
set([0, 1, 2, 3, 6, 7, 8, 9])
```

#### Dictionaries

A dictionary is a key-value store. They key of a dictionary can be any immutable type (e.g. strings, numbers). Tuples can be used as keys if they contain only immutable values. Keys are unique. Storing a value on an existing key override the existing value, and fetching a value from a non-existing key is an error. 

```python
>>> dict = {'a': 1, 'b': 2, 'c': 3}
>>> dict['a']
1
>>> dict.keys()
['a', 'c', 'b']
>>> dict.values()
[1, 3, 2]

```

Comprehensions can be used to create dictionaries.

```python
>>> dict = { x : x**x for x in range(5) }
>>> dict
{0: 1, 1: 1, 2: 4, 3: 27, 4: 256}
```

## Conditions

Python comes with built-in boolean values `True` and `False` values. These values support the `and`, `or`, and `not` operators. The `and` and `or` operators are evaluated from left to right and short-circuit when the result is assured.

```python
>>> a = True
>>> b = False
>>> a and b
False
>>> a or b
True
>>> not a
False
```

The `in` operator checks if a value is contained in a sequence.

```python
>>> l = ['a', 'b', 'c']
>>> 'a' in l
True
>>> 'z' in l
False
```

Sequences can be compared one to another if they are of the same type (string, list, etc). The comparison is done lexicographically - if the first element is different then the second element is compared, and so on until all elements are compared. It is possible to compare objects of different types but the results are weird and there is no promise that in the future they will be the same.

```python
>>> [1,2,3] < [1,2,3,4]
True
>>> [1,2,3,4] > [1,2,3,4]
False
>>> [1,2,3,4] == [1,2,3,4]
True
```


## Control Flow

Python supports the usual control flow statements that exist in popular languages: `while`, `for`, `if`. 

At this point you need to know a very important thing - indentation is part of the syntax of the Python language. While in languages like C, Java and C# you would use curly brackets (`{` and `}`) to group a set of expressions, in Python you a colon (`:`) to start the group, and after this you use indentation. It doesn't have to be a specific number of whitespaces - it can be a tab, a space, two tabs, or whatever. Kind of weird, ah?

`While` loops are very straightforward:

```python
>>> i = 0
>>> while i < 5:
...     print i,    # Note the comma here that suppresses the newline character in the print function.
...     i += 1
...
0 1 2 3 4
```

`If` statements can appear alone, with zero or more `elif`s after it, and an optional `else` at the end.

```python
>>> if x > 10:
...     print 'Big!'
... elif x < 10:
...     print 'Small!'
... else:
...     print 'Just right :-)'
```

`For` are very interesting. Instead of having the user define an initial setup, step conditions, and halting condition, Python uses `for` loops to iterate over items of a sequence (for example a `string`).

```python
>>> city = 'london'
>>> for letter in city:
...     print letter,
...
l o n d o n
```

But many times we just want to loop a specific number of times... so how do we do this? By using the `range` function which returns a `sequence` containing arithmetic progressions. The `range` function can take one, two or three parameters, but for now we'll use only one.

```python
>>> r = range(5)
>>> r
[0, 1, 2, 3, 4]
>>> for i in r:
...     print i,
...
0 1 2 3 4
```

Loop statements can have a `break` statement, which breaks the innermost enclosing loop. They can also have a `continue` statement which skips the rest of the code for the loop and goes to the beginning of the loop.

```python
>>> for i in range(10):
...     if i == 8:
...             break
...     elif i % 2 == 0:
...             continue
...     print i,
...
1 3 5 7
```

There is also an option to add an `else` clause to the end of a loop but I think it is confusing so I won't add it here.

When looping through a sequence we can fetch the index and the value at the same time using the `enumerate` function.

```python
>>> a = ['a', 'b', 'c', 'd']
>>> for i, v in enumerate(a):
...     print i, v
...
0 a
1 b
2 c
3 d
```

You can loop over multiple sequences at the same time using the `zip` function.

```python
>>> for a, b in zip(range(5), range(5,10)):
...     print a, b
...
0 5
1 6
2 7
3 8
4 9
```

When looping over dictionaries, you can use the `iteritems` function to iterate over all key-value pairs.

```python
>>> dict = {'a':1, 'b':2, 'c':3}
>>> for k,v in dict.iteritems():
...     print k, v
...
a 1
c 3
b 2
```

## Functions

A function is defined using the `def` keyword. It can have zero or more parameters and an optional return value. As in control flow expressions, functions use indentation to define the code that is contained inside it. After the function definition and before the body you can add a documentation string literal (and you should do this most of the time).

```python
>>> def print_count(n):
...     """Print the numbers up to (but excluding) n and Finished!"""
...     for i in range(n):
...             print i,
...     print 'Finished!'
...
>>> print_count(10)
0 1 2 3 4 5 6 7 8 9 Finished!
```

Arguments are passed by value, when a value is always an _object reference_ (more on this later). Variables assigned in the function body are local to the function. A function can reference variables in enclosing scopes up to the global scope but cannot override them. If a function sets the of a variable in its scope, it can only reference the local variable after it has been set. Functions can also be defined inside other functions, which makes them available inside the function where they are defined.

```python
>>> def f1():
...     a = 2
...     def f2():
...         a = 3
...         print a
...     f2()
...     print a
...
>>> f1()
3
2
>>> print a
1
```

All functions return a value. If no value is set explicitly, the return value is `None`. To return a value use the `return` statement inside the function body.

```python
>>> def f1():
...     print "a"
...
>>> def f2():
...     return 5
...
>>> print f1()
a
None
>>> print f2()
5
```

Python functions support default argument values,

```python
>>> def print_separated(elements, separator = ' - '):
...     result = ""
...     for element in elements:
...         result += element + separator
...     if (len(result) > 0):
...         result = result[0:-3]
...     print result
...
>>> print_separated(["a","b", "c", "d"])
a - b - c - d
>>> print_separated(["a", "b", "c", "d"], " & ")
a & b & c & d
```

calling functions with named (_keyword_) arguments,

```python
>>> def calculation_with_many_parameters(a = 10, b = 15, c = 2.4, d = 4, e = 6):
...     return a * b / c + d * e
...
>>> print calculation_with_many_parameters(a=0, b=0)
24.0
>>> print calculation_with_many_parameters(e=0)
62.5
```

and argument lists.

```python
>>> def sum_values(*args):
...     sum = 0
...     for val in args:
...         sum += val
...     return sum
...
>>> print sum_values(1,2,3,4)
10
>>> print sum_values(1,2,3,4,5,6)
21
```

Functions can be returned from functions and assigned to variables and re

```python
>>> def f1(a):
...     def f2(b):
...         return a*b
...
>>>
>>>
>>> def f1(a):
...     def f2(b):
...         return a*b
...     return f2
...
>>> a = f1
>>> print a(1)(1)
1
>>> b = f1(2)
>>> print b(2)
4
```

When a function is short you can use `lambda` expressions, which is just syntactic sugar for single expression functions.

```python
>>> f1 = lambda x: x + 5
>>> print f1(5)
10
```

## Modules

A module is a file that contains python definitions and statements. The name of the file is the name of the module with `.py` after. So in file
`module1.py` we write

```python
def f1():
    print "Hello from f1"

def f2():
    print "Hello from f2"
```

and then from the interpreter (running in the same directory as the module)

```python
>>> import module1
>>> module1.f1()
Hello from f1
```

If we are lazy (and we all are), we can import the function into the current namespace.

```python
>>> from module1 import f1
>>> f1()
Hello from f1
```

And if we are very lazy (and not worried about name collisions), we can import all the definitions in the module

```python
>>> from module1 import *
>>> f1()
Hello from f1
>>> f2()
Hello from f2
```

A module can contain executable statements outside definitions. They are executed the first time the module is loaded (which is the first time an import from the module is found). Import statements can be anywhere in a script/file but its customary to put them at the beginning. 

You can import a module and rename it using `import module1 as kuku`. This means that if `f1` is in `module1`, you can now use `kuku.f1()` and things will work. This is excellent for [job security](https://github.com/Droogans/unmaintainable-code) but not so much for code readability, so please, please don't do it.

Modules are first searched in the built-in modules, and if it's not there it is searched in the directories given by the variable `sys.path` (inside module `sys`). This variable is initialized with the directory of the input script (or the current directory if in the interpreter), the contents of the `pythonpath` environment variable, and the defaults for the current installation. 

Modules can be created in hierarchical directory structures called _packages_. Python assumes a directory in its path is a package if it has a file named  `__init__.py` in it. For example, let's say we have a directory in the path called `package1` with an init file and a module file named `module1.py` with function `f1`, and inside `package1` there is a directory called `package2` that also has an init file and a module file named `module2.py` with function `f2`, we can reference the functions as follows.

```python
import package1
import package1.package2

package1.module1.f1()
package1.package2.module2.f2()
```

And once again, since we are lazy and don't want to type too much, we can import both a function and a module to the namespace.

```python
from package1 import module1
from package1.package2.module2 import f2

module1.f1()
f2()
```

If two modules are in the same package, one module can import the other without having to give the full package name. Furthermore, packages are relative so if `module2` is in `package1.package2` and `module1` is in `package1` then `module1` can import `module2` using only `from package2 import module2`.

It is possible to import all of the modules of a package if the `__init__.py` file of the package defines a list named `__all__` containing the names of all modules in that package. It is up to the "owner" of the package to make sure this list is always up to date.

## Exceptions

The well known try/catch idiom is also used in Python to handle exceptions. 

```python
>>> try:
...     5/0
... except ZeroDivisionError:
...     print "Wooops!"
...
Wooops!
```

Multiple exception types can be caught in the same handler using `except (ExceptionType1, ExceptionType2, ...)`. Multiple exception handlers can be defined. A catch-all exception handler with no type can be added at the end of the block to catch any exception that was not caught by other handlers. A `try/except` block can have an `else` clause at the end which is executed if no exception was raised. And lastly, the block can have a `finally` clause that is executed after all the block, regardless if an exception was raised or not. A typical use for this is to close resources after opening them, regardless if an exception ocurred.

```python
try:
    f = open(filename)
    s = f.readline()
    i = int(s.strip())
except IOError:
    print "cannot open", filename
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error"
else:
    print "This is only executed if there are no exceptions"
finally:
    f.close()   # Always executed
```

An exception is thrown using the `raise` statement, which receives an instance of an `Exception`. The `Exception` object can contain data that can be referenced by the catcher of the exception using `except ExceptionType as variable_name`.

```python
>>> try:
...     raise Exception("Woops!")
... except Exception as e:
...     print e
...
Woops!
```

## Classes

Python classes are defined with the `class` keyword. A class can have properties and methods, it can inherit from a parent class and can override parent methods. A class definition can also include documentation that describes what the class does, and also class variables that are shared by all instances. A class is instantiated by using the class name as a function (no `new` operator). Class attributes (values or functions) are accessed using the `.` operator on the class instance. When an instance function is called, the interpreter will automatically put a reference to the calling instance as the first parameter of the function, which is usually called `self`. You can call it whatever you want, but you shouldn't). In the end, the call `instance.method()` is equivalent to `class.method(instance)`

```python
>>> class A:
...     """This is the documentation"""
...     i = 5
...     def f1(self):
...         print "This is an instance function"
...
>>> print A.i
5
>>> a = A()
>>> a.f1()
This is an instance function
>>> A.f1(a)
This is an instance function
>>> a.i
5
```

A class can be initialize by creating a function named `__init__`. This method can have multiple arguments to customize how the instance is created. Instance variables, just like regular variables, come into existence when they are first assigned, which can be any place in the class definition or outside the class definition.

```python
>>> class B:
...     def __init__(self, x):
...         self.x = x
...
>>> b = B("hello")
>>> print b.x
hello
>>> b.y = "world"
>>> print b.y
world
```

Python does not support _data encapsulation_. Data inside a class instance can be accessed by any that has a handle to that instance.

Classes can be _inherited_. All attributes of the base class are available in the derived class. The derive class can also override attributes of the base class. It is possible to reference a method of the base class of a derived class using `BaseClass.method(self, arguments)`. When an attribute is referenced, it is searched in the instantiated class. If it doesn't exist there, the search is done recursively on base classes until found (or not).

```python
>>> class A:
...     def f1(self):
...         print "Function f1 in A"
...
>>> class B(A):
...     def f2(self):
...         print "Function f2 in B"
...
>>> b = B()
>>> b.f1()
Function f1 in A
>>> b.f2()
Function f2 in B
>>> class C(A):
...     def f1(self):
...         print "Function f1 in C"
...
>>> c = C()
>>> c.f1()
Function f1 in C
>>> A.f1(c)
Function f1 in A
```

Multiple inheritance is supported using `class A(X, Y, Z):`. I won't get into more details here because if you are using multiple inheritance you either know what you are doing, or you should not be using multiple inheritance. 

## Built-in Functions

### General

* `del(x)` - delete variable `a`. This can also be used to delete class attributes.
* `enumerate(i)` - create an enumerator for `i` which on iteration returns a tuple `(index, value)` matching `i`.
* `isinstance(o, class)` - check if `o` is an instance of `class`.
* `issubclass(c2, c1)` - check if `c2` is a subclass of `c1`. 
* `len(x)` - length of an object which can be and iterable or a collection.
* `max(i)` - largest item in iterable `i` based on default ordering.
* `min(i)` - smallest item in iterable `i` based on default ordering.
* `range(stop)` - a list starting at `0` and ending at `stop-1`
* `range(start, stop, step = 1)` - a list starting at `start`, progressing with `v(n+1) = v(n) + step` and ending with the value previous to `stop` in the direction of the step.
* `round(x[,d])` - round `x` to `d` digits after the decimal point. Rounding is done towards +infinity.
* `set([i])` - create a set object, optionally initialized with the values in iterable `i`.
* `str(o)` - a string with a nice represenation of `o`.
* `sum(i)` - sum of all elements in `i`.
* `tuple(i)` - a tuple with all the elements contained in `i`.
* `type(o)` - the type on `o`.
* `zip([i1[,...]])` - create a list of tuples containing in tuple `i` the `i`th value of all input iterables. The lenght of the list equals the shortest of the input iterators. With no arguments it returns an empty list.

### Functional Programming

* `filter(f,i)` - create a new list with all the elements of `i` that return true for `f`.
* `map(f, i)` - apply function `f` to every element of iterable `i` and return a list with the results.
* `reduce(f, i[,init])` - apply function `f` cumulative to a pair of elements of `i` from left to right, returning the accumulated value. If `i` has only one element is is returned. If `init` exists it works as if `i` had one more value at the beginning.

### Data Structures

Useful functions of popular data structures

* List
  * `list.append(x)` - add `x` to the end of the list.
  * `list.extend(l)` - add all elements in `l` to the end of the list. Assumes `l` is iterable.
  * `list.insert(i,x)` - Inserts `x` at index `i` of the list pushing existing elements. If `i` is equal or greater than the length of the list then `x` is added to the end of the list.
  * `list.remove(x)` - remove the first element in the list with value equals to `x`. Existing elements are pushed left after removal. If there is no element equal to `x` it is an error.
  * `list.pop()` - remove and return the last element of the list.
  * `list.index(x)` - returns the index of the first item in the list that equals to `x`.
  * `list.count(x)` - returns the number of time the value `x` appears on the list.
  * `list.sort()` - sort the elements of the list in place. Default sorting is used.
  * `list.reverse()` - reverse the elements of the list in place.
* String
  * `str.format()` - perform a string format operation. For example, `"hello {0:.3f}, welcome {1}".format(1,2)` will output "hello 1.000, welcome 2".
  
## Conventions

Classes: use PascalCase (camelCase with the initial letter capitalized) for class names.

Constants: should be all-caps with underscores between words, e.g. `THIS_IS_A_CONSTANT`.

Functions: should be in lowercase, with underscores between words, e.g. `this_is_a_function`. Names of non-public methods should start with a leading underscore, e.g.`_private_function`.  

Modules: lowercase, with underscores if this improves readability.

Variables: should be in lowercase, with underscores between words, e.g. `this_is_a_variable`. Names of non-public variables should start with a leading underscore, e.g. `_private_variable`.

## Magic Variables

`_`: the value of the last printed expression in the interactive console.