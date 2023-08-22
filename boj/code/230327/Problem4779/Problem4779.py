# baekjoon Problem 4779
# input: multiple n(0 <= n <=12)
# output: print cantor set
# 2023-03-27

import sys

def MakeBlank(x, l, r):
    for i in range(l, r+1):
        x[i] = ' '

def CantorSet(x, l, r):
    if r-l+1 >= 3:
        cnt = (r-l+1) // 3
        m1 = l + cnt
        m2 = m1 + cnt
        CantorSet(x, l, m1-1)
        CantorSet(x, m2, r)
        MakeBlank(x, m1, m2-1)

inNumList = []
while True:
    num = sys.stdin.readline().rstrip()
    if num:
        inNumList.append(int(num))
    else:
        break

lines = []
for i in inNumList:
    num = int(i)
    line = ['-' for i in range(3**num)]
    CantorSet(line, 0, len(line)-1)
    lines.append(''.join(line))

for line in lines:
    sys.stdout.write(line+'\n')