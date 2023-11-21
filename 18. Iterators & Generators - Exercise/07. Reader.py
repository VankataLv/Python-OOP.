def read_next(*args):
    for el in args:
        for it in el:
            yield f"{it}"


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print("\n---------------------")
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
