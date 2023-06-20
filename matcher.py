import re

def selector(a, b):
        c = []
        for x in range(len(a)):
                if b[x] != []:
                        c.append(b[x][0])
                else:
                        c.append(a[x])
        return c

#parse file and delete in line comments
#this will cause an issue if strings in the report have a double dash sequence
f = open("report.txt")
report = f.read()
delineated = report.split(sep="\n")
nocomment = re.compile("(.+)--")
commentFree = [nocomment.findall(x) for x in delineated ]
merged = selector(delineated, commentFree)

#compile the regular expressions and use list comprehension to iterate and match
resources = re.compile("((?<=FROM )\w+|(?<=JOIN )\w+)", flags=re.IGNORECASE)
match1 = [ resources.findall(x) for x in merged]
match1 = [x[0] for x in match1 if x != [] ]

tempTable = re.compile("(?<=TEMP TABLE )\w+", flags=re.IGNORECASE)
match2 = [ tempTable.findall(x) for x in merged]
match2 = [x[0] for x in match2 if x != [] ]

print("Resources Used: ", end="")
for i, x in enumerate(match1):
        if x not in match2:
                if i:
                        print(", ", end='')
                print(x, end="")

print("\n\nTemp Tables: ", end="")
if match2 == []:
        print("None")
else:
        for i, x in enumerate(match2):
                if i:
                        print(", ", end="")
                print(x, end="")
