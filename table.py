data = [['1', '2', '3'],
        ['2', '4', '6'],
        ['3', '6', '9']]
longests = []
for x in range(len(data)):
    longests.append(0)
    for y in data[x]:
        if len(y) > longests[x]:
            longest = len(y)

print(longests)
