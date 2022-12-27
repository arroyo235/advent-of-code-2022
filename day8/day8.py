import numpy as np
file = open("input.txt", "r")
# file = open("input0.txt", "r")

lines = file.read().split("\n")

matriz = []
for i in lines:
    matriz.append([int(x) for x in i])

grid = np.array(matriz)
# print(grid)    

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



#PART 1
evalGrid(grid)
# print("Arboles visibles: ", sorted(visibles))
print("Arboles visibles: ", len(visibles)) #1854


#PART 2
def dict_initialize(grid):
    visibles_trees = {}
    for i, j in np.ndenumerate(grid):
        visibles_trees[i] = [[], [], [], []]
    return visibles_trees


def count_visible_trees(grid):
    global visibles_trees

    # LOOK TO THE RIGHT
    num = 0
    for i, tree in np.ndenumerate(grid):
        # print(i, tree)
        index = i
        if (i[1] == len(grid) - 2):  # cuando llega al penultimo elemento para recorrer, añade solo el de la derecha
                # print("Añade al penultimo", grid[i[0], i[1]+1])
                visibles_trees[index][num].append(grid[i[0], i[1]+1])
        else:        
            t = i[1] + 1 # t es para recorrer la elementos de la fila de cada numero, empieza por la posicion de la derecha
            max_tree = -1
            while (t <= len(grid)-1): # 1 (t) -> 4 (5-1)
                right_tree = grid[i[0], t]
                if(right_tree >= tree):
                    # print("Añade por que ", right_tree, ">= ", tree)
                    visibles_trees[index][num].append(right_tree) # añade 
                    break
                else:
                    # print("Añade",right_tree,"y continua")
                    visibles_trees[index][num].append(right_tree) # añade 
                t += 1
        
    print()

    # LOOK TO THE LEFT
    num = 1
    for i, tree in np.ndenumerate(grid):
        index = (i[0], len(grid)-i[1]-1)
        tree = grid[index]
        # print(index, tree)
        if (index[1] == 1):  # cambiar
                # print("Añade al penultimo", grid[index[0], index[1]-1])
                visibles_trees[index][num].append(grid[index[0], index[1]-1]) # cambiar
        else:      
            max_tree = -1
            t = index[1] - 1 # cambiado
            while (t >= 0): # 1 (t) -> 4 (5-1) cambiado
                left_tree = grid[index[0], t]
                if(left_tree >= tree):
                    # print("Añade por que ", left_tree, ">= ", tree)
                    visibles_trees[index][num].append(left_tree) # añade 
                    # print("break")
                    break
                else:
                    # print("Añade",left_tree,"y continua")
                    visibles_trees[index][num].append(left_tree) # añade 
                t -= 1

    # print()
    # LOOK TO THE BOTTOM
    num = 2
    for i, tree in np.ndenumerate(grid):
        index = (i[1], i[0]) # cambiar
        tree = grid[index]
        # print(index, tree)
        if (index[0] == len(grid) - 2):  # cambiar
                # print("Añade al penultimo", grid[index[0]+1, index[1]])
                visibles_trees[index][num].append(grid[index[0]+1, index[1]]) # cambiar
        else:        
            max_tree = -1
            t = index[0] + 1 # cambiar
            while (t <= len(grid)-1): # 1 (t) -> 4 (5-1) cambiar
                bottom_tree = grid[t, index[1]] # cambiar
                if(bottom_tree >= tree):
                    # print("Añade por que ", bottom_tree, ">= ", tree)
                    visibles_trees[index][num].append(bottom_tree) # añade 
                    # print("break")
                    break
                else:
                    # print("Añade",bottom_tree, index,"y continua")
                    visibles_trees[index][num].append(bottom_tree) # añade 
                t += 1
        
    # print()   
        
    # LOOK TO THE TOP
    num = 3
    for i, tree in np.ndenumerate(grid):
        index = (len(grid)-i[1]-1, i[0]) # cambiar
        tree = grid[index]
        # print(index, tree)
        if (index[0] == 1):  # cambiado
                # print("Añade al penultimo", grid[index[0]-1, index[1]])
                visibles_trees[index][num].append(grid[index[0]-1, index[1]]) # cambiado
        else:        
            max_tree = -1
            t = index[0] - 1 # cambiar
            while (t >= 0): # 1 (t) -> 4 (5-1) cambiar
                top_tree = grid[t, index[1]] # cambiar
                if(top_tree >= tree):
                    visibles_trees[index][num].append(top_tree) # añade 
                    break
                else:
                    visibles_trees[index][num].append(top_tree) # añade 
                t -= 1
            
            
visibles_trees = dict_initialize(grid)
count_visible_trees(grid)

# print()
# for k, v in visibles_trees.items():
#     print(k, v)
    
# for k, v in visibles_trees.items():
#     print(k, [np.prod([len(s) for s in v])])
    

solution = max([np.prod([len(s) for s in v]) for v in visibles_trees.values()])
print("PART2: ", solution) # > 360