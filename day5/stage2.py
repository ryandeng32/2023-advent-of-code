import re

f = open("input.txt", "r") 
lines = [line.strip() for line in f.readlines()]

seeds_line = [int(seed) for seed in lines[0].split(": ")[1].split()]
seeds = [] 
def parse_seeds_line(): 
    i = 0 
    while i < len(seeds_line): 
        seed, length = seeds_line[i], seeds_line[i+1]
        seeds.append((seed, seed + length - 1))
        i += 2
parse_seeds_line()
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


def apply_interval(i1, i2, new_start): 
    i1_start, i1_end = i1[0], i1[1]
    i2_start, i2_end = i2[0], i2[1]
    # print(i1, i2, new_start)
    overlap_start, overlap_end = max(i1_start, i2_start), min(i1_end, i2_end)
    # print("Overlap" + " " + str(overlap_start) + " " + str(overlap_end))
    if overlap_end < overlap_start: 
        return [], [i1]
    offset = i2_start - new_start
    ret = ([((overlap_start - offset, overlap_end - offset))], [(i1_start, overlap_start - 1), (overlap_end+1, i1_end)])
    return [x for x in ret[0] if x[1] >= x[0]], [x for x in ret[1] if x[1] >= x[0]]




results = set(seeds[::])
for i in map_line_indices: 
    mappings = extract_mapping(i + 1) 
    # print("----------------")
    # print(results)
    new_results = set()
    to_change = results.copy()
    temp_to_change = to_change.copy()
    for mapping in mappings: 
        # print("new_results before: ", new_results)
        for interval in to_change: 
            changed, unchanged = apply_interval(interval, (mapping[1], mapping[1] + mapping[2] - 1), mapping[0])
            temp_to_change.remove(interval) 
            if unchanged: 
                temp_to_change.update(unchanged) 
            new_results.update(changed)
        # print("new_results after: ", new_results)
        to_change = temp_to_change.copy()
    new_results.update(to_change)
    results = new_results

# print("-----")
# print(results)
print(min([x[0] for x in results]))

f.close()
