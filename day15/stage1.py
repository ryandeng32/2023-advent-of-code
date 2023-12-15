f = open("input.txt", "r") 
tokens = [line.strip() for line in f.readlines()][0].split(",")
print(len(tokens))

total = 0 
for token in tokens: 
    curr = 0 
    for s in token: 
        curr += ord(s)
        curr *= 17 
        curr %= 256 
    total += curr
print(total)