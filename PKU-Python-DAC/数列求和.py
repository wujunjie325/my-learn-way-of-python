def _sum(arr):
    if arr == []:
        return 0
    return arr[-1] + _sum(arr[:-1])

a = [1,2,3,4,5,6,7,8,9,10]
print(_sum(a))