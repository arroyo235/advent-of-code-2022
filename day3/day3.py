# https://adventofcode.com/2022/day/3
file = open("input.txt", "r")

rucksackFull = file.read().split("\n")
# print(rucksackFull)

rucksack = list(map(lambda x : [x[:int(len(x)/2)], x[int(len(x)/2):]], rucksackFull))
# print(rucksack)

d = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
    'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
    'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42,
    'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50,
    'Y': 51, 'Z': 52
}

sum = 0
for i, j in rucksack:
    sum += d[list(set(i).intersection(set(j)))[0]]

print(sum)

# Part 2

# Divide a list into sublists with 3 elements each
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sublists = list()
# for i in range(0, len(rucksackFull), 3):
#     sublists.append(rucksackFull[i:i + 3])

# print(sublists)
# Divide a list into sublists with 3 elements each using the zip() function
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sublists = [list(sublist) for sublist in zip(*[iter(rucksackFull)] * 3)]
# print(sublists)

sum = 0
for i, j, k in sublists:
    sum += d[list(set(i).intersection(set(j).intersection(set(k))))[0]]

print(sum)
