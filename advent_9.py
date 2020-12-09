file = open('advent_data_9.txt')

lines = file.readlines()

nums = []
err=0

for line in lines:
    line.strip('\n')
    nums.append(int(line))

# Part 1

for lineno in range(25, len(nums)):
    found = False
    for x in range(lineno-25, lineno):
        search = nums[lineno]-nums[x]
        if search in nums[lineno-25:lineno-1] and search != x:
            found = True
            break
    if not found:
        err = nums[lineno]
        print(err)

# Part 2

for xr in range(0, len(nums)):
    contig = []
    for yr in range(xr, len(nums)):
        contig.append(nums[yr])
        if sum(contig) == err:
            print(sum([min(contig),max(contig)]))
        elif sum(contig) > err:
            break
