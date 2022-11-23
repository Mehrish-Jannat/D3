import csv
d1 = []
d2 = []
with open ("D1.csv","r") as f:
    read = csv.reader(f)
    for i in read :
        d1.append(i)
with open ("D2.csv","r") as f:
    read = csv.reader(f)
    for i in read :
        d2.append(i)
h1 = d1[0]
data1 = d1[1:]
h2 = d2[0]
data2 = d2[1:]
h = h1 + h2
data = []
for i, j in enumerate(d1):
    data.append(d1[i]+d2[i])

with open("merged.csv","a+") as f :
    write = csv.writer(f)
    write.writerow(h)
    write.writerows(data)

