def foo(name, **kwds):
    return "name" in kwds


# There is no possible call that will make it return True as the keyword
# 'name' will always bind to the first parameter. For example:

foo(1, **{"name": 2})

# Traceback (most recent call last):
#   File "D:\drs\Python\PythonTutorial_3.11\004_ControlFlow\021_positional_keywords_collision.py", line 8, in <module>
#     foo(1, **{"name": 2})
# TypeError: foo() got multiple values for argument 'name'
