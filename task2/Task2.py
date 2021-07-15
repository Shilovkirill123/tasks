from sys import argv

import os, math

script, filename1, filename2 = argv

input = open(filename1, 'r')

center_x,center_y = map(int, input.readline().split())
radius = int(input.readline())

with  open(filename2) as f:
    s = []
    for i in f:
        s.append((int(i[0]),int(i[2])))


def in_circle(center_x, center_y, radius, x, y):
    dist = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)
    if dist == radius:
        return 0
    elif dist < radius:
        return 1
    else:
        return 2
    

for i in s:
    print(in_circle(center_x,center_y,radius,i[0],i[1]))