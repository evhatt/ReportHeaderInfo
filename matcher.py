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
resources = re.compile("(from|join) \w+\.(\w+)", flags=re.IGNORECASE)
#print([ resources.findall(x) for x in merged])
match1 = [ resources.findall(x) for x in merged]
match1 = [x[0][1] for x in match1 if x != [] ] #grab captured table name
match1 = [x for x in match1 if x != ''] #remove nulls
match1 = list(set(match1)) #remove duplicates
match1.sort() #alphabatize

tempTable = re.compile("(?<=TEMP TABLE )\w+", flags=re.IGNORECASE)
match2 = [ tempTable.findall(x) for x in merged]
match2 = [x[0] for x in match2 if x != [] ]
match2 = list(set(match2))
match2.sort()

#checks items that are aliased. used to discard more false positives
#alias = re.compile("(?<=AS )\w+", flags=re.IGNORECASE)
#match3 = [ alias.findall(x) for x in merged]
#match3 = [x[0] for x in match3 if x != [] ]
#match3 = list(set(match3))
#match3.sort()

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
