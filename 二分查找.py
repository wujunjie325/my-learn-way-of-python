def search(arr, teaget):
    r = len(arr) - 1
    l = 0
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == teaget:
            return mid
        elif arr[mid] > teaget:
            r = mid - 1
        elif arr[mid] < teaget:
            l = mid + 1
    return l
List = [1,2,4,4,5,6,7,8,9]
print(search(List, 3))