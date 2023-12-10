# https://adventofcode.com/2022/day/4
file = open("input.txt", "r")
# file = open("test.txt", "r")



assignment  = file.read().split("\n")
# print(assignment)

assignmentPairs = list(map(lambda x: x.split(","), assignment))

pairsList = list(map(lambda x: list((i.split("-") for i in x)), assignmentPairs))

def pairs(lista):
    # print(lista)
    sum = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j] = int(lista[i][j])

    return isIn(lista[0], lista[1])


def isIn(a, b):
    if(a[0] >= b[0] and a[1] <= b[1]):
        return True    
    elif (b[0] >= a[0] and b[1] <= a[1]):
        return True
    else:
        return False


print(list(map(lambda x: pairs(x), pairsList)).count(True) )


# Part 2
"""
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
"""

def overlap(a, b):

    if (a[0] >= b[0] and b[1] <= a[1] and a[0] <= b[1] and b[1] >= a[0]):
        return True
    elif (b[0] >= a[0] and a[1] <= b[1] and b[0] <= a[1] and a[1] >= b[0]):
        return True
    else:
        return False

def pairsDouble(lista):
    # print(lista)
    sum = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j] = int(lista[i][j])

    return isIn(lista[0], lista[1]) or overlap(lista[0], lista[1])

print(list(map(lambda x: pairsDouble(x), pairsList)).count(True))