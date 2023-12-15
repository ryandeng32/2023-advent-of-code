def process_line(line): 
    _, r = line.split(":")
    target, curr = [x.strip() for x in r.split("|")]
    target_arr = target.split(" ")
    curr_arr = curr.split(" ")
    matched = len([x for x in curr_arr if x in target_arr and x != ""])
    return matched

f = open("input.txt", "r")
line = f.readline() 
winnings = [] 
copies = [] 
while line: 
    winnings.append(process_line(line))
    copies.append(1)
    line = f.readline() 

total = 0 
for i in range(len(copies)): 
    total += copies[i]
    for j in range(i + 1, i + winnings[i] + 1): 
        copies[j] += copies[i]
print(total)

