import numpy

file = open('advent_data_3.txt')

lines = file.readlines()[1:]

# Task 1
col_count = 0
tree_count = 0

for line in lines:
    line = line.strip('\n')
    col_count += 3
    ind = col_count % len(line)
    if line[ind] == '#':
        tree_count += 1
print(tree_count)

# Task 2

final_count = []
col_iters = [1, 3, 5, 7, 1]
row_iters = [1, 1, 1, 1, 2]

for n in range(0, len(col_iters)):
    col_count = 0
    tree_count = 0
    for i in range(0, len(lines), row_iters[n]):
        line = lines[i]
        line = line.strip('\n')
        col_count += col_iters[n]
        ind = col_count % len(line)
        if line[ind] == '#':
            tree_count += 1
    final_count.append(tree_count)
print(numpy.prod(final_count))
