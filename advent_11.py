import numpy as np
import collections


lines = [l.rstrip('\n') for l in open('advent_data_11.txt').readlines()]
lines = [[char for char in l] for l in lines]
lines = np.array(lines)

# Part 1
op = lines.copy()
changed = True

while changed:
    changed = False
    ip = op.copy()
    print(np.char.count(ip, sub='#').sum())
    for r_i in range(0, len(lines)):
        for c_i in range(0, len(lines[0])):
            surround = ip[max(r_i-1, 0):min(r_i+2, len(lines)), max(c_i-1, 0):min(c_i+2, len(lines[0]))]
            hash_count = np.char.count(surround, sub='#').sum()

            if ip[r_i, c_i] == 'L' and hash_count == 0:
                op[r_i, c_i] = '#'
                changed = True
            elif ip[r_i, c_i] == '#' and hash_count >= 5:
                op[r_i, c_i] = 'L'
                changed = True


def occupied(d_x, d_y):
    if [d_x, d_y] == [0, 0]:
        return False
    if 0 <= r_i+d_x < len(ip) and 0 <= c_i+d_y < len(ip[0]):
        if ip[r_i+d_x, c_i+d_y] == '#':
            return True
        elif ip[r_i, c_i+d_y] == '.':
            return occupied(d_x+np.sign(d_x), d_y+np.sign(d_y))
    return False


changed = True
op = lines.copy()
# Part 2
while changed:
    ip = op.copy()
    changed = False
    print(np.char.count(ip, sub='#').sum())
    for r_i in range(0, len(lines)):
        for c_i in range(0, len(lines[0])):
            occs = []
            for ddx in range(-1, 2):
                for ddy in range(-1, 2):
                    if ddx == ddy == 0:
                        continue
                    i = 1
                    while 0 <= r_i + i * ddx < len(ip) and 0 <= c_i + i * ddy < len(ip[0]):
                        ch = ip[r_i + i * ddx][c_i + i * ddy]
                        if ch != '.':
                            occs.append(ch)
                            break
                        i += 1
            hash_count = occs.count('#')

            if ip[r_i, c_i] == 'L' and hash_count == 0:
                op[r_i, c_i] = '#'
                changed = True
            elif ip[r_i, c_i] == '#' and hash_count >= 5:
                op[r_i, c_i] = 'L'
                changed = True


