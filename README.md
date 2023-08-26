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

##### 4.8.3.5. Recap
The use case will determine which parameters to use in the function definition:

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```

As guidance:

* Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

* Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

* For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

#### 4.8.4. Arbitrary Argument Lists

Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see [Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tut-tuples)). Before the variable number of arguments, zero or more normal arguments may occur.

```
def concat(*args, sep="/"):
    return sep.join(args)


print('concat("earth", "mars", "venus")')
print(concat("earth", "mars", "venus"))

print('\nconcat("earth", "mars", "venus", sep=".")')
print(concat("earth", "mars", "venus", sep="."))
```

#### 4.8.5. Unpacking Argument Lists

```
print("list(range(3,6))")
print(list(range(3, 6)))

args = [3, 6]
print("args = [3, 6]")
print("list(range(*args))")
print(list(range(*args)))

# [3, 4, 5]
# args = [3, 6]
# list(range(*args))
# [3, 4, 5]
```

#### 4.8.6. Lambda Expressions

Small anonymous functions can be created with the lambda keyword. 

Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

```
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))  # 42
print(f(1))  # 43 
```

#### 4.8.7. Documentation Strings

Here are some conventions about the content and formatting of documentation strings.

The first line should always be a short, concise summary of the object’s purpose. For brevity, it should not explicitly state the object’s name or type, since these are available by other means (except if the name happens to be a verb describing a function’s operation). This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

```
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
```

#### 4.8.8. Function Annotations

[Function annotations](https://docs.python.org/3/reference/compound_stmts.html#function) are completely optional metadata information about the types used by user-defined functions (see [PEP 3107](https://peps.python.org/pep-3107/) and [PEP 484](https://peps.python.org/pep-0484/) for more information).

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function.

The following example has a required argument, an optional argument, and the return value annotated:
```
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

### 4.9. Intermezzo: Coding Style

For Python, [PEP 8](https://peps.python.org/pep-0008/) has emerged as the style guide that most projects adhere to; 
it promotes a very readable and eye-pleasing coding style.

* Use 4-space indentation, and no tabs.

* 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.

* Wrap lines so that they don’t exceed 79 characters.

* This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.

* Use blank lines to separate functions and classes, and larger blocks of code inside functions.

* When possible, put comments on a line of their own.

* Use docstrings.

* Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).

* Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).

* Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.

* Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.

## 5. Data Structures

### 5.1. More on Lists

* list.append(_x_)
* list.extend(_iterable_)
* list.insert(_i, x_)
* list.remove(x)
* list.pop(_[index]_)
* list.clear()
* list.index(_x, [, start [, end]]_)
* list.count(x)
* list.sort(_*, key=NOne, reverse=False_)
* list.reverse()
* list.copy()

```
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
# 2
print(fruits.count("tangerine"))
# 0
print(fruits.index("banana"))
# 3
print(fruits.index("banana", 4))  # Find next banana starting at position 4
# 6
fruits.reverse()
print(fruits)
# ["banana", "apple", "kiwi", "banana", "pear", "apple", "orange"]
fruits.append("grape")
print(fruits)
# ["banana", "apple", "kiwi", "banana", "pear", "apple", "orange", "grape"]
fruits.sort()
print(fruits)
# ["apple", "apple", "banana", "banana", "grape", "kiwi", "orange", "pear"]
print(fruits.pop())
# 'pear'
```

#### 5.1.1. Using Lists as Stacks

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. For example:

```
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
# [3, 4, 5, 6, 7]
print(stack.pop())
# 7
print(stack)
# [3, 4, 5, 6]
print(stack.pop())
# 6
print(stack.pop())
# 5
print(stack)
# [3, 4]
```

#### 5.1.2. Using Lists as Queues

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) which was designed to have fast appends and pops from both ends. For example:

```
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue)
# deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
print(queue.popleft())  # The first to arrive now leaves
# "Eric"
print(queue.popleft())  # The second to arrive now leaves
# "John"
print(queue)
# deque(['Michael', 'Terry', 'Graham'])
```

#### 5.1.3. List Comprehensions

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

```
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

points = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(points)
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

from math import pi

mypi = [str(round(pi, i)) for i in range(1, 6)]
print(mypi)
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

#### 5.1.4. Nested List Comprehensions

The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

```
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


new_matrix = list(zip(*matrix))
print(matrix)
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(*matrix)
# [1, 2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12]
print(new_matrix)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

