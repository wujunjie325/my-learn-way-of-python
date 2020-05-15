arr = [1,2,3,4,5,6]


def _sum(arr):#二分递归
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    return _sum(arr[:n // 2]) + _sum(arr[n // 2 : ])
    

print(_sum(arr))