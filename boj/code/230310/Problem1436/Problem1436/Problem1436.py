
inNum = int(input())

minValue = 666

cnt = 0
for i in range(666, 123456789):
    if str(i).find('666') != -1:
        cnt += 1
        if cnt == inNum:
            result = i
            break

print(result)