need_data = [1, 1, 2, 2, 2, 8]
out_data = [0, 0, 0, 0, 0, 0]
x = input()
in_data = x.split()

for i in range(0, len(need_data), 1):
    out_data[i] = need_data[i] - int(in_data[i])
    print(out_data[i], end = " ")
print()
