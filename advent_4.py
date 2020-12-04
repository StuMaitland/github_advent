import ast

file = open('advent_data_4.txt')

lines = file.readlines()

fields = {
    'byr': False,
    'iyr': False,
    'eyr': False,
    'hgt': False,
    'hcl': False,
    'ecl': False,
    'pid': False
}
opt_fields = {'cid': False}

batch = ''
correct_count = 0

# Section 1

for line in lines:
    line = line.strip('\n')

    batch = batch + ' ' + line

    batch = batch.strip()

    if line == '':  # End of batch reached
        vals = batch.split(' ')
        for val in vals:
            key = val.split(':')[0]
            if key in fields.keys():
                fields[key] = True

        if all(value is True for value in fields.values()):
            correct_count += 1
        # reset the counters
        batch = ''
        fields = dict.fromkeys(fields, False)
        opt_fields = dict.fromkeys(opt_fields, False)
        continue
print(correct_count)

# Section 2

batch = ''
correct_count = 0

# Section 2


def field_validator(f_key, value):
    if value == '':
        return False
    if f_key == 'byr':
        if 1920 <= int(value) <= 2002:
            return True
    elif f_key == 'iyr':
        if 2010 <= int(value) <= 2020:
            return True
    elif f_key == 'eyr':
        if 2020 <= int(value) <= 2030:
            return True
    elif f_key == 'hgt':
        if value[-2:] == 'cm':
            if 150 <= int(value[0:-2]) <= 193:
                return True
        elif value[-2:] == 'in':
            if 59 <= int(value[0:-2]) <= 76:
                return True
    elif f_key == 'hcl':
        if len(value) == 7:
            if value[1:].isalnum():
                return True
    elif f_key == 'ecl':
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    elif f_key == 'pid':
        if len(value) == 9:
            if value.isnumeric():
                return True
    return False


for line in lines:
    line = line.strip('\n')

    batch = batch + ' ' + line

    batch = batch.strip()

    if line == '':  # End of batch reached
        vals = batch.split(' ')
        for val in vals:
            [key, value] = val.split(':')
            valid=field_validator(key, value)
            print(key,': ', value, ' ', valid)
            if valid:
                fields[key] = True

        if all(value is True for value in fields.values()):
            correct_count += 1
        # reset the counters
        batch = ''
        fields = dict.fromkeys(fields, False)
        opt_fields = dict.fromkeys(opt_fields, False)
        continue
print(correct_count)
