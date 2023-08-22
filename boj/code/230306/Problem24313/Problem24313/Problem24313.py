x = input()
a1, a0 = x.split(" ")
c = int(input())
n0 = int(input())
a1 = int(a1)
a0 = int(a0)

if c == a1:
    print(int(a0<0))
elif a0/(c-a1) > n0:
    print(0)
else:
    print(int((c-a1)*n0 >= a0))