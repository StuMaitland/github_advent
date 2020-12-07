file = open('advent_data_6.txt')

lines = file.readlines()

lens = []
batch = ''

for line in lines:
    line = line.strip('\n')

    batch = batch + line

    if line == '':  # End of batch reached
        unique = set(batch)
        lens.append(len(unique))
        batch = ''
        print(batch, ': ', unique, ', ', len(unique))
print(sum(lens))

lens = []
intersects = None

for line in lines:
    line = line.strip('\n')
    if intersects is None:
        intersects = set(line)
    elif line == '':  # End of batch reached
            lens.append(len(intersects))
            intersects = None
    else:
        intersects = intersects.intersection(line)
print(sum(lens))

