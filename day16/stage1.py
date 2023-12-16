from collections import deque 

f = open("input.txt", "r") 

def add_pos(pos1, pos2): 
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

# construct graph 
matrix = f.readlines() 
row, col = len(matrix), len(matrix[0]) - 1

# each node is (pos, dir)
# dir: r(right), l(left), u(up), d(down)
dir_mapping = {"r": (0,1), "l": (0,-1), "u": (-1,0), "d": (1,0)}

init = None
if matrix[0][0] == "." or matrix[0][0] == "-": 
    init = [((0,0), "r")]
elif matrix[0][0] == "|": 
    init = [((0,0), "u"), ((0,0), "d")]
elif matrix[0][0] == "/": 
    init = [((0,0), "u")]
elif matrix[0][0] == "\\": 
    init = [((0,0), "d")]
queue = deque(init)

seen = [[False] * col for _ in range(row)] 
seen[0][0] = True 
visited = [[set() for i in range(col)] for j in range(row)]
visited[0][0].add("r")
mirror_mapping = {"/": {"r": "u", "l": "d", "u": "r", "d": "l"}, "\\": {"r": "d", "l": "u", "u": "l", "d": "r"}}
while queue: 
    print(queue)
    level_len = len(queue)
    for _ in range(level_len): 
        # get node [v]
        pos, direction = queue.popleft() 
        i, j = pos
        seen[i][j] = True 
        visited[i][j].add(direction)
        # move node [v]
        new_i, new_j = add_pos(pos, dir_mapping[direction])
        # check bound: [v]
        if new_i < 0 or new_i >= row or new_j < 0 or new_j >= col: 
            # abandon the beam [v]
            continue 
        encounter = matrix[new_i][new_j] 
        # check mirror [v]
        if encounter == "/" or encounter == "\\":
            new_dir = mirror_mapping[encounter][direction]
            if new_dir not in visited[new_i][new_j]:
                queue.append(((new_i, new_j), new_dir))
        # check splitter 
        elif encounter == "|" and (direction == "r" or direction == "l"): 
            if "u" not in visited[new_i][new_j]:
                queue.append(((new_i, new_j), "u"))
            if "d" not in visited[new_i][new_j]:
                queue.append(((new_i, new_j), "d"))
        elif encounter == "-" and (direction == "u" or direction == "d"): 
            if "l" not in visited[new_i][new_j]:
                queue.append(((new_i, new_j), "l"))
            if "r" not in visited[new_i][new_j]:
                queue.append(((new_i, new_j), "r"))     
        # handle pass through [v]
        else: 
            if direction not in visited[new_i][new_j]: 
                queue.append(((new_i, new_j), direction))
        
total = 0 
for i in range(row): 
    for j in range(col): 
        if seen[i][j]: 
            total += 1
print(total) 
# for li in seen: 
#     print(["." if not i else "#" for i in li])