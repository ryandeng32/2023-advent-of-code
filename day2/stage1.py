LIMIT = {
    "red": 12, 
    "green": 13, 
    "blue": 14
}
def parseline(line): 
    label, content = line.split(":")
    game_num = int(label.strip().split(" ")[1])
    total_revealed = content.strip().split(";")
    for set_revealed in total_revealed:
        info = set_revealed.strip().split(",")
        for single in info: 
            num, colour = single.strip().split(" ")
            if LIMIT[colour.strip()] < int(num):
                return 0
    return game_num

f = open("input.txt", "r")
line = f.readline()
total = 0 
while line: 
    total += parseline(line)
    line = f.readline() 
print(total)