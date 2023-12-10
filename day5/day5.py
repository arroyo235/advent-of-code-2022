# https://adventofcode.com/2022/day/5

import re
import numpy as np

file = open("input.txt", "r")
# file = open("test.txt", "r")

stack_moves = file.read().split("\n\n")

stacks_input = stack_moves[0]
moves = stack_moves[1]

list_stacks = (stacks_input.split("\n")[-1].split("  "))
list_stacks = list(map(lambda x: int(x), list_stacks))


num_stacks = len(list_stacks)

def trim_row_crates(row):
    return re.findall("[A-Z]|\s\s\s\s", row)

row_crates = np.transpose(list(map(lambda x: trim_row_crates(x), stacks_input.split("\n")[:-1])))

crates_stack = list(map(lambda x : list(reversed(x)), row_crates))

class Stack:
    def __init__(self):
        self.crates = []

    def __init__(self, crates=[]):
        self.crates = crates

    def move_crates(self, num_crates, other_stack):
        # print("move ", num_crates, "from ", self.crates, " to ", other_stack.crates)
        for i in range(num_crates):
            crate = self.crates.pop()
            other_stack.crates.append(crate)
        # print("Reesult: ", self.crates, "and ", other_stack.crates)

    def move_crates_big(self, num_crates, other_stack):
        # print("move ", num_crates, "from ", self.crates, " to ", other_stack.crates)
        temp = []
        for i in range(num_crates):
            temp.append(self.crates.pop())
        temp.reverse()
        for i in temp:
            other_stack.crates.append(i)
        # print("Reesult: ", self.crates, "and ", other_stack.crates)

# print(num_stacks)
# print(crates_stack)

trim_stacks = [[x for x in sublist if x != '    '] for sublist in crates_stack]
# print(trim_stacks)
stacks = []

for i in trim_stacks:
    stacks.append(Stack(i))

# print("INIT STACKS")
# for i in stacks:
#     print(i.crates)

moves_simple = list(map(lambda x: re.findall("\d+", x), moves.split("\n")))
# print(moves_simple)
# move X from X to X
for move in moves_simple:
    stacks[int(move[1])-1].move_crates(int(move[0]), stacks[int(move[2])-1])
    

# print("END STACKS")
result = []
for i in stacks:
    a = i.crates[-1]
    result.append(a)
print("".join(result))


# PART 2
trim_stacks = [[x for x in sublist if x != '    '] for sublist in crates_stack]
stacks2 = []

for i in trim_stacks:
    stacks2.append(Stack(i))

for move in moves_simple:
    stacks2[int(move[1])-1].move_crates_big(int(move[0]), stacks2[int(move[2])-1])


result = []
for i in stacks2:
    a = i.crates[-1]
    result.append(a)
print("".join(result))