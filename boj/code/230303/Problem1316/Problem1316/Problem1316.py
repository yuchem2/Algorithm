

inStrNum = int(input())
count = 0

for i in range(inStrNum):
    inStr = input()
    # judgement

    word = {}
    word[inStr[0]] = 1
    for j in range(1, len(inStr)):
        if inStr[j-1] == inStr[j]:
            word[inStr[j]] += 1
        else:
            if inStr[j] in word:
                break
            else:
                word[inStr[j]] = 1

    if len(inStr) == sum(word.values()):
        count += 1
    

print(count)
