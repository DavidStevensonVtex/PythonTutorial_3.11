def concat(*args, sep="/"):
    return sep.join(args)


print('concat("earth", "mars", "venus")')
print(concat("earth", "mars", "venus"))

print('\nconcat("earth", "mars", "venus", sep=".")')
print(concat("earth", "mars", "venus", sep="."))

# concat("earth", "mars", "venus")
# earth/mars/venus

# concat("earth", "mars", "venus", sep=".")
# earth.mars.venus
