def process_line(line): 
    _, r = line.split(":")
    target, curr = [x.strip() for x in r.split("|")]
    target_arr = target.split(" ")
    curr_arr = curr.split(" ")
    matched = len([x for x in curr_arr if x in target_arr and x != ""])
    return 2 ** (matched - 1) if matched > 0 else 0

f = open("input.txt", "r")
total = 0 
line = f.readline() 
while line: 
    total += process_line(line) 
    line = f.readline() 
print(total)
