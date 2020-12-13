import turtle

lines = [l.rstrip('\n') for l in open('advent_data_12.txt').readlines()]

# t = turtle.Turtle()
# t.speed(120)
#
# for line in lines:
#     instruct = line[0]
#     mag = int(line[1:])
#
#     if instruct == 'F':
#         t.forward(mag)
#     elif instruct == 'L':
#         t.left(mag)
#     elif instruct == 'R':
#         t.right(mag)
#     elif instruct == 'N':
#         t.sety(t.pos()[1]+mag)
#     elif instruct == 'S':
#         t.sety(t.pos()[1]-mag)
#     elif instruct == 'E':
#         t.setx(t.pos()[0]+mag)
#     elif instruct == 'W':
#         t.setx(t.pos()[0]-mag)


# print(abs(t.pos()[0])+abs(t.pos()[1]))

t = turtle.Turtle()
h = turtle.Turtle()
h.setpos(10, 1)
t.speed(120)
h.pencolor('red')
h.speed(120)

t.screen.screensize(10000, 10000)

for line in lines:
    instruct = line[0]
    mag = int(line[1:])
    x_diff = h.pos()[0]-t.pos()[0]
    y_diff = h.pos()[1] - t.pos()[1]
    abs_dist = t.distance(h)

    if instruct == 'F':
        t.setpos(t.pos()[0]+x_diff*mag, t.pos()[1]+y_diff*mag)
        h.setpos(t.pos()[0]+x_diff, t.pos()[1]+y_diff)
    elif instruct == 'L':
        if mag == 90:
            h.setpos(t.pos()[0] - y_diff, t.pos()[1] + x_diff)
        elif mag == 180:
            h.setpos(t.pos()[0] - x_diff, t.pos()[1] - y_diff)
        elif mag == 270:
            h.setpos(t.pos()[0] + y_diff, t.pos()[1] - x_diff)
    elif instruct == 'R':
        if mag == 90:
            h.setpos(t.pos()[0] + y_diff, t.pos()[1] - x_diff)
        elif mag == 180:
            h.setpos(t.pos()[0] - x_diff, t.pos()[1] - y_diff)
        elif mag == 270:
            h.setpos(t.pos()[0] - y_diff, t.pos()[1] + x_diff)
    elif instruct == 'N':
        h.sety(h.pos()[1]+mag)
    elif instruct == 'S':
        h.sety(h.pos()[1]-mag)
    elif instruct == 'E':
        h.setx(h.pos()[0]+mag)
    elif instruct == 'W':
        h.setx(h.pos()[0]-mag)

print(abs(t.pos()[0])+abs(t.pos()[1]))

