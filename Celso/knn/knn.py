''' 
Celso Antonio - August 2019 
'''

import csv
import math

def euclideanDistance(xa, ya, xb, yb):
    return math.sqrt(((xa - xb) ** 2) + ((ya - yb) ** 2 ))

data = list()

with open('dataset.csv', newline='') as csvfile:
    data = list(csv.DictReader(csvfile))

print('Insert a odd number greater than one(3,5,7.. for example)')
k = int(input())

if(k % 2 == 0):
    print('Not odd number')
    exit()

print('Insert coord X, Coord Y')
newObj = list(map(int, input().split()))

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

myCsvRow = '' + str(len(data) + 1) + ',' + str(newObj[0]) + ',' + str(newObj[1]) + ',' + cClass

with open('dataset.csv','a') as fd:
    fd.write(myCsvRow + "\n")
