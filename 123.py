import random
arr=[1,3,4,1,6,2,8,9,0,5,3]
for i in range(len(arr)):
    arr[i]=random.randint(1,10)
#冒泡排序
def maopao_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def select_sort(arr):
    for i in range(len(arr)-1):
        cul = i
        for j in range(i, len(arr)):
            if arr[j] < arr[cul]:
                cul = j
        arr[cul], arr[i] = arr[i], arr[cul]
def insert_sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                arr.insert(j,arr.pop(i))
                break
def insertsoet(arr):
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                break
def marger(arr_1, arr_2):
    index_1 = 0
    index_2 = 0
    while index_1 < len(arr_1) and index_2 < len(arr_2):
        
def margersort(arr):

insertsoet(arr)
#maopao_sort(arr)
print(arr)
#select_sort(arr)
insert_sort(arr)
print(arr)
