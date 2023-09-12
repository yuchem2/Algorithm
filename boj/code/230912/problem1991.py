import sys


def preorder(x):
    sys.stdout.write(chr(x+65))
    if adj[x][0] != '.':
        preorder(ord(adj[x][0])-65)
    if adj[x][1] != '.':
        preorder(ord(adj[x][1])-65)


def inorder(x):
    if adj[x][0] != '.':
        inorder(ord(adj[x][0]) - 65)
    sys.stdout.write(chr(x + 65))
    if adj[x][1] != '.':
        inorder(ord(adj[x][1]) - 65)


def postorder(x):
    if adj[x][0] != '.':
        postorder(ord(adj[x][0]) - 65)
    if adj[x][1] != '.':
        postorder(ord(adj[x][1]) - 65)
    sys.stdout.write(chr(x + 65))


v_num = int(input())
adj = [[] for _ in range(v_num)]
for _ in range(v_num):
    a, b, c = sys.stdin.readline().split()
    adj[ord(a)-65] = (b, c)

preorder(0)
sys.stdout.write("\n")
inorder(0)
sys.stdout.write("\n")
postorder(0)
sys.stdout.write("\n")