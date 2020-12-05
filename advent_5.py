import numpy as np

file = open('advent_data_5.txt')

lines = file.readlines()

multiples = []
seat_full = np.zeros((128, 8))

for line in lines:
    line = line.replace('F', '0')
    line = line.replace('B', '1')
    line = line.replace('L', '0')
    line = line.replace('R', '1')
    row = int(line[0:7], 2)
    col = int(line[7:], 2)
    seat_full[row, col] = True
    print(line, ': ', row, ', ', col)
    multiples.append((row*8)+col)

print(max(multiples))
unoccupied = np.where(seat_full[2:118, :] == False)
unoccupied_id = ((unoccupied[0]+2)*8)+unoccupied[1]
print(unoccupied_id[0])
