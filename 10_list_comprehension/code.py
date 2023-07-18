

names = ["Mansur", "Arif", 'Asif', "Asim", "Tahir"]

startsName = []

for name in names:
    if name.startswith("A"):
        startsName.append(name)

print(startsName)


# Short using

names = ["Mansur", "Arif", 'Asif', "Asim", "Tahir"]

startsName = [name for name in names if name.startswith("A")]


print(startsName)
