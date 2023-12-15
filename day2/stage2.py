LIMIT = {
    "red": 12, 
    "green": 13, 
    "blue": 14
}
def parseline(line): 
    min_required = {"red": 0, "green": 0, "blue": 0}
    _, content = line.split(":")
    total_revealed = content.strip().split(";")
    for set_revealed in total_revealed:
        info = set_revealed.strip().split(",")
        for single in info: 
            num, colour = single.strip().split(" ")
            min_required[colour] = max(min_required[colour], int(num)) 
    return min_required["red"] * min_required["blue"] * min_required["green"]

f = open("input.txt", "r")
line = f.readline()
total = 0 
while line: 
    total += parseline(line)
    line = f.readline() 
print(total)