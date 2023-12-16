def process_line(hand, bid): 
    count = dict() 
    for c in hand: 
        if c not in count: 
            count[c] = 0 
        count[c] += 1
    if 5 in count.values(): 
        match['five-of-a-kind'].append((hand, bid)) 
    elif 4 in count.values(): 
        match['four-of-a-kind'].append((hand, bid))
    elif 3 in count.values(): 
        if 2 in count.values(): 
            match["full-house"].append((hand, bid))
        else: 
            match["three-of-a-kind"].append((hand, bid))
    elif 2 in count.values(): 
        if list(count.values()).count(2) == 2:
            match["two-pair"].append((hand, bid))
        else:
            match["one-pair"].append((hand, bid))
    else: 
        match["high-card"].append((hand, bid)) 

f = open("input.txt", "r")
line = f.readline()
card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
hand_order = ["five-of-a-kind", "four-of-a-kind", "full-house", "three-of-a-kind", "two-pair", "one-pair", "high-card"]
match = {"high-card": [], "one-pair": [], "two-pair": [], "three-of-a-kind": [], "full-house": [], "four-of-a-kind": [], "five-of-a-kind": []}
while line: 
    hand, bid = line.split()
    process_line(hand, bid)
    line = f.readline() 
curr_rank = 1 
total = 0 
for order in reversed(hand_order): 
    for hand in sorted(match[order], key=lambda x: tuple([card_order.index(c) for c in x[0]]), reverse=True): 
        total += curr_rank * int(hand[1])
        curr_rank += 1
print(total)
