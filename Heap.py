#堆
#必须是完全二叉树且父节点必须大于子节点 or 小于
arr = [2,5,3,1,10,4]
def heapify(tree, n , i = 0):
    if i > n:
        return
    c1 = 2*i + 1
    c2 = 2*i + 2
    max = i
    if c1 < n and tree[c1] > tree[max]:
        max = c1
    if c2 < n and tree[c2] > tree[max]:
        max =c2
    if max != i:
        tree[max],tree[i] = tree[i],tree[max]
        heapify(tree, n, max)
def build_heap(tree, n):
    last_node = n - 1
    parent = (last_node - 1) // 2
    for i in range(parent, -1, -1):
        heapify(tree, n, i)
def heapsort(tree, n):
    while n > 0:
        tree[n - 1], tree[0] = tree[0], tree[n - 1]
        n -= 1
        heapify(tree, n, 0)

#heapify(arr, len(arr), 0)
build_heap(arr,len(arr))
heapsort(arr, len(arr))
print(arr)