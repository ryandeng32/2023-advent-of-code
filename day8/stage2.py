import math
import re 

f = open("input.txt", "r") 
commands = f.readline().strip()
# skip empty line 
f.readline()

nodes = {} 
line = f.readline() 
pattern = re.compile(r"[1-9A-Z]{3}")
while line: 
    group = pattern.findall(line)
    nodes[group[0]] = (group[1], group[2])
    line = f.readline()

init = [x for x in nodes if x[-1] == "A"]
command_to_index = {"R": 1, "L": 0}

# find cycle 
def get_cycle(node): 
    curr = node
    dist = 0 
    index = 0 
    while True: 
        command = commands[index]
        index = (index + 1) % len(commands) 
        dist += 1
        curr = nodes[curr][command_to_index[command]]
        if curr[-1] == 'Z': 
            return dist

cycles = [get_cycle(x) for x in init]
print(math.lcm(*cycles))