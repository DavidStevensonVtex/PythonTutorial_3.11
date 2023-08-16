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