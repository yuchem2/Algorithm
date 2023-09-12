import sys
sys.setrecursionlimit(10**6)


def find_tree(inst, ined, post, poed):
    if inst > ined or post > poed:
        return

    root = index[postorder[poed]]
    new_left_poed = post+root-1-inst
    sys.stdout.write(str(inorder[root]) + " ")

    find_tree(inst, root-1, post, new_left_poed)
    find_tree(root+1, ined, new_left_poed+1, poed-1)


v_num = int(input())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
index = [-1]*(v_num+1)
for i in range(v_num):
    index[inorder[i]] = i


find_tree(0, v_num-1, 0, v_num-1)

