import re 

f = open("input.txt") 
commands = [x for x in f.readline()[:-1]]
# empty line
f.readline() 
line = f.readline() 
match = dict() 
pattern = re.compile(r"[a-zA-Z]{3}")
while line: 
    values = pattern.findall(line)
    match[values[0]] = {"L": values[1], "R": values[2]}
    line = f.readline() 

curr = "AAA"
total = 0
index = 0 
while True: 
    # print(curr)
    command = commands[index] 
    if curr == "ZZZ": 
        break 
    curr = match[curr][command] 
    index += 1
    total += 1
    index %= len(commands)
print(total)

