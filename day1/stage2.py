mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
def parse_line(line): 
    l_seen, r_seen = "", "" 
    l, r = 0, len(line) - 1
    l_seen += line[l]
    r_seen += line[r] 
    while not line[l].isnumeric() and not any([True if str(x) in l_seen else False for x in mapping.keys()]):
        l += 1
        l_seen += line[l]
    while not line[r].isnumeric() and not any([True if x[::-1] in r_seen else False for x in mapping.keys()]):
        r -= 1
        r_seen += line[r]
    
    left_digit, right_digit = None, None
    if line[l].isnumeric(): 
        left_digit = int(line[l])
    else: 
        left_digit = mapping[list(filter(lambda x: x in l_seen, mapping.keys()))[0]]
    if line[r].isnumeric(): 
        right_digit = int(line[r])
    else: 
        right_digit = mapping[list(filter(lambda x: x[::-1] in r_seen, mapping.keys()))[0]]
    
    return left_digit * 10 + right_digit
    
total = 0 
f = open("input.txt", "r") 
line = f.readline() 
while line: 
    total += parse_line(line) 
    line = f.readline() 

print(total)