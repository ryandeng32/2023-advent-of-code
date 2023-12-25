f = open('input.txt', 'r')
matrix = f.readlines()
row, col = len(matrix), len(matrix[0]) - 1

# get a list of columns without galaxies
expand_cols = set() 
for j in range(col):
    has_galaxies = False
    for i in range(row):  
        if matrix[i][j] == '#': 
            has_galaxies = True
            break 
    if not has_galaxies: 
        expand_cols.add(j) 
print(expand_cols)

# insert column spaces
for i in range(row): 
    new_col = [] 
    for j in range(col): 
        if j in expand_cols: 
            new_col.append('.')
        new_col.append(matrix[i][j])
    matrix[i] = new_col 
col += len(expand_cols) 

# insert row spaces 
expand_rows = set() 
for i in range(row): 
    has_galaxies = False
    for j in range(col): 
        if matrix[i][j] == '#': 
            has_galaxies = True
            break 
    if not has_galaxies: 
        expand_rows.add(i) 
print(expand_rows)
new_matrix = [] 
for i in range(row): 
    if i in expand_rows: 
        new_matrix.append(['.'] * col)
    new_matrix.append(matrix[i]) 
row += len(expand_rows) 
matrix = new_matrix

# find pos of galaxies
galaxies = [] 
for i in range(row): 
    for j in range(col): 
        if matrix[i][j] == '#': 
            galaxies.append((i,j))

def calc_dist(pos1, pos2): 
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

total = 0
for i in range(len(galaxies)): 
    for j in range(i+1, len(galaxies)): 
        total += calc_dist(galaxies[i], galaxies[j])

print(total)