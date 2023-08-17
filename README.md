# Python Tutorial 3.11
[The Python Tutorial - 3.11.4](https://docs.python.org/3/tutorial/index.html)

[The Python Standard Library](https://docs.python.org/3/library/index.html#library-index)

[The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index)


## 1. Whetting Your Appetite

## 2. Using the Python Interpreter

### 2.1. Invoking the Interpreter

Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: quit().

```
$ python
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

## 3. An Informal Introduction to Python

### 3.1. Using Python as a Calculator

#### 3.1.1. Numbers

```
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # division always returns a floating point number
1.6
```

```
>>> 17 /3 # classic division returns a float
5.666666666666667
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3   # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17
```

```
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

```
>>> n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

```
>>> 4 * 3.75 - 1
14.0
```

In interactive mode, the last printed expression is assigned to the variable _. 

```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

#### 3.1.2. Text

```
>>> 'spam eggs'    # single quotes
'spam eggs'
>>> "Paris rabbit got your back :! Yay!"  # double quotes
'Paris rabbit got your back :! Yay!'
>>> '1975'       #digits and numerals enclosed in quotes are also strings
'1975'
```

To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks:

```
>>> 'doesn\'t'   # use \' to escape the single quote
"doesn't"
>>> "doesn't"    # or use double quotes instead 
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t" they said'
'"Isn\'t" they said'
```

```
>>> s = 'First line.\nSecond line.'   # \n means newline
>>> s   # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s)   # with print(), special characters are interpreted , so \n produces new line
First line.
Second line.
```

If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

```
>>> print('C:\some\name')   # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

There is one subtle aspect to raw strings: a raw string may not end in an odd number of \ characters; 
see the [FAQ entry](https://docs.python.org/3/faq/programming.html#faq-programming-raw-string-backslash) 
for more information and workarounds.

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.

```
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                   Display this usage message
...      -H hostname          Hostname to connect to
... """)
Usage: thingy [OPTIONS]
     -h                   Display this usage message
     -H hostname          Hostname to connect to
```

```
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

```
>>> 'Py' 'thon'
'Python'
```

```
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

Strings can be indexed (subscripted), with the first character having index 0. 

```
>>> word = 'Python'
>>> word[0]    # character in position 0
'P'
>>> word[5]    # character in position 5
'n'
>>> word[-1]   # last character
'n'
>>> word[-2]   # second-last character
'o'
>>> word[-6]     
'P'
```

Slices

```
>>> word[:2]  # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]  # characters from position 4 (included) to the end
'on'
>>> word[-2:] # characters from the second-last (included) to the end
'on'
```

```
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

However, out of range slice indexes are handled gracefully when used for slicing:

```
>>> word[4:42]
'on'
>>> word[42:]
''
```

__See also:__

[Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#textseq)

Strings are examples of sequence types, and support the common operations supported by such types.

[String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

Strings support a large number of methods for basic transformations and searching.

[Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

String literals that have embedded expressions.

[Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)

Information about string formatting with str.format().

[printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)

The old formatting operations invoked when strings are the left operand of the % operator are described in more detail here.

#### 3.1.3. Lists

_Lists_  can be written as a list of comma-separated values (items) between square brackets.

```
>>> squares = [ 1, 4, 9, 16, 25 ]
>>> squares
[1, 4, 9, 16, 25]
>>> squares + [ 36, 49, 64, 81, 100 ] 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

```
>>> cubes = [ 1, 8, 27, 65, 125 ] # something's wrong here
>>> 4 ** 3 # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64         # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]

>>> cubes.append(216)     # add the cube of 6
[1, 8, 27, 64, 125, 216]
>>> cubes.append(7 ** 3)  # and the cube of 7 
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

```
>>> letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = [ 'C', 'D', 'E' ] 
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

```
>>> letters = [ 'a', 'b', 'c', 'd' ] 
>>> len(letters)
4
```

Nesting lists

```
>>> a = [ 'a', 'b', 'c' ]
>>> n = [ 1, 2, 3 ]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

### 3.2. First Steps Towards Programming

```
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
... 
0
1
1
2
3
5
8
```

* The first line contains a multiple assignment
* The while loop executes as long as the condition (here: a < 10) remains true.
* The body of the loop is indented: indentation is Python’s way of grouping statements.

```
>>> i = 256*256 
>>> print('The value of i is', i)
The value of i is 65536
```

## 4. More Control Flow Tools

### 4.1. if Statements¶

```
x = int(input("Please enter an integer: "))
if x <0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Please enter an integer: 42
# More
```

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’.

### 4.2. for Statements

```
# Measure some strings:
words = [ 'cat', 'window', 'defenestrate' ]
for w in words:
    print(w, len(w))

# cat 3
# window 6
# defenestrate 12
```

```
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print("users: ", users)

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print("active_users: ", active_users)

# users:  {'Hans': 'active', '景太郎': 'active'}
# active_users:  {'Hans': 'active', '景太郎': 'active'}
```

### 4.3. The range() Function

```
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
```

```
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

```
>>> a = [ 'Mary', 'had', 'a', 'little', 'lamb' ]
>>> for i in range(len(a)):
...     print(i, a[i])
... 
0 Mary
1 had
2 a
3 little
4 lamb
```

A strange thing happens if you just print a range:
```
>>> range(10)
range(0, 10)
```

```
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```

### 4.4. break and continue Statements, and else Clauses on Loops

* The break statement breaks out of the innermost enclosing for or while loop.

* A for or while loop can include an else clause.

* In a for loop, the else clause is executed after the loop reaches its final iteration.

* In a while loop, it’s executed after the loop’s condition becomes false.

* In either kind of loop, the else clause is not executed if the loop was terminated by a break.

```
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break 
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
```

```
for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# Found an even number 2
# Found an odd number 3
# Found an even number 4
# Found an odd number 5
# Found an even number 6
# Found an odd number 7
# Found an even number 8
# Found an odd number 9
```

### 4.5. pass Statements¶

The __pass__ statement does nothing. It can be used when a statement is 
required syntactically but the program requires no action. 

```
>>> while True:
...     pass            # Busy-wait for keyboard interrupt (Ctrl+C)
```

This is commonly used for creating minimal classes:

```
>>> class MyEmptyClass:
...     pass
... 
```

Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code.

```
>>> def initlog(*args):
...     pass   # Remember to implement this!
... 
```

### 4.6. match Statements

A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it’s more similar to pattern matching in languages like Rust or Haskell. 

```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"

print(http_error(500))

# Something's wrong with the Internet
```

You can combine several literals in a single pattern using | (“or”):

```
case 401 | 403 | 404:
    return "Not allowed"
```

Patterns can look like unpacking assignments, and can be used to bind variables:

```
point = (0,5)

# point is an (x,y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# Y=5
```

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def where_is(point):
        match point:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else")
            case _:
                print("Not a point")

p = Point(0,5)
p.where_is()
# Y=5
```

```
class Point:
    # __match_args__ allows to define a default order for arguments to be matched in when a custom class is used in a case
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = Point(0,5)

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```


We can add an if clause to a pattern, known as a “guard”. If the guard is false, match goes on to try the next case block. Note that value capture happens before the guard is evaluated:

```
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

Patterns may use named constants. These must be dotted names to prevent them from being interpreted as capture variable:

```
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
```

[PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)

### 4.7. Defining Functions

```
def fib(n):     # write Fibonacci series up to n
    """Print a Fibonaccie series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
```

```
def fib2(n):        # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

### 4.8. More on Defining Functions

It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

#### 4.8.1. Default Argument Values

```
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

```

* ask_ok('Do you really want to quit?')
* ask_ok('OK to overwrite the file?', 2)
* ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

The default values are evaluated at the point of function definition in the defining scope, so that

```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# 5
```

__Important warning:__ The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

```
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# [1]
# [1, 2]
# [1, 2, 3]
```

If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# [1]
# [2]
# [3]
```

#### 4.8.2. Keyword Arguments

Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:

```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# -- This parrot wouldn't voom if you put 1000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

# -- This parrot wouldn't voom if you put 1000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

# -- This parrot wouldn't jump if you put a million volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's bereft of life !

# -- This parrot wouldn't voom if you put a thousand volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's pushing up the daisies !
```


but all the following calls would be invalid:

* parrot()                     # required argument missing
* parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
* parrot(110, voltage=220)     # duplicate value for the same argument
* parrot(actor='John Cleese')  # unknown keyword argument

Duplicate keyword arguments

```
def function(a):
    pass 

function(0, a=0)

# Traceback (most recent call last):
#   File "D:\drs\Python\PythonTutorial_3.11\004_ControlFlow\018_multiple_keyword_arguments.py", line 4, in <module>
#     function(0, a=0)
# TypeError: function() got multiple values for argument 'a'
```

When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a function like this:

```
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.      
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch
```

Note that the order in which the keyword arguments are printed is guaranteed to match the order in which they were provided in the function call.

#### 4.8.3. Special parameters

A function definition may look like:

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

where / and * are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.

##### 4.8.3.1. Positional-or-Keyword Arguments

If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword.

##### 4.8.3.2. Positional-Only Parameters

Looking at this in a bit more detail, it is possible to mark certain parameters as positional-only. If positional-only, the parameters’ order matters, and the parameters cannot be passed by keyword. Positional-only parameters are placed before a / (forward-slash). The / is used to logically separate the positional-only parameters from the rest of the parameters. If there is no / in the function definition, there are no positional-only parameters.

Parameters following the / may be positional-or-keyword or keyword-only.

##### 4.8.3.3. Keyword-Only Arguments

To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.

##### 4.8.3.4. Function Examples

```
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

```