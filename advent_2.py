file = open('advent_data_2.txt')

lines = file.readlines()
passcount = 0
passtwocount = 0

for line in lines:
    line = line.strip('\n')
    parts = line.split(' ')
    bounds = parts[0].split('-')
    l_bound = int(bounds[0])
    u_bound = int(bounds[1])
    char = parts[1][0]
    password = parts[2]
    # Task 1
    if password.count(char) <= u_bound:
        if password.count(char) >= l_bound:
            passcount += 1

    # Task 2
    if len(password) >= u_bound-1:
        if (password[l_bound-1] == char) ^ (password[u_bound-1] == char):
            passtwocount += 1

print(passcount)
print(passtwocount)
