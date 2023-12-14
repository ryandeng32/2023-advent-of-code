def parse_line(line): 
    l, r = 0, len(line) - 1 
    while not line[l].isnumeric(): 
        l += 1
    while not line[r].isnumeric(): 
        r -= 1
    return int(line[l]) * 10 + int(line[r])

f = open("input.txt", "r")

total = 0
line = f.readline()
while line: 
    total += parse_line(line) 
    line = f.readline()

print(total)