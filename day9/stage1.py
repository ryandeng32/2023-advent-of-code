def process_line(line): 
    stages = [] 
    curr_stage = [int(x) for x in line.split()]
    stages.append(curr_stage[:]) 
    while len(set(curr_stage)) != 1: 
        curr_stage = [curr_stage[i+1] - curr_stage[i] for i in range(len(curr_stage) - 1)]
        stages.append(curr_stage)
    ret = sum([x[-1] for x in stages])
    return ret

f = open("input.txt", "r")
line = f.readline() 
total = 0 
while line: 
    total += process_line(line) 
    line = f.readline()
print(total)