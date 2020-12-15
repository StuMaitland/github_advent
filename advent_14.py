file = open('advent_data_14.txt')

lines = [l.rstrip('\n') for l in open('advent_data_14.txt').readlines()]

# Part 1
mem = dict()
mask = 'x' * 36

for line in lines:
    parts = line.split(' = ')
    if parts[0] == 'mask':
        mask = parts[1]
    else:
        addr = int(parts[0][4:-1])
        val = int(parts[1])
        b_val = "{0:036b}".format(val)
        cv = ''
        for i, l in enumerate(mask):
            if l == 'X':
                cv += b_val[i]
            else:
                cv += l
        mem[addr] = int(cv,2)


# Part 2
mem = dict()


def bitstring(x, l):
    return bin(x)[2:].zfill(l)


for line in lines:
    parts = line.split(' = ')
    if parts[0] == 'mask':
        mask = parts[1]
    else:
        addr = "{0:036b}".format(int(parts[0][4:-1]))
        val = int(parts[1])
        addr_template = ''
        for mask_bit, addr_bit in zip(mask, addr):
            if mask_bit == "0":
                addr_template += addr_bit
            elif mask_bit == "1":
                addr_template += "1"
            else:
                addr_template += "{}"
        floating_length = mask.count('X')
        for f in range(2 ** floating_length):
            addr = addr_template.format(*bitstring(f, floating_length))
            addr = int(addr, 2)
            mem[addr] = int(val)

print(sum(mem.values()))