See [Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments) for details on the asterisk in this line.

### 5.2. The del statement

There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

```
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
# [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
# [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)
# [1, 66.25, 1234.5]
del a[:]
print(a)
# []
```

del can also be used to delete entire variables:

```
del a
```

Referencing the name a hereafter is an error (at least until another value is assigned to it). We’ll find other uses for [del](https://docs.python.org/3/reference/simple_stmts.html#del) later.

### 5.3. Tuples and Sequences¶

We saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequence data types (see [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq)).

A tuple consists of a number of values separated by commas, for instance:

```
t = 12345, 54321, "hello!"
print(t[0])
# 12345
print(t)
# (12345, 54321, "hello!")
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# ((12345, 54321, "hello!"), (1, 2, 3, 4, 5))
# Tuples are immutable:
try:
    t[0] = 88888
except TypeError:
    print("TypeError: 'tuple' object does not support item assignment")

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
([1, 2, 3], [3, 2, 1])
```

Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:

```
empty = ()
singleton = ("hello",)  # <-- note trailing comma
print(len(empty))
# 0
print(len(singleton))
# 1
print(singleton)
# ("hello",)
```

Unpacking a tuple

```
# tuple packing
t = 12345, 54321, "hello!"
# tuple unpacking
x, y, z = t
print("x: ", x, "y: ", y, "z: ", z)
# x:  12345 y:  54321 z:  hello!
```

### 5.4. Sets

Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

Here is a brief demonstration:

```
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # show that duplicates have been removed
# {"orange", "banana", "pear", "apple"}
print("orange" in basket)  # fast membership testing
# True
print("crabgrass" in basket)
# False

# Demonstrate set operations on unique letters from two words

a = set("abracadabra")
b = set("alacazam")
print(a)  # unique letters in a
# {"a", "r", "b", "c", "d"}
print(b)  # unique letters in b
# {'m', 'l', 'z', 'a', 'c'}
print(a - b)  # letters in a but not in b
# {"r", "d", "b"}
print(a | b)  # letters in a or b or both
# {"a", "c", "r", "d", "b", "m", "z", "l"}
print(a & b)  # letters in both a and b
# {"a", "c"}
print(a ^ b)  # letters in a or b but not both
# {"r", "d", "b", "m", "z", "l"}
```

Similarly to list comprehensions, set comprehensions are also supported:

```
a = {x for x in "abracadabra" if x not in "abc"}
print(a)
# {'r', 'd'}
```

### 5.5 Dictionaries

Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

Here is a small example using a dictionary:

```
tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)
# {"jack": 4098, "sape": 4139, "guido": 4127}
print(tel["jack"])
# 4098
del tel["sape"]
tel["irv"] = 4127
print(tel)
# {"jack": 4098, "guido": 4127, "irv": 4127}
print(list(tel))
# ["jack", "guido", "irv"]
print(sorted(tel))
# ["guido", "irv", "jack"]
print("guido" in tel)
# True
print("jack" not in tel)
# False
```

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

```
phone_numbers = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])
print(phone_numbers)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
```

In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

```
squares = {x: x**2 for x in (2, 4, 6)}
print(squares)
# {2: 4, 4: 16, 6: 36}
```

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

```
phone_numbers = dict(sape=4139, guido=4127, jack=4098)
print(phone_numbers)
# {"sape": 4139, "guido": 4127, "jack": 4098}
```

### 5.6. Looping Techniques

Dictionary Looping Technique

```
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)

# gallahad the pure
# robin the brave
```

Sequence Looping Technique

```
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

# 0 tic
# 1 tac
# 2 toe
```

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

```
for i in reversed(range(1, 10, 2)):
    print(i)

# 9
# 7
# 5
# 3
# 1
```

To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

```
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for i in sorted(basket):
    print(i)

# apple
# apple
# banana
# orange
# orange
# pear
```

It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

```
import math

raw_data = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
# [56.2, 51.7, 55.3, 52.5, 47.8]
```

### 5.7. More on Conditions

The conditions used in while and if statements can contain any operators, not just comparisons.

The comparison operators in and not in are membership tests that determine whether a value is in (or not in) a container. The operators is and is not compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than that of all numerical operators.

Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.

Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition.

The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,

```
string1, string2, string3 = "", "Trondheim", "Hammer Dance"
non_null = string1 or string2 or string3
print(non_null)
# "Trondheim"
```

Note that in Python, unlike C, assignment inside expressions must be done explicitly with the walrus operator :=. This avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.

### 5.8. Comparing Sequences and Other Types

Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:

```
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

Note that comparing objects of different types with < or > is legal provided that the objects have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.

## 6. Modules

To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

```
# Fibonacci numbers module


def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
```

### 6.1. More on Modules

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement. 1 (They are also run if the file is executed as a script.)

Each module has its own private namespace, which is used as the global namespace by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables. On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module (or script, for that matter). The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a module directly into the importing module’s namespace. For example:

```
from fibo import fib, fib2
fib(500)
```

This does not introduce the module name from which the imports are taken in the local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

```
from fibo import *
fib(500)
```

This imports all names except those beginning with an underscore (_). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

If the module name is followed by as, then the name following as is bound directly to the imported module.

```
import fibo as fib
fib.fib(500)
```

This is effectively importing the module in the same way that import fibo will do, with the only difference of it being available as fib.

It can also be used when utilising from with similar effects:

```
from fibo import fib as fibonacci
fibonacci(500)
```

#### 6.1.1. Executing modules as scripts

When you run a Python module with

```
python fibo.py &lt;arguments&gt;
```

the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:

```
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```


you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

```
$ python fibo.py 500
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
```

If the module is imported, the code is not run:

```
$ python
>>> import fibo
>>> 
```

This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).

#### 6.1.2. The Module Search Path

When a module named spam is imported, the interpreter first searches for a built-in module with that name. These module names are listed in [sys.builtin_module_names](https://docs.python.org/3/library/sys.html#sys.builtin_module_names). If not found, it then searches for a file named spam.py in a list of directories given by the variable [sys.path](https://docs.python.org/3/library/sys.html#sys.path). [sys.path](https://docs.python.org/3/library/sys.html#sys.path) is initialized from these locations:

* The directory containing the input script (or the current directory when no file is specified).

* [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names, with the same syntax as the shell variable PATH).

* The installation-dependent default (by convention including a site-packages directory, handled by the [site](https://docs.python.org/3/library/site.html#module-site) module).

More details are at [The initialization of the sys.path module search path](https://docs.python.org/3/library/sys_path_init.html#sys-path-init).

After initialization, Python programs can modify [sys.path](https://docs.python.org/3/library/sys.html#sys.path). The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended. See section [Standard Modules](https://docs.python.org/3/tutorial/modules.html#tut-standardmodules) for more information.

#### 6.1.3. “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc, where the version encodes the format of the compiled file; it generally contains the Python version number. For example, in CPython release 3.3 the compiled version of spam.py would be cached as __pycache__/spam.cpython-33.pyc. This naming convention allows compiled modules from different releases and different versions of Python to coexist.

Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that’s loaded directly from the command line. Second, it does not check the cache if there is no source module. To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.

Some tips for experts:

* You can use the [-O](https://docs.python.org/3/using/cmdline.html#cmdoption-O) or [-OO](https://docs.python.org/3/using/cmdline.html#cmdoption-OO) switches on the Python command to reduce the size of a compiled module. The -O switch removes assert statements, the -OO switch removes both assert statements and \_\_\_doc\_\_\_ strings. Since some programs may rely on having these available, you should only use this option if you know what you’re doing. “Optimized” modules have an opt- tag and are usually smaller. Future releases may change the effects of optimization.

* A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that’s faster about .pyc files is the speed with which they are loaded.

* The module [compileall](https://docs.python.org/3/library/compileall.html#module-compileall) can create .pyc files for all modules in a directory.

* There is more detail on this process, including a flow chart of the decisions, in [PEP 3147](https://peps.python.org/pep-3147/).

### 6.2 Standard Modules

Python comes with a library of standard modules, described in a separate document, the Python Library Reference (“Library Reference” hereafter). Some modules are built into the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide access to operating system primitives such as system calls. The set of such modules is a configuration option which also depends on the underlying platform. For example, the [winreg](https://docs.python.org/3/library/winreg.html#module-winreg) module is only provided on Windows systems. One particular module deserves some attention: sys, which is built into every Python interpreter. The variables sys.ps1 and sys.ps2 define the strings used as primary and secondary prompts:

```
import sys
sys.ps1
'>>> '
sys.ps2
'... '
sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings that determines the interpreter’s search path for modules. It is initialized to a default path taken from the environment variable [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), or from a built-in default if PYTHONPATH is not set. You can modify it using standard list operations:

```
import sys
sys.path.append('/ufs/guido/lib/python')
```

### 6.3. The [dir()](https://docs.python.org/3/library/functions.html#dir) Function

The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:

```
import fibo, sys
dir(fibo)
dir(sys)
```

Without arguments, dir() lists the names you have defined currently:

```
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
```

Note that it lists all types of names: variables, modules, functions, etc.

[dir()](https://docs.python.org/3/library/functions.html#dir) does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module [builtins](https://docs.python.org/3/library/builtins.html#module-builtins):

### 6.4. Packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.

Suppose you want to design a collection of modules (a “package”) for the uniform handling of sound files and sound data. There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au), so you may need to create and maintain a growing collection of modules for the conversion between the various file formats. There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect), so in addition you will be writing a never-ending stream of modules to perform these operations. Here’s a possible structure for your package (expressed in terms of a hierarchical filesystem):


