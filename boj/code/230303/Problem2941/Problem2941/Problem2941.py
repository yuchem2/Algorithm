croDic = {'c=': 2, 'c-': 2, 'd-': 2, 'lj': 2, 'nj': 2, 's=': 2, 'z=': 2, 'dz=': 3}

inStr = input()
count = 0
i = 0
indexIncNum = 1

while i < len(inStr)-1: 
    if i < len(inStr)-2 and ''.join(inStr[i:i+3]) in croDic:
        indexIncNum = croDic['dz=']
    elif i < len(inStr)-1:
        tmp = ''.join(inStr[i:i+2])
        if tmp in croDic:
            indexIncNum = croDic[tmp]
        else:
            indexIncNum = 1
    count += 1
    i = i + indexIncNum
if i == len(inStr)-1:
    count += 1
print(count)
