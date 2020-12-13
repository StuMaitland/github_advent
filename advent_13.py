file = open('advent_data_13.txt')

lines = file.readlines()

# Part 1
t_start = int(lines[0].strip('\n'))
bus_times = set(lines[1].split(','))
waits = dict()

for time in bus_times:
    if time != 'x':
        time = int(time)
        a= list(range(time, t_start+time, time))
        b = min([i for i in a if i >= t_start])
        waits[time] = b-t_start

low = min(waits.items(), key=lambda x: x[1])

print(low[0]*low[1])

# Part 2
start = int(lines[0])
pairs = []
for i, n in enumerate(lines[1].split(',')):
    if n == 'x':
        continue
    n = int(n)
    pairs.append((n - i, n))


def crt(pairs):  # Chinese remainder theory solution
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx - 2, mx)
        total %= M
    return total


print(crt(pairs))



