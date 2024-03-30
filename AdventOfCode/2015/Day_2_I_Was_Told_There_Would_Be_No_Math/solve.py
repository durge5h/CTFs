data = open("input.txt").read().splitlines()
data = [d.split('x') for d in data]
data = [list(map(int, d)) for d in data]
paper = 0
for d in data:
    sides = [ d[0]*d[1], d[1]*d[2], d[0]*d[2] ]
    paper += 2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides)
print (paper)
