
steps = 30000000 # 2020 for part 1
ns = [1, 17, 0, 10, 18, 11, 6]
last, c = ns[-1], {n: i+1 for i, n in enumerate(ns)}
for i in range(len(ns), steps):
    c[last], last = i, i - c.get(last, i)
print(last)