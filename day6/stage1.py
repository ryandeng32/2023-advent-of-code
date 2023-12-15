def calc_distance(hold_time, total_time): 
    run_time = total_time - hold_time 
    return hold_time * run_time

f = open("small-input.txt", "r")
times = [int(x) for x in f.readline().split(":")[1].strip().split()]
distances = [int(x) for x in f.readline().split(":")[1].strip().split()]

ret = 1
for i, time in enumerate(times): 
    curr = 0 
    for hold_time in range(1,time): 
        if calc_distance(hold_time, time) > distances[i]: 
            curr += 1
    ret *= curr
print(ret) 