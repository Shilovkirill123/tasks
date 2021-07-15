from sys import argv


script, filename = argv

with  open(filename) as f:
    s = []
    for i in f:
        s.append(int(i))

n = 0
s.sort()
mid = len(s) // 2
mid_s = s[mid]

while len(set(s)) != 1:
    for index, i in enumerate(s):
        if i > mid_s:
            n +=1
            s[index] = i - 1
        elif i < mid_s:
            n +=1
            s[index] = i + 1
        
print(n)
    

