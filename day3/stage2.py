import math 

f = open("input.txt", "r") 
matrix = f.readlines()

# -1 to handle \n 
row, col = len(matrix), len(matrix[0]) - 1

symbol_pos = dict()
valid_pos = dict()
seen_num_pos = set() 

for i in range(row): 
    for j in range(col): 
        # gather pos of potential gear
        if matrix[i][j] == "*": 
            symbol_pos[(i, j)] = []
for (i, j) in symbol_pos: 
    for di, dj in [(0,0),(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]: 
        valid_pos[(i+di, j+dj)] = (i,j)

def process_num_starting_at(i, j): 
    num = 0
    pos = None 
    while j < col and matrix[i][j].isdigit():  
        seen_num_pos.add((i, j))
        if (i,j) in valid_pos: 
            pos = (i,j)
        num = num * 10 + int(matrix[i][j]) 
        j += 1
    if pos: 
        symbol_pos[valid_pos[pos]].append(num) 


for i in range(row): 
    for j in range(col): 
        if matrix[i][j].isdigit() and (i,j) not in seen_num_pos: 
            process_num_starting_at(i, j) 

total = 0 
for symbol in symbol_pos: 
    if len(symbol_pos[symbol]) == 2: 
        total += math.prod(symbol_pos[symbol])
print(total)