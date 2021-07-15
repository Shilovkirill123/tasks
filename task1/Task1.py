from sys import argv
from itertools import cycle, islice
n = int(argv[1])
m = int(argv[2])
s = []

for i in range(n):
    s.append(i+1)

x = m-1
y = x + m
s_list = [1]

while True:
    m_list = list(islice(cycle(s),x,y))
    x,y = y-1,y+m-1
    s_list.append(m_list[0])
    if s_list[-1] == 1:
        s_list = s_list[:-1]
        break

a = ''
for i in s_list:
    a += str(i)

print(int(a))