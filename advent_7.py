file = open('advent_data_7.txt')

lines = file.readlines()

tree = {}

for line in lines:
    line = line.strip('\n')
    [parent, children] = line.split(' contain ')  # Split line into parent/children
    children = children[0:-1]
    parent = parent[0:-5]
    childrensp = children.split(', ')

    col = []
    if childrensp[0] != 'no other bags':  # If this is not a leaf node
        for child in childrensp:
            colour = child[2:-4].strip()
            count = int(child[0])
            col.append((colour, count)) # Create a tuple in order to refer back to values
    tree[parent] = col


# Part 1
def has_shiny(color):
    if color == 'shiny gold':
        return True
    return any(has_shiny(c) for c, _ in tree[color])


# Part 2
def search_children(key):
    total = 0
    for color, innercount in tree[key]:
        total += innercount
        total += innercount * search_children(color)
    return total


print(sum(has_shiny(c) for c in tree.keys()) - 1)

print(search_children('shiny gold'))
