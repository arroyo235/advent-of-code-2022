# https://adventofcode.com/2022/day/2
file = open("input.txt", "r")

score = 0

lost = 0
draw = 3
win = 6

x = 1
y = 2
z = 3

roundsString = file.read().split("\n")

rules = {   "A X": draw+x, "A Y": win+y, "A Z": lost+z,
            "B X": lost+x, "B Y": draw+y, "B Z": win+z,
            "C X": win+x, "C Y": lost+y, "C Z": draw+z }
            
score = sum(list(map(lambda x: rules[x], roundsString)))

print(score)

# Part 2

score2 = 0
rules2 = {  "A X": lost+z, "A Y": draw+x, "A Z": win+y,
            "B X": lost+x, "B Y": draw+y, "B Z": win+z,
            "C X": lost+y, "C Y": draw+z, "C Z": win+x }

score2 = sum(list(map(lambda x: rules2[x], roundsString)))

print(score2)