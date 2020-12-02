import pandas as pd

nos = pd.read_csv('advent_data_1.csv')


# This is very messy, could probably do this with transposed arrays, but meh.
# Section 1
for number in nos.values:
    for number2 in nos.values:
        add = number+number2
        if add == 2020:
            print(number*number2)

# Section 2
for number in nos.values:
    for number2 in nos.values:
        for number3 in nos.values:
            add = number+number2+number3
            if add == 2020:
                print(number*number2*number3)
