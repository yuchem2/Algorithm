
inNum = int(input())

minBagNum = 1234
maxBagNum = [ inNum // 3, inNum // 5] # 3kg, 5kg

for i in range(0, maxBagNum[0]+1):
    for j in range(0, maxBagNum[1]+1):
        if i*3 + j* 5 == inNum and i+j < minBagNum:
            minBagNum = i + j

if minBagNum == 1234:
    minBagNum = -1

print(minBagNum)