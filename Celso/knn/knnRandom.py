''' 
Celso Antonio - August 2019 
'''

import matplotlib.pyplot as plt
import csv
import math
import random

def euclideanDistance(xa, ya, xb, yb):
    return math.sqrt(((xa - xb) ** 2) + ((ya - yb) ** 2 ))

data = list()

with open('dataset.csv', newline='') as csvfile:
    data = list(csv.DictReader(csvfile))

k = 1
newCoords = list()

x = list()
y = list()
z = list()

for i in range(1000):
    newCoords.append([random.randint(1,101), random.randint(1,101)])
    
for newObj in newCoords:

    eucliDist = list()

    for obj in list(data):
        eucliDist.append((euclideanDistance(newObj[0], newObj[1], int(obj['X']), int(obj['Y'])), int(obj['id'])))

    eucliDist.sort(key = lambda x: x[0])

    classifier = {}

    for i in range(k):
        for obj in data:
            if(int(obj['id']) == eucliDist[i][1]):
                if not obj['Class'] in classifier:
                    classifier[obj['Class']] = 1
                else:   
                    classifier[obj['Class']] += 1  

    a = 0
    cClass = ''

    for key in classifier:
        if(classifier[key] > a):
            a = classifier[key]
            cClass = key

    print('Classified as Class ' +  cClass)
    print('New classified coords added to the dataset')

    data.append({'id': len(data) + 1, 'X': newObj[0], 'Y': newObj[1], 'Class': cClass})

    x.append(int(newObj[0]))
    y.append(int(newObj[1]))
    z.append(cClass)

for obj in data:
    x.append(int(obj['X']))
    y.append(int(obj['Y']))
    z.append(obj['Class'])

plt.scatter(x, y, c=z)
plt.show()
'''
myCsvRow = '' + str(len(data) + 1) + ',' + str(newObj[0]) + ',' + str(newObj[1]) + ',' + cClass
with open('dataset.csv','a') as fd:
    fd.write(myCsvRow + "\n")
'''