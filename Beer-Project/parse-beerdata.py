import csv


storeJSON = {}
lines = []

with open('beerglassData.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        lines.append(row)
        # print ', '.join(row)

# print lines

for a in lines:
    if a[1] not in storeJSON:
        storeJSON[a[1]] = []
        storeJSON[a[1]].append(a[2])
    else:
        storeJSON[a[1]].append(a[2])

# print storeJSON

lst = []

for a in storeJSON:
    # print a
    d = {}
    d["beerName"] = a
    d["glassType"] = storeJSON[a]
    lst.append(d)

print lst