When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

The \_\_init\_\_.py files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, \_\_init\_\_.py  can just be an empty file, but it can also execute initialization code for the package or set the \_\_all\_\_ variable, described later.

Users of the package can import individual modules from the package, for example:

```
import sound.effects.echo
```

This loads the submodule sound.effects.echo. It must be referenced with its full name.

```
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

An alternative way of importing the submodule is:

```
from sound.effects import echo
```

This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

```
echo.echofilter(input, output, delay=0.7, atten=4)
```

Yet another variation is to import the desired function or variable directly:

```
from sound.effects.echo import echofilter
```

Again, this loads the submodule echo, but this makes its function echofilter() directly available:

```
echofilter(input, output, delay=0.7, atten=4)
```

Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an ImportError exception is raised.

Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

#### 6.4.1. Importing * From a Package

Now what happens when the user writes from sound.effects import *? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the package. The import statement uses the following convention: if a package’s \_\_init\_\_.py code defines a list named \_\_all\_\_, it is taken to be the list of module names that should be imported when from package import * is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don’t see a use for importing * from their package. For example, the file sound/effects/\_\_init\_\_.py could contain the following code:

```
__all__ = ["echo", "surround", "reverse"]
```

This would mean that from sound.effects import * would import the three named submodules of the sound.effects package.

Be aware that submodules might become shadowed by locally defined names. For example, if you added a reverse function to the sound/effects/\_\_init\_\_.py file, the from sound.effects import * would only import the two submodules echo and surround, but not the reverse submodule, because it is shadowed by the locally defined reverse function:

```
__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'
```

If \_\_all\_\_ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in \_\_init\_\_.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by \_\_init\_\_.py. It also includes any submodules of the package that were explicitly loaded by previous import statements. Consider this code:

```
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

