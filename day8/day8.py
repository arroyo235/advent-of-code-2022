import numpy as np
# file = open("input.txt", "r")
file = open("input0.txt", "r")

lines = file.read().split("\n")

matriz = []
for i in lines:
    matriz.append([int(x) for x in i])

grid = np.array(matriz)
print(grid)

# grid_size = len(grid) * len(grid)
# grid_insize = (len(grid) - 2) * (len(grid) - 2)
# edge = grid_size - grid_insize  # Trees viseble on the edge
edge = len(grid) * 4  # Trees viseble on the edge
# print(edge)

visibles = []


def evalGrid(grid):
    # LEFT TO RIGHT
    temp_max = -1
    for i, tree in np.ndenumerate(grid):
        if (tree > temp_max and i not in visibles):  # and i not in visibles
            if (i not in visibles):
                # print("AÑADE LEFT TO RIGHT", i, tree)
                visibles.append(i)
            temp_max = tree
        if (i[1] == len(grid) - 1):  # nueva fila
            temp_max = -1

    # TOP TO BOTTOM
    # print()
    # print("TOP TO BOTTOM")
    temp_max = -1
    for i, tree in np.ndenumerate(grid):
        index = (i[1], i[0])
        tree = grid[index]
        # print(index)
        if (tree > temp_max):
            if (index not in visibles):
                # print("AÑADE TOP TO BOTTOM", index, tree)
                visibles.append(index)
            temp_max = tree
        if (i[1] == len(grid) - 1):  # nueva columna
            temp_max = -1

    # print()
    # print("RIGHT TO LEFT")
    # RIGHT TO LEFT
    temp_max = -1
    for i, tree in np.ndenumerate(grid):
        index = (i[0], len(grid) - i[1] - 1)
        tree = grid[index]
        # print(index)
        if (tree > temp_max):
            if (index not in visibles):
                # print("AÑADE RIGHT TO LEFT", index, tree)
                visibles.append(index)
            temp_max = tree
        if (i[1] == len(grid) - 1):
            temp_max = -1

    # BOTTOM TO RIGHT
    # print()
    # print("BOTTOM TO RIGHT")
    temp_max = -1
    for i, tree in np.ndenumerate(grid):
        index = (len(grid) - i[1] - 1, i[0])
        tree = grid[index]
        # print(index)
        if (tree > temp_max):
            if (index not in visibles):
                # print("AÑADE RIGHT TO LEFT", index, tree)
                visibles.append(index)
            temp_max = tree
        if (i[1] == len(grid) - 1):
            temp_max = -1


evalGrid(grid)


#PART 1
# print("Arboles visibles: ", sorted(visibles))
print("Arboles visibles: ", len(visibles)) #1854

#PART 2