'''
def radix_sort(mylist):#基数排序
    i = 0 
    max_num = max(mylist)  
    j = len(str(max_num)) 
    while i < j:
        bucket_list = [[] for _ in range(10)]
        for x in mylist:
            bucket_list[int(x/(10**i))%10].append(x)
        mylist.clear()
        for x in bucket_list:
            for y in x:
                mylist.append(y)
        i += 1
        print(mylist)
    return mylist
a = eval(input())

print(radix_sort(a))
'''