import re
f = open("report.txt")
report = f.read()
resources = re.compile("(^(?<=FROM )\w+|(?<=JOIN )\w+)", flags=re.IGNORECASE)
match1 = list(set(resources.findall(report)))
tempTable = re.compile("(?<=TEMP TABLE )\w+", flags=re.IGNORECASE)
match2 = list(set(tempTable.findall(report)))

print("Resources Used: ", end="")
for x in match1:
        if x not in match2:
                print(x + ", ", end="")

print("\n\nTemp Tables: ", end="")
if match2 == []:
        print("None")
else:
        for x in match2:
                print(x + ", ", end="")