In this example, the echo and surround modules are imported in the current namespace because they are defined in the sound.effects package when the from...import statement is executed. (This also works when __all__ is defined.)

Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practice in production code.

Remember, there is nothing wrong with using from package import specific_submodule! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.

#### 6.4.2. Intra-package References

When packages are structured into subpackages (as with the sound package in the example), you can use absolute imports to refer to submodules of siblings packages. For example, if the module sound.filters.vocoder needs to use the echo module in the sound.effects package, it can use from sound.effects import echo.

You can also write relative imports, with the from module import name form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the surround module for example, you might use:

```
When packages are structured into subpackages (as with the sound package in the example), you can use absolute imports to refer to submodules of siblings packages. For example, if the module sound.filters.vocoder needs to use the echo module in the sound.effects package, it can use from sound.effects import echo.

You can also write relative imports, with the from module import name form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the surround module for example, you might use:
```

Note that relative imports are based on the name of the current module. Since the name of the main module is always "\_\_main\_\_", modules intended for use as the main module of a Python application must always use absolute imports.

#### 6.4.3. Packages in Multiple Directories

Packages support one more special attribute, \_\_path\_\_. This is initialized to be a list containing the name of the directory holding the package’s\_\_init\_\_.py before the code in that file is executed. This variable can be modified; doing so affects future searches for modules and subpackages contained in the package.

While this feature is not often needed, it can be used to extend the set of modules found in a package.

## 7. Input and Output

### 7.1. Fancier Output Formatting

```
year = 2016
event = "Referendum"
print(f"Results of the {year} {event}")
# Results of the 2016 Referendum
```

