from collections import Counter
# Input
lines = [l.rstrip('\n') for l in open('advent_data_10.txt').readlines()]
lines = [int(l) for l in lines]
lines.extend([0, max(lines)+3])
lines.sort()

# Part 1

cd = [x - lines[i - 1] for i, x in enumerate(lines)][1:]

print(cd.count(3)*cd.count(1))

# Part 2- dynamic programming
routes = Counter()
routes[0] = 1

lines = lines[1:]

for line in lines:
    routes[line] = routes[line - 1] + routes[line - 2] + routes[line - 3]

print(routes[lines[-1]])
