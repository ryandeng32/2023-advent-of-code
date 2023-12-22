f = open('input.txt', 'r')
matrix = f.readlines()

row, col = len(matrix), len(matrix[0]) - 1 

start_pos = None
for i in range(row): 
    for j in range(col): 
        if matrix[i][j] == 'S': 
            start_pos = (i, j) 

steps = 0 
curr_pos = start_pos 
next_pos = None 
prev_dir = None 
char_to_dir = {'|': {(1,0): (1,0), (-1,0): (-1,0)}, 
               '-': {(0,1): (0,1), (0,-1): (0,-1)},
               'L': {(1,0): (0,1), (0,-1): (-1,0)},
               'J': {(1,0): (0,-1), (0,1): (-1,0)},
               '7': {(0,1): (1,0), (-1,0): (0,-1)},
               'F': {(-1,0): (0,1), (0,-1): (1,0)}}
for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]: 
    new_i, new_j = di + start_pos[0], dj + start_pos[1]
    if new_i >= 0 and new_i < row and new_j >= 0 and new_j < col: 
        if ((di, dj) == (0,1) and matrix[new_i][new_j] in ['-', 'J', '7']) or (
            (di, dj) == (0,-1) and matrix[new_i][new_j] in ['-', 'L', 'F']) or (
            (di, dj) == (1,0) and matrix[new_i][new_j] in ['|', 'L', 'J']) or (
            (di, dj) == (-1,0) and matrix[new_i][new_j] in ['|', '7', 'F']):
            next_pos = (new_i, new_j) 
            prev_dir = (di, dj)
            try:
                curr_pos = start_pos 
                steps = 0
                while curr_pos != start_pos or steps == 0: 
                    curr_pos = next_pos
                    if matrix[next_pos[0]][next_pos[1]] == 'S':
                        steps += 1
                        break  
                    di, dj = char_to_dir[matrix[next_pos[0]][next_pos[1]]][prev_dir]
                    next_pos = (next_pos[0] + di, next_pos[1] + dj)  
                    prev_dir = (di, dj)
                    steps += 1
                print(steps)
                break
            except:
                continue 


