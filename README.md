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

## 9. Classes

Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

### 9.1. A Word About Names and Objects

Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is usually used to the benefit of the program, since aliases behave like pointers in some respects. For example, passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change.

### 9.2. Python Scopes and Namespaces

A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries.

By the way, I use the word attribute for any name following a dot — for example, in the expression z.real, real is an attribute of the object z. 

Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer from the object named by modname.

Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits. 

The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function.

Scopes:

* the innermost scope, which is searched first, contains the local names
* the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names
* the next-to-last scope contains the current module’s global names
* the outermost scope (searched last) is the namespace containing built-in names

It is important to realize that scopes are determined textually: the global scope of a function defined in a module is that module’s namespace, no matter from where or by what alias the function is called. On the other hand, the actual search for names is done dynamically, at run time — however, the language definition is evolving towards static name resolution, at “compile” time, so don’t rely on dynamic name resolution! (In fact, local variables are already determined statically.)

A special quirk of Python is that – if no [global](https://docs.python.org/3/reference/simple_stmts.html#global) or [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for deletions: the statement del x removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, [import](https://docs.python.org/3/reference/simple_stmts.html#import) statements and function definitions bind the module or function name in the local scope.

The [global](https://docs.python.org/3/reference/simple_stmts.html#global) statement can be used to indicate that particular variables live in the global scope and should be rebound there; the [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement indicates that particular variables live in an enclosing scope and should be rebound there.

#### 9.2.1. Scopes and Namespaces Example

```
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

The output of the example code is:

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam  
In global scope: global spam
```

### 9.3. A First Look at Classes

#### 9.3.1. Class Definition Syntax

The simplest form of class definition looks like this:

```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Class definitions, like function definitions (def statements) must be executed before they have any effect. (You could conceivably place a class definition in a branch of an if statement, or inside a function.)

In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed, and sometimes useful — we’ll come back to this later. The function definitions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods — again, this is explained later.

When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

When a class definition is left normally (via the end), a class object is created. This is basically a wrapper around the contents of the namespace created by the class definition; we’ll learn more about class objects in the next section. The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class object is bound here to the class name given in the class definition header (ClassName in the example).

#### 9.3.2. Class Objects

Class objects support two kinds of operations: attribute references and instantiation.

_Attribute references_ use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class’s namespace when the class object was created. So, if the class definition looked like this:

```
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

then MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively. Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment. \_\_doc\_\_ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):

```x = MyClass()```

creates a new instance of the class and assigns this object to the local variable x.

The instantiation operation (“calling” a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named \_\_init\_\_(), like this:

```
def __init__(self):
    self.data = []
```

When a class defines an \_\_init\_\_() method, class instantiation automatically invokes \_\_init\_\_() for the newly created class instance. So in this example, a new, initialized instance can be obtained by:

```x = MyClass()```

Of course, the \_\_init\_\_() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to \_\_init\_\_(). For example,

```
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

#### 9.3.3. Instance Objects

Now what can we do with instance objects? The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.

data attributes correspond to “instance variables” in Smalltalk, and to “data members” in C++. Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to. For example, if x is the instance of MyClass created above, the following piece of code will print the value 16,
without leaving a trace:

```
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

The other kind of instance attribute reference is a method. A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on. However, in the following discussion, we’ll use the term method exclusively to mean methods of class instance objects, unless explicitly stated otherwise.)

Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances. So in our example, x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not. But x.f is not the same thing as MyClass.f — it is a method object, not a function object.

#### 9.3.4. Method Objects

Usually, a method is called right after it is bound:

```x.f()```

In the MyClass example, this will return the string 'hello world'. However, it is not necessary to call a method right away: x.f is a method object, and can be stored away and called at a later time. For example:

```
xf = x.f
while True:
    print(xf())
```

will continue to print hello world until the end of time.

What exactly happens when a method is called? You may have noticed that x.f() was called without an argument above, even though the function definition for f() specified an argument. What happened to the argument? Surely Python raises an exception when a function that requires an argument is called without any — even if the argument isn’t actually used…

Actually, you may have guessed the answer: the special thing about methods is that the instance object is passed as the first argument of the function. In our example, the call x.f() is exactly equivalent to MyClass.f(x). In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.

If you still don’t understand how methods work, a look at the implementation can perhaps clarify matters. When a non-data attribute of an instance is referenced, the instance’s class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: this is the method object. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

#### 9.3.5. Class and Instance Variables

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:

```
class Dog:
    kind = "canine"  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


d = Dog("Fido")
e = Dog("Buddy")
print("d.kind", d.kind)  # shared by all dogs
print("e.kind", e.kind)  # shared by all dogs
print("d.name", d.name)  # unique to d
print("e.name", e.name)  # unique to e

# d.kind canine
# e.kind canine
# d.name Fido
# e.name Buddy
```

As discussed in [A Word About Names and Objects](https://docs.python.org/3/tutorial/classes.html#tut-object), shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries. For example, the tricks list in the following code should not be used as a class variable because just a single list would be shared by all Dog instances:

```
class Dog:
    tricks = []  # mistaken use of a class variable

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")

print("d.tricks", d.tricks)  # unexpectedly shared by all dogs
# d.tricks ['roll over', 'play dead']
```

Correct design of the class should use an instance variable instead:

```
class Dog:
    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")

print("d.tricks", d.tricks)
print("e.tricks", e.tricks)

# d.tricks["roll over"]
# e.tricks["play dead"]

```

### 9.4. Random Remarks

If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:

```
class Warehouse:
    purpose = "storage"
    region = "west"


w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = "east"
print(w2.purpose, w2.region)

# storage west
# storage east
```

Data attributes may be referenced by methods as well as by ordinary users (“clients”) of an object. In other words, classes are not usable to implement pure abstract data types. In fact, nothing in Python makes it possible to enforce data hiding — it is all based upon convention. (On the other hand, the Python implementation, written in C, can completely hide implementation details and control access to an object if necessary; this can be used by extensions to Python written in C.)

Clients should use data attributes with care — clients may mess up invariants maintained by the methods by stamping on their data attributes. Note that clients may add data attributes of their own to an instance object without affecting the validity of the methods, as long as name conflicts are avoided — again, a naming convention can save a lot of headaches here.

There is no shorthand for referencing data attributes (or other methods!) from within methods. I find that this actually increases the readability of methods: there is no chance of confusing local variables and instance variables when glancing through a method.

Often, the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.

Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:

```
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

Now f, g and h are all attributes of class C that refer to function objects, and consequently they are all methods of instances of C — h being exactly equivalent to g. Note that this practice usually only serves to confuse the reader of a program.

Methods may call other methods by using method attributes of the self argument:

```
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing its definition. (A class is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually, the class containing the method is itself defined in this global scope, and in the next section we’ll find some good reasons why a method would want to reference its own class.

Each value is an object, and therefore has a class (also called its type). It is stored as object.\_\_class\_\_.

### 9.5. Inheritance

Of course, a language feature would not be worthy of the name “class” without supporting inheritance. The syntax for a derived class definition looks like this:

```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

The name BaseClassName must be defined in a scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

```class DerivedClassName(modname.BaseClassName):```

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

There’s nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class. Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (For C++ programmers: all methods in Python are effectively virtual.)

An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)

Python has two built-in functions that work with inheritance:

* Use [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) to check an instance’s type: isinstance(obj, int) will be True only if obj.\_\_class\_\_ is int or some class derived from int.

* Use [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

### 9.5.1. Multiple Inheritance

Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to [super()](https://docs.python.org/3/library/functions.html#super). This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (where at least one of the parent classes can be accessed through multiple paths from the bottommost class). For example, all classes inherit from object, so any case of multiple inheritance provides more than one path to reach object. To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic (meaning that a class can be subclassed without affecting the precedence order of its parents). Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance. For more detail, see https://www.python.org/download/releases/2.3/mro/.

### 9.6. Private Variables

“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:

```
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

The above example would work even if MappingSubclass were to introduce a __update identifier since it is replaced with _Mapping__update in the Mapping class and _MappingSubclass__update in the MappingSubclass class respectively.

Note that the mangling rules are designed mostly to avoid accidents; it still is possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current class; this is similar to the effect of the global statement, the effect of which is likewise restricted to code that is byte-compiled together. The same restriction applies to getattr(), setattr() and delattr(), as well as when referencing \_\_dict\_\_ directly.

### 9.7. Odds and Ends

Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items. The idiomatic approach is to use [dataclasses](https://docs.python.org/3/library/dataclasses.html#module-dataclasses) for this purpose:

```
>>> from dataclasses import dataclass
>>> 
>>> @dataclass
... class Employee:
...     name: str
...     dept: str
...     salary: int
... 
>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
```

A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead. For instance, if you have a function that formats some data from a file object, you can define a class with methods [read()](https://docs.python.org/3/library/io.html#io.TextIOBase.read) and [readline()](https://docs.python.org/3/library/io.html#io.TextIOBase.readline) that get the data from a string buffer instead, and pass it as an argument.

Instance method objects have attributes, too: m.\_\_self\_\_ is the instance object with the method m(), and m.\_\_func\_\_ is the function object corresponding to the method.

### 9.8. Iterators

By now you have probably noticed that most container objects can be looped over using a for statement:

```
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {"one": 1, "two": 2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end="")

# 1
# 2
# 3
# 1
# 2
# 3
# one
# two
# 1
# 2
# 3
# The rain in Spain falls mainly in the plain.
# As they say in Finland, there's more than one way to roast a reindeer.
# You can see a lot just by looking.
```

This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls [iter()](https://docs.python.org/3/library/functions.html#iter) on the container object. The function returns an iterator object that defines the method [\_\_next\_\_()](https://docs.python.org/3/library/stdtypes.html#iterator.__next__) which accesses elements in the container one at a time. When there are no more elements, [\_\_next\_\_()](https://docs.python.org/3/library/stdtypes.html#iterator.__next__) raises a [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration) exception which tells the for loop to terminate. You can call the [\_\_next\_\_()](https://docs.python.org/3/library/stdtypes.html#iterator.__next__) method using the next() built-in function; this example shows how it all works:

```
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_ascii_iterator object at 0x00000249D08877F0>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes. Define an [\_\_iter\_\_()](https://docs.python.org/3/library/stdtypes.html#container.__iter__) method which returns an object with a [\_\_next\_\_()](https://docs.python.org/3/library/stdtypes.html#iterator.__next__) method. If the class defines [\_\_next\_\_()](https://docs.python.org/3/library/stdtypes.html#iterator.__next__), then __iter__() can just return self:

```
class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse("spam")
print("iter(rev)", iter(rev))
for char in rev:
    print(char)

# iter(rev) <__main__.Reverse object at 0x0000026B62773B10>
# m
# a
# p
# s
```

### 9.9. Generators

[Generators](https://docs.python.org/3/glossary.html#term-generator) are a simple and powerful tool for creating iterators. They are written like regular functions but use the [yield](https://docs.python.org/3/reference/simple_stmts.html#yield) statement whenever they want to return data. Each time [next()](https://docs.python.org/3/library/functions.html#next) is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example shows that generators can be trivially easy to create:

```
>>> def reverse(data):
...     for index in range(len(data)-1, -1, -1):
...         yield data[index]
...
>>> for char in reverse('golf'):
...     print(char)
... 
f
l
o
g
```

Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the [\_\_iter\_\_()](https://docs.python.org/3/library/stdtypes.html#iterator.__iter__) and [\_\_next\_\_()](https://docs.python.org/3/reference/expressions.html#generator.__next__) methods are created automatically.

Another key feature is that the local variables and execution state are automatically saved between calls. This made the function easier to write and much more clear than an approach using instance variables like self.index and self.data.

In addition to automatic method creation and saving program state, when generators terminate, they automatically raise [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration). In combination, these features make it easy to create iterators with no more effort than writing a regular function.

### 9.10. Generator Expressions

Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

```
sum(i*i for i in range(10))                 # sum of squares
285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```

## 10. Brief Tour of the Standard Library

### 10.1. Operating System Interface

The [os](https://docs.python.org/3/library/os.html#module-os) module provides dozens of functions for interacting with the operating system:

```
>>> import os
>>> os.getcwd()             # Return the current working directory
'D:\\drs\\Python\\PythonTutorial_3.11\\010_BriefTourOfTheStandardLibrary'
>>> os.chdir('D:\\drs\\Python\\PythonTutorial_3.11\\010_BriefTourOfTheStandardLibrary')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

Be sure to use the import os style instead of from os import *. This will keep os.open() from shadowing the built-in open() function which operates much differently.

The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:

```
import os
dir(os)
help(os)
```

For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use:

```
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
```

### 10.2. File Wildcards

The [glob](https://docs.python.org/3/library/glob.html#module-glob) module provides a function for making file lists from directory wildcard searches:

```
import glob
glob.glob('*.py')
```

### 10.3. Command Line Arguments

Common utility scripts often need to process command line arguments. These arguments are stored in the [sys](https://docs.python.org/3/library/sys.html#module-sys) module’s argv attribute as a list. For instance the following output results from running python demo.py one two three at the command line:

$ python demo.py one two three
```
import sys

print(sys.argv)

# ['demo.py', 'one', 'two', 'three']
```

The [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) module provides a more sophisticated mechanism to process command line arguments. The following script extracts one or more filenames and an optional number of lines to be displayed:

```
import argparse

parser = argparse.ArgumentParser(
    prog="top", description="Show top lines from each file"
)
parser.add_argument("filenames", nargs="+")
parser.add_argument("-l", "--lines", type=int, default=10)
args = parser.parse_args()
print(args)
```

When run at the command line with python top.py --lines=5 alpha.txt beta.txt, the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].

### 10.4. Error Output Redirection and Program Termination

The [sys](https://docs.python.org/3/library/sys.html#module-sys) module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warnings and error messages to make them visible even when stdout has been redirected:

```
>>> import sys
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

The most direct way to terminate a script is to use __sys.exit()__.

### 10.5. String Pattern Matching

The [re](https://docs.python.org/3/library/re.html#module-re) module provides regular expression tools for advanced string processing. 
For complex matching and manipulation, regular expressions offer succinct, optimized solutions:

```
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:

```
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

### 10.6. Mathematics

The [math](https://docs.python.org/3/library/math.html#module-math) module gives access to the underlying C library functions for floating point math:

```
>>> import math
>>> math.cos(math.pi / 4)
0.7071067811865476
>>> math.log(1024, 2)
10.0
```

The [random](https://docs.python.org/3/library/random.html#module-random) module provides tools for making random selections:

<pre>
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[87, 76, 51, 30, 11, 75, 68, 96, 46, 37]
>>> random.random()                 # random float
0.6042513502100706
>>> random.randrange(6)             # random integer chosen from range(6)
5
</pre>

The [statistics](https://docs.python.org/3/library/statistics.html#module-statistics) module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

```
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

The SciPy project <https://scipy.org> has many other modules for numerical computations.

### 10.7. Internet Access

There are a number of modules for accessing the internet and processing internet protocols. 
Two of the simplest are [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) 
for retrieving data from URLs and smtplib for sending mail:

```
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline
```

```
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
```

(Note that the second example needs a mailserver running on localhost.)

### 10.8. Dates and Times

The [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. The module also supports objects that are timezone aware.

```
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2023, 9, 5)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'09-05-23. 05 Sep 2023 is a Tuesday on the 05 day of September.'
>>>
>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
21585
```

### 10.9. Data Compression
Common data archiving and compression formats are directly supported by modules including: 

* [zlib](https://docs.python.org/3/library/zlib.html#module-zlib)
* [gzip](https://docs.python.org/3/library/gzip.html#module-gzip)
* [bz2](https://docs.python.org/3/library/bz2.html#module-bz2)
* [lzma](https://docs.python.org/3/library/lzma.html#module-lzma)
* [zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile)
* [tarfile](https://docs.python.org/3/library/tarfile.html#module-tarfile)

```
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

### 10.10. Performance Measurement

Some Python users develop a deep interest in knowing the relative performance of different approaches to the same problem. Python provides a measurement tool that answers those questions immediately.

For example, it may be tempting to use the tuple packing and unpacking feature instead of the traditional approach to swapping arguments. 
The [timeit](https://docs.python.org/3/library/timeit.html#module-timeit) module quickly demonstrates a modest performance advantage:


```
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.05515559995546937
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.038036399986594915
```

In contrast to [timeit](https://docs.python.org/3/library/timeit.html#module-timeit)’s fine level of granularity, 
the [profile](https://docs.python.org/3/library/profile.html#module-profile) 
and [pstats](https://docs.python.org/3/library/profile.html#module-pstats) modules 
provide tools for identifying time critical sections in larger blocks of code.

### 10.11. Quality Control
One approach for developing high quality software is to write tests for each function as it is developed and to run those tests frequently during the development process.

The [doctest](https://docs.python.org/3/library/doctest.html#module-doctest) module provides a tool for scanning a module and validating tests embedded in a program’s docstrings. Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. This improves the documentation by providing the user with an example and it allows the doctest module to make sure the code remains true to the documentation:

```
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

The [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be maintained in a separate file:

```
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

### 10.12. Batteries Included
Python has a “batteries included” philosophy. This is best seen through the sophisticated and robust capabilities of its larger packages. For example:

* The [xmlrpc.client](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client) 
and [xmlrpc.server](https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server) modules 
make implementing remote procedure calls into an almost trivial task. Despite the modules’ names, no direct knowledge or handling of XML is needed.

* The [email](https://docs.python.org/3/library/email.html#module-email) package is a library for managing email messages, including MIME and other [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822.html)-based message documents. Unlike [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) and [poplib](https://docs.python.org/3/library/poplib.html#module-poplib) which actually send and receive messages, the email package has a complete toolset for building or decoding complex message structures (including attachments) and for implementing internet encoding and header protocols.

* The [json](https://docs.python.org/3/library/json.html#module-json) package provides robust support for parsing this popular data interchange format. 
The [csv](https://docs.python.org/3/library/csv.html#module-csv) module supports direct reading and writing of files in Comma-Separated Value format, commonly supported by databases and spreadsheets. 
XML processing is supported by the [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree), 
[xml.dom](https://docs.python.org/3/library/xml.dom.html#module-xml.dom) and 
[xml.sax](https://docs.python.org/3/library/xml.sax.html#module-xml.sax) packages. Together, these modules and packages greatly simplify data interchange between Python applications and other tools.

* The [sqlite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) module is a wrapper for the SQLite database library, providing a persistent database that can be updated and accessed using slightly nonstandard SQL syntax.

* Internationalization is supported by a number of modules including [gettext](https://docs.python.org/3/library/gettext.html#module-gettext), 
[locale](https://docs.python.org/3/library/locale.html#module-locale), and 
the [codecs](https://docs.python.org/3/library/codecs.html#module-codecs) package.

## 11. Brief Tour of the Standard Library -- Part II

This second tour covers more advanced modules that support professional programming needs. These modules rarely occur in small scripts.

### 11.1 Output Formatting

The [reprlib](https://docs.python.org/3/library/reprlib.html#module-reprlib) module provides a version of 
[repr()](https://docs.python.org/3/library/functions.html#repr) customized for abbreviated displays of large or deeply nested containers:

```
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
```
<pre>"{'a', 'c', 'd', 'e', 'f', 'g', ...}"</pre>


The [pprint](https://docs.python.org/3/library/pprint.html#module-pprint) module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter. When the result is longer than one line, the “pretty printer” adds line breaks and indentation to more clearly reveal data structure:

```
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)
```
<pre>
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
</pre>

The textwrap module formats paragraphs of text to fit a given screen width:

```
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
```
<pre>The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
</pre>

The [locale](https://docs.python.org/3/library/locale.html#module-locale) module accesses a database of culture specific data formats. The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators:

```
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> 'English_United States.1252'
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
<stdin>:1: DeprecationWarning: This method will be removed in a future version of Python. Use 'locale.format_string()' instead.
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

### 11.2. Templating

The [string](https://docs.python.org/3/library/string.html#module-string) module includes a versatile [Template](https://docs.python.org/3/library/string.html#string.Template) class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.

The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces. Writing $$ creates a single escaped $:

```
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

The [substitute()](https://docs.python.org/3/library/string.html#string.Template.substitute) method raises a [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError) when a placeholder is not supplied in a dictionary or a keyword argument. For mail-merge style applications, user supplied data may be incomplete and the [safe_substitute()](https://docs.python.org/3/library/string.html#string.Template.safe_substitute) method may be more appropriate — it will leave placeholders unchanged if data is missing:

```
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Program Files\Python311\Lib\string.py", line 121, in substitute
    return self.pattern.sub(convert, self.template)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\string.py", line 114, in convert
    return str(mapping[named])
               ~~~~~~~^^^^^^^
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

Template subclasses can specify a custom delimiter. For example, a batch renaming utility for a photo browser may elect to use percent signs for placeholders such as the current date, image sequence number, or file format:

```
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

### 11.3. Working with Binary Data Record Layouts

The [struct](https://docs.python.org/3/library/struct.html#module-struct) module provides [pack()](https://docs.python.org/3/library/struct.html#struct.pack) and [unpack()](https://docs.python.org/3/library/struct.html#struct.unpack) functions for working with variable length binary record formats. The following example shows how to loop through header information in a ZIP file without using the [zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile) module. Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. The "<" indicates that they are standard size and in little-endian byte order:

```
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

### 11.4. Multi-threading

Threading is a technique for decoupling tasks which are not sequentially dependent. Threads can be used to improve the responsiveness of applications that accept user input while other tasks run in the background. A related use case is running I/O in parallel with computations in another thread.

The following code shows how the high level [threading](https://docs.python.org/3/library/threading.html#module-threading) module can run tasks in background while the main program continues to run:

```
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. To that end, the threading module provides a number of synchronization primitives including locks, events, condition variables, and semaphores.

While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. So, the preferred approach to task coordination is to concentrate all access to a resource in a single thread and then use the [queue](https://docs.python.org/3/library/queue.html#module-queue) module to feed that thread with requests from other threads. Applications using [Queue](https://docs.python.org/3/library/queue.html#queue.Queue) objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.

### 11.5. Logging

The [logging](https://docs.python.org/3/library/logging.html#module-logging) module offers a full featured and flexible logging system. At its simplest, log messages are sent to a file or to sys.stderr:

```
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

By default, informational and debugging messages are suppressed and the output is sent to standard error. Other output options include routing messages through email, datagrams, sockets, or to an HTTP Server. New filters can select different routing based on message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

The logging system can be configured directly from Python or can be loaded from a user editable configuration file for customized logging without altering the application.

### 11.6. Weak References

Python does automatic memory management (reference counting for most objects and [garbage collection](https://docs.python.org/3/glossary.html#term-garbage-collection) to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.

This approach works fine for most applications but occasionally there is a need to track objects only as long as they are being used by something else. Unfortunately, just tracking them creates a reference that makes them permanent. The [weakref](https://docs.python.org/3/library/weakref.html#module-weakref) module provides tools for tracking objects without creating a reference. When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects. Typical applications include caching objects that are expensive to create:

### 11.7. Tools for Working with Lists

Many data structure needs can be met with the built-in list type. However, sometimes there is a need for alternative implementations with different performance trade-offs.

The array module provides an [array()](https://docs.python.org/3/library/array.html#array.array) object that is like a list that stores only homogeneous data and stores it more compactly. The following example shows an array of numbers stored as two byte unsigned binary numbers (typecode "H") rather than the usual 16 bytes per entry for regular lists of Python int objects:

```
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

The [collections](https://docs.python.org/3/library/collections.html#module-collections) module provides a [deque()](https://docs.python.org/3/library/collections.html#collections.deque) object that is like a list with faster appends and pops from the left side but slower lookups in the middle. These objects are well suited for implementing queues and breadth first tree searches:

```
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```

In addition to alternative list implementations, the library also offers other tools such as the [bisect](https://docs.python.org/3/library/bisect.html#module-bisect) module with functions for manipulating sorted lists:

The heapq module provides functions for implementing heaps based on regular lists. The lowest valued entry is always kept at position zero. This is useful for applications which repeatedly access the smallest element but do not want to run a full list sort:

### 11.8. Decimal Floating Point Arithmetic

The [decimal](https://docs.python.org/3/library/decimal.html#module-decimal) module offers a [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal) datatype for decimal floating point arithmetic. Compared to the built-in float implementation of binary floating point, the class is especially helpful for

* financial applications and other uses which require exact decimal representation,
* control over precision,
* control over rounding to meet legal or regulatory requirements,
* tracking of significant decimal places, or
* applications where the user expects the results to match calculations done by hand.









### [os](https://docs.python.org/3/library/os.html#module-os) module

### [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) module

### [sys](https://docs.python.org/3/library/sys.html#module-sys) module

### [glob](https://docs.python.org/3/library/glob.html#module-glob) module

### [re](https://docs.python.org/3/library/re.html#module-re) module

### [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) module
