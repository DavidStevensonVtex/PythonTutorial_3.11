def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


print("\nstandard_arg(2)")
standard_arg(2)
# 2

print("\nstandard_arg(arg=2)")
standard_arg(arg=2)
# 2

print("\npos_only_arg(1)")
pos_only_arg(1)
# 1

print("\npos_only_arg(arg=1)")
try:
    pos_only_arg(arg=1)
except TypeError:
    print("positional-only arguments passed as keyword arguments: 'arg'")

print("\nkwd_only_arg(3)")
try:
    kwd_only_arg(3)
except TypeError:
    print("kwd_only_arg() takes 0 positional arguments but 1 was given")

print("\ncombined_example(1, 2, 3)")
try:
    combined_example(1, 2, 3)
except:
    print("TypeError: combined_example() takes 2 positional arguments but 3 were given")

print("\ncombined_example(1, 2, kwd_only=3)")
combined_example(1, 2, kwd_only=3)

print("\ncombined_example(1, standard=2, kwd_only=3)")
combined_example(1, standard=2, kwd_only=3)

print("\ncombined_example(pos_only=1, standard=2, kwd_only=3)")
try:
    combined_example(pos_only=1, standard=2, kwd_only=3)
except TypeError:
    print(
        "TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'"
    )
