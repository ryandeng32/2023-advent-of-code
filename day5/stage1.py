import re

f = open("input.txt", "r") 
lines = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in lines[0].split(": ")[1].split()]

pattern = re.compile(r"\bmap\b")
def extract_mapping(start_index): 
    mappings = [] 
    i = start_index 
    while i < len(lines) and lines[i]: 
        parts = [int(part) for part in lines[i].split()]
        mappings.append(parts) 
        i += 1
    return mappings

map_line_indices = [i for i, line in enumerate(lines) if pattern.search(line)]

results = seeds[::]
for i in map_line_indices: 
    mappings = extract_mapping(i + 1)
    for i, curr in enumerate(results): 
        for mapping in mappings: 
            if curr >= mapping[1] and curr <= mapping[1] + mapping[2]: 
                results[i] = mapping[0] + curr - mapping[1] 
print(min(results))
