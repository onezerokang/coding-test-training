import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

preorder_result = []
while True:
    try:
        preorder_result.append(int(input()))
    except:
        break

def postorder(arr):
    if len(arr) < 1:
        return
    root = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] > root:
            right.append(arr[i])
        else:
            left.append(arr[i])
    postorder(left)
    postorder(right)
    print(root)

postorder(preorder_result)