* The str.format() method of strings requires more manual effort. You’ll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted.

```
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
"{:-9} YES votes  {:2.2%}".format(yes_votes, percentage)
```

When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the repr() or str() functions.

The str() function is meant to return representations of values which are fairly human-readable, while repr() is meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax). For objects which don’t have a particular representation for human consumption, str() will return the same value as repr(). Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function. Strings, in particular, have two distinct representations.

```
$ python 
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> 'Hello, world.'
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> "'Hello, world.'"
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> '0.14285714285714285'
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> The value of x is 32.5, and y is 40000...
  File "<stdin>", line 1
    The value of x is 32.5, and y is 40000...
        ^^^^^
SyntaxError: invalid syntax
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> 'hello, world\n'
'hello, world\n'
>>> # The argument to repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

#### 7.1.1. Formatted String Literals

[Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:

```
$ python 
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

```
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')

Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():

```
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

```
>>> bugs = 'roaches'                                                                                                                                          
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```

See [self-documenting expressions](https://docs.python.org/3/whatsnew/3.8.html#bpo-36817-whatsnew) for more information on the = specifier. For a reference on these format specifications, see the reference guide for the [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec).

#### 7.1.2. The String format() Method

Basic usage of the [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) method looks like this:

```
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

```
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.

```
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Positional and keyword arguments can be arbitrarily combined:

```
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
...                                                    other='Georg'))
The story of Bill, Manfred, and Georg.
```

If you have a really long format string that you don’t want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys.

```
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

This could also be done by passing the table dictionary as keyword arguments with the ** notation.

```
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

This is particularly useful in combination with the built-in function [vars()](https://docs.python.org/3/library/functions.html#vars), which returns a dictionary containing all local variables.

As an example, the following lines produce a tidily aligned set of columns giving integers and their squares and cubes:

```
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
... 
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

For a complete overview of string formatting with [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format), see [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings).

#### 7.1.3. Manual String Formatting

Here’s the same table of squares and cubes, formatted manually:

```
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
... 
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

(Note that the one space between each column was added by the way [print()](https://docs.python.org/3/library/functions.html#print) works: it always adds spaces between its arguments.)

The [str.rjust()](https://docs.python.org/3/library/stdtypes.html#str.rjust) method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods [str.ljust()](https://docs.python.org/3/library/stdtypes.html#str.ljust) and [str.center()](https://docs.python.org/3/library/stdtypes.html#str.center). These methods do not write anything, they just return a new string. If the input string is too long, they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually better than the alternative, which would be lying about a value. (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)

There is another method, [str.zfill()], which pads a numeric string on the left with zeros. It understands about plus and minus signs:

```
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

#### 7.1.4. Old string formatting

The % operator (modulo) can also be used for string formatting. Given 'string' % values, instances of % in string are replaced with zero or more elements of values. This operation is commonly known as string interpolation. For example:

```
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

More information can be found in the [printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting) section.

### 7.2. Reading and Writing Files

[open()](https://docs.python.org/3/library/functions.html#open) returns a [file object](https://docs.python.org/3/glossary.html#term-file-object), and is most commonly used with two positional arguments and one keyword argument: open(filename, mode, encoding=None)

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent (see open()). Because UTF-8 is the modern de-facto standard, encoding="utf-8" is recommended unless you know that you need to use a different encoding. Appending a 'b' to the mode opens the file in binary mode. Binary mode data is read and written as bytes objects. You can not specify encoding when opening file in binary mode.

In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.

It is good practice to use the [with](https://docs.python.org/3/reference/compound_stmts.html#with) keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent [try-finally](https://docs.python.org/3/reference/compound_stmts.html#finally) blocks:

```
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed        // True
```

If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it.

#### 7.2.1. Methods of File Objects

The rest of the examples in this section will assume that a file object called f has already been created.

To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise, at most size characters (in text mode) or size bytes (in binary mode) are read and returned. If the end of the file has been reached, f.read() will return an empty string ('').

```
f.read()
'This is the entire file.\n'
f.read()
''
```

f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.

For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

```
for line in f:
    print(line, end='')
