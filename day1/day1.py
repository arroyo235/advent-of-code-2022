# https://adventofcode.com/2022/day/1

file = open("input.txt", "r")

elvesString = file.read().split("\n\n")
elves = list(map(lambda x: list(map(lambda y: int(y), x.split())), elvesString))

elves_sum = list(map(lambda x: sum(x), elves))

# Part 1
max_calories = max(elves_sum)
print(max_calories)


# Part2
top_3 = sum(sorted(elves_sum, reverse=True)[:3])
print(top_3)