import math
# def calc_distance(hold_time, total_time): 
#     run_time = total_time - hold_time 
#     return hold_time * run_time

f = open("input.txt", "r")
time = int("".join(f.readline().split(":")[1].split())) 
distance = int("".join(f.readline().split(":")[1].split())) 

# curr = 0 
# for hold_time in range(1,time): 
#     if calc_distance(hold_time, time) > distance: 
#         curr += 1
# print(curr)

'''Solution with quadratic formula:'''
a = (-time - math.sqrt(time**2 - 4*-1*-distance))/(2*-1)
b = (-time + math.sqrt(time**2 - 4*-1*-distance))/(2*-1)
a, b = min(a, b), max(a, b)
print(math.floor(b) - math.ceil(a) + 1)