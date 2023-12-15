f = open("input.txt", "r") 
tokens = [line.strip() for line in f.readlines()][0].split(",")

boxes = {i: {"order": [], "contains": set()} for i in range(256)}

def hash(label): 
    curr = 0 
    for s in label: 
        curr += ord(s)
        curr *= 17 
        curr %= 256 
    return curr

for token in tokens: 
    if "-" in token: 
        label = token.split("-")[0] 
        box = boxes[hash(label)]
        if label in box["contains"]:   
            box["contains"].remove(label) 
            box["order"] = [x for x in box["order"] if x[0] != label]
    elif "=" in token:
        label, num = token.split("=")
        box = boxes[hash(label)]
        if label in box["contains"]: 
            box["order"] = [x if x[0] != label else (label, num) for x in box["order"]]
        else: 
            box["order"].append((label, num))
            box["contains"].add(label)

total_power = 0 
for i, box_index in enumerate(boxes.keys(), 1): 
    curr_power = 0 
    box = boxes[box_index]
    for j, (label, num) in enumerate(box["order"], 1): 
        curr_power += i * j * int(num)
    total_power += curr_power 
print(total_power)