```

If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

f.write(string) writes the contents of string to the file, returning the number of characters written.

```
f.write('This is a test\n')     // 15
```

Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

```
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)      # 18
```

f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

To change the file object’s position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the whence argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

```
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')    # 16
f.seek(5)                       # Go to the 6th byte in the file, returns 5
f.read(1)                       # b'5'
f.seek(-3, 2)                   # Go to the 3rd byte before the end, returns 13
f.read(1)                       # returns b'd'
```

In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file are allowed (the exception being seeking to the very file end with seek(0, 2)) and the only valid offset values are those returned from the f.tell(), or zero. Any other offset value produces undefined behaviour.

File objects have some additional methods, such as [isatty()](https://docs.python.org/3/library/io.html#io.IOBase.isatty) and [truncate()](https://docs.python.org/3/library/io.html#io.IOBase.truncate) which are less frequently used; consult the Library Reference for a complete guide to file objects.

#### 7.2.2. Saving structured data with json

Strings can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called [JSON (JavaScript Object Notation)](https://json.org/). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

```
Note: The JSON format is commonly used by modern applications to allow for data exchange. Many programmers are already familiar with it, which makes it a good choice for interoperability.
```

If you have an object x, you can view its JSON string representation with a simple line of code:

```
import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

Another variant of the [dumps()](https://docs.python.org/3/library/json.html#json.dumps) function, called [dump()](https://docs.python.org/3/library/json.html#json.dump), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:

```
json.dump(x, f)
```

To decode the object again, if f is a binary file or text file object which has been opened for reading:

```
x = json.load(f)
```

```
Note: JSON files must be encoded in UTF-8. Use encoding="utf-8" when opening JSON file as a text file for both of reading and writing.
```

This simple serialization technique can handle lists and dictionaries, but serializing arbitrary class instances in JSON requires a bit of extra effort. The reference for the [json](https://docs.python.org/3/library/json.html#module-json) module contains an explanation of this.


See also [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) - the pickle module

Contrary to [JSON](https://docs.python.org/3/tutorial/inputoutput.html#tut-json), pickle is a protocol which allows the serialization of arbitrarily complex Python objects. As such, it is specific to Python and cannot be used to communicate with applications written in other languages. It is also insecure by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was crafted by a skilled attacker.

## 8. Errors and Exceptions¶

### 8.1. Syntax Errors

Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

```
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

### 8.2. Exceptions

```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError[), [NameError](https://docs.python.org/3/library/exceptions.html#NameError) and [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError).

[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) lists the built-in exceptions and their meanings.

### 8.3. Handling Exceptions

Note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.

```
>>> while True:               
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
... 
Please enter a number: abc
Oops!  That was no valid number.  Try again...
Please enter a number: Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
KeyboardInterrupt
```

The [try](https://docs.python.org/3/reference/compound_stmts.html#try) statement 

* First, the try clause (the statement(s) between the try and except keywords) is executed.

* If no exception occurs, the except clause is skipped and execution of the try statement is finished.

* If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

* If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

```
except (RuntimeError, TypeError, NameError):
...     pass
```

When an exception occurs, it may have associated values, also known as the exception’s arguments. The presence and types of the arguments depend on the exception type.

The except clause may specify a variable after the exception name. The variable is bound to the exception instance which typically has an args attribute that stores the arguments. For convenience, builtin exception types define \_\_str\_\_() to print all the arguments without explicitly accessing .args.

```
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception type
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
... 
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException) is the common base class of all exceptions. One of its subclasses, [Exception](https://docs.python.org/3/library/exceptions.html#Exception), is the base class of all the non-fatal exceptions. Exceptions which are not subclasses of Exception are not typically handled, because they are used to indicate that the program should terminate. They include [SystemExit](https://docs.python.org/3/library/exceptions.html#SystemExit) which is raised by [sys.exit()](https://docs.python.org/3/library/sys.html#sys.exit) and [KeyboardInterrupt](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt) which is raised when a user wishes to interrupt the program.

Exception can be used as a wildcard that catches (almost) everything. However, it is good practice to be as specific as possible with the types of exceptions that we intend to handle, and to allow any unexpected exceptions to propagate on.

```
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:

```
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

Exception handlers do not handle only exceptions that occur immediately in the try clause, but also those that occur inside functions that are called (even indirectly) in the try clause. For example:

```
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
... 
Handling run-time error: division by zero
```

### 8.4. Raising Exceptions

The [raise](https://docs.python.org/3/reference/simple_stmts.html#raise) statement allows the programmer to force a specified exception to occur. For example:

```
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from BaseException, such as Exception or one of its subclasses). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

```
raise ValueError  # shorthand for 'raise ValueError()'
```

If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:

```
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
... 
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

### 8.5. Exception Chaining

If an unhandled exception occurs inside an except section, it will have the exception being handled attached to it and included in the error message:

```
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: unable to handle error
```

To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause:

```
# exc must be exception instance or None.
raise RuntimeError from exc
```

This can be useful when you are transforming exceptions. For example:

```
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

It also allows disabling automatic exception chaining using the from None idiom:

```
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
... 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

For more information about chaining mechanics, see [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

### 8.6. User-defined Exceptions

Programs may name their own exceptions by creating a new exception class (see [Classes](https://docs.python.org/3/tutorial/classes.html#tut-classes) for more about Python classes). Exceptions should typically be derived from the [Exception](https://docs.python.org/3/library/exceptions.html#Exception) class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.

Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions.

Many standard modules define their own exceptions to report errors that may occur in functions they define.

### 8.7. Defining Clean-up Actions

The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances. For example:

```
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
... 
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception. 

For example:

```
def bool_return():
    try:
        return True
    finally:
        return False
```

A more complicated example:

```
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

As you can see, the [finally](https://docs.python.org/3/reference/compound_stmts.html#finally) clause is executed in any event. The [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError) raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

In real world applications, the [finally](https://docs.python.org/3/reference/compound_stmts.html#finally) clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

### 8.8. Predefined Clean-up Actions

Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed. Look at the following example, which tries to open a file and print its contents to the screen.

```
for line in open("myfile.txt"):
    print(line, end="")
```

The problem [with](https://docs.python.org/3/reference/compound_stmts.html#with) this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing. This is not an issue in simple scripts, but can be a problem for larger applications. The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

```
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

### 8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that have occurred. This is often the case in concurrency frameworks, when several tasks may have failed in parallel, but there are also other use cases where it is desirable to continue execution and collect multiple errors rather than raise the first exception.

The builtin [ExceptionGroup](https://docs.python.org/3/library/exceptions.html#ExceptionGroup) wraps a list of exception instances so that they can be raised together. It is an exception itself, so it can be caught like any other exception.

```
>>> def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
... 
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |   File "<stdin>", line 3, in f
  | ExceptionGroup: there were problems (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: e')
... 
caught <class 'ExceptionGroup'>: e
```

By using except* instead of except, we can selectively handle only the exceptions in the group that match a certain type. In the following example, which shows a nested exception group, each except* clause extracts from the group exceptions of a certain type while letting all other exceptions propagate to other clauses and eventually to be reraised.

```
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: e')
... 
caught <class 'ExceptionGroup'>: e
>>>
>>> 
>>> def f():
...     raise ExceptionGroup(
...         "group1",
...         [
...             OSError(1),
...             SystemError(2),
...             ExceptionGroup(
...                 "group2",
...                 [
...                     OSError(3),
...                     RecursionError(4)
...                 ]
...             )
...         ]
...     )
...
>>> try:
...     f()
... except* OSError as e:
...     print("There were OSErrors")
... except* SystemError as e:
...     print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |   File "<stdin>", line 2, in f
  | ExceptionGroup: group1 (1 sub-exception)
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2 (1 sub-exception)
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
```

Note that the exceptions nested in an exception group must be instances, not types. This is because in practice the exceptions would typically be ones that have already been raised and caught by the program, along the following pattern:

```
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)
```

### 8.10. Enriching Exceptions with Notes

When an exception is created in order to be raised, it is usually initialized with information that describes the error that has occurred. There are cases where it is useful to add information after the exception was caught. For this purpose, exceptions have a method add_note(note) that accepts a string and adds it to the exception’s notes list. The standard traceback rendering includes all notes, in the order they were added, after the exception.

```
>>> try:
...     raise TypeError('bad type')
... except Exception as e:
...     e.add_note('Add some information')
...     e.add_note('Add some more information')
...     raise
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: bad type
Add some information
Add some more information
```

For example, when collecting exceptions into an exception group, we may want to add context information for the individual errors. In the following each exception in the group has a note indicating when this error has occurred.

```
>>> def f():
...     raise OSError('operation failed')
...
>>> excs = []
>>> for i in range(3):
...     try:
...         f()
...     except Exception as e:
...         e.add_note(f'Happened in Iteration {i+1}')
...         excs.append(e)
...
>>> raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 2
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 3
    +------------------------------------
>>>
```