f = open("input.txt", "r") 
matrix = f.readlines()

# -1 to handle \n 
row, col = len(matrix), len(matrix[0]) - 1

symbol_pos = set()
valid_pos = set()
seen_num_pos = set() 
total = 0

for i in range(row): 
    for j in range(col): 
        # gather pos of symbol 
        if not matrix[i][j].isdigit() and matrix[i][j] != ".": 
            symbol_pos.add((i, j))
for (i, j) in symbol_pos: 
    for di, dj in [(0,0),(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]: 
        valid_pos.add((i+di, j+dj))

def process_num_starting_at(i, j): 
    num = 0
    is_valid = False
    while j < col and matrix[i][j].isdigit():  
        seen_num_pos.add((i, j))
        if (i,j) in valid_pos: 
            is_valid = True 
        num = num * 10 + int(matrix[i][j]) 
        j += 1
    return num if is_valid else 0 


for i in range(row): 
    for j in range(col): 
        if matrix[i][j].isdigit() and (i,j) not in seen_num_pos: 
            total += process_num_starting_at(i, j) 


print(total)