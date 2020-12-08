file = open('advent_data_8.txt')

lines = file.readlines()

instruction = []

for line in lines:
    line=line.strip('\n')
    seq = line.split(' ')
    instruction.append((seq[0], int(seq[1])))


def compil(instruct):
    lineno = 0
    acc = 0
    visited=[False for i in range(len(instruct))]
    while True:
        if lineno >= len(instruct):
            return acc, True
        elif visited[lineno]:
            return acc, False
        else:
            visited[lineno] = True
            if instruct[lineno][0] == 'nop':
                lineno += 1
            elif instruct[lineno][0] == 'acc':
                acc += instruct[lineno][1]
                lineno += 1
            elif instruct[lineno][0] == 'jmp':
                lineno += instruct[lineno][1]

# Part 1

print(compil(instruction))

# Part 2
acc = 0
term = False
for i in range(len(instruction)):
    if instruction[i][0] == 'jmp':
        instruction[i] = ('nop', instruction[i][1])
    elif instruction[i][0] == 'nop':
        instruction[i] = ('jmp', instruction[i][1])

    acc, term = compil(instruction)
    if term:
        break

    # Flip the instructions again
    if instruction[i][0] == 'jmp':
        instruction[i] = ('nop', instruction[i][1])
    elif instruction[i][0] == 'nop':
        instruction[i] = ('jmp', instruction[i][1])

print(acc, term)
