print(sum(2 * (l*w + w*h + h*l) + min(l*w, w*h, h*l) for l, w, h in (map(int, line.strip().split('x')) for line in open("./input.txt"))))


