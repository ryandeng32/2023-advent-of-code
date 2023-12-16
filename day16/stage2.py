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
mirror_mapping = {"/": {"r": "u", "l": "d", "u": "r", "d": "l"}, "\\": {"r": "d", "l": "u", "u": "l", "d": "r"}}


def gen_init(pos, direction): 
    init = None 
    i, j = pos 
    if matrix[i][j] == "." : 
        init = [((i,j), direction)]
    elif matrix[i][j] == "-": 
        if direction == "r" or direction == "l": 
            init = [((i,j), direction)]
        else: 
            init = [((i,j), "l"), ((i,j), "r")]
    elif matrix[i][j] == "|": 
        if direction == "u" or direction == "d": 
            init = [((i,j), direction)]
        else: 
            init = [((i,j), "u"), ((i,j), "d")]
    elif matrix[i][j] == "/": 
        init = [((i,j), mirror_mapping["/"][direction])]
    elif matrix[i][j] == "\\": 
        init = [((i,j), mirror_mapping["\\"][direction])]
    return init 




def get_ret_for_init(start, init): 
    seen = [[False] * col for _ in range(row)] 
    seen[0][0] = True 
    visited = [[set() for i in range(col)] for j in range(row)]
    visited[0][0].add(start[1])
    queue = deque(init)


    while queue: 
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
    return total 




starts = [((0,0), "d"), ((0,0), "r"),  ((col-1,0), "d"), ((col-1,0), "l"),  ((row-1,0), "u"), ((row-1,0), "r"),  ((row-1,col-1), "u"), ((row-1, col-1), "l")]
for i in range(1, col-1): 
    starts.append(((0,i), "d"))
    starts.append(((row-1,i), "u"))
for i in range(1, row-1): 
    starts.append(((i,0), "r"))
    starts.append(((i,col-1), "l"))

curr_max = -float("inf") 
for start in starts: 
    init = gen_init(start[0], start[1])
    curr_max = max(curr_max, get_ret_for_init(start, init)) 

print(curr_max)