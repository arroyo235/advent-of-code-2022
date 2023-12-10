def imprimir_malla(conjuntos):
    # Obtener las coordenadas máximas y mínimas
    min_x = min(conjuntos, key=lambda x: x[0])[0]
    min_y = min(conjuntos, key=lambda x: x[1])[1]
    max_x = max(conjuntos, key=lambda x: x[0])[0]
    max_y = max(conjuntos, key=lambda x: x[1])[1]

    # Ajustar las coordenadas para que (0, 0) esté en la esquina inferior izquierda
    matriz = [['.' for _ in range(max_x - min_x + 1)] for _ in range(min_y, max_y + 1)]

    # Marcar las posiciones ocupadas con '#'
    for x, y in conjuntos:
        matriz[y - min_y][x - min_x] = '#'

    # Marcar la posición (0, 0) con 'O'
    matriz[-min_y][-min_x] = 'O'

    # Imprimir la representación de la malla por pantalla
    for fila in reversed(matriz):
        print(' '.join(fila))



def part1(lines):
    head_moves = []
    tail_moves = []
    
    # Initial position    
    head_pos = (0,0)
    tail_pos = (0,0)

    tail_moves.append(tail_pos)
    
    for line in lines:
        move = line[0]
        num = int(line[2:])
        # print(move, num)
        if move == "R":
            for i in range(num):
                head_pos = (1+head_pos[0], head_pos[1])
                head_moves.append(head_pos)
                if (abs(head_pos[0] - tail_pos[0]) == 2):
                    tail_pos = (head_pos[0]-1, head_pos[1])
                    tail_moves.append(tail_pos)
                # print(head_pos, tail_pos)
            # draw_grid(tail_moves)
        elif move == "L":
            for i in range(num):
                head_pos = (head_pos[0]-1, head_pos[1])
                head_moves.append(head_pos)
                if (abs(head_pos[0] - tail_pos[0]) == 2):
                    tail_pos = (head_pos[0]+1, head_pos[1])
                    tail_moves.append(tail_pos)
                # print(head_pos, tail_pos)
            # draw_grid(tail_moves)
        elif move == "U":
            for i in range(num):
                head_pos = (head_pos[0], 1+head_pos[1])
                head_moves.append(head_pos)
                if (abs(head_pos[1] - tail_pos[1]) == 2):
                    tail_pos = (head_pos[0], head_pos[1]-1)
                    tail_moves.append(tail_pos)
                # print(head_pos, tail_pos)
            # draw_grid(tail_moves)
        elif move == "D":
            for i in range(num):
                head_pos = (head_pos[0], head_pos[1]-1)
                head_moves.append(head_pos)
                if (abs(head_pos[1] - tail_pos[1]) == 2):
                    tail_pos = (head_pos[0], head_pos[1]+1)
                    tail_moves.append(tail_pos)
                # print(head_pos, tail_pos)
            # draw_grid(tail_moves)
    
    
    # Remove duplicates
    tail_moves = list(set(tail_moves))
    # print(sorted(tail_moves))
    # draw_grid(tail_moves)
    # imprimir_malla(tail_moves)
    print(len(tail_moves)) # Result 6406 
    
def part2(lines):
    pass


if __name__ == "__main__":
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    # part1(lines)
    part1(lines)
    part2(lines)
