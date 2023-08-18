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
