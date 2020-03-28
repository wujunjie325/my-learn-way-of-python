def opt(n,state = False):
    if n == 1:
        return 1
    if n < 2:
        return 0
    if n == 3:
        return 1
    if state is True:
        return opt(n + 1,False) + opt(n - 2,True) + opt(n - 4,True)
    else:
        return opt(n - 2,True) + opt(n - 4,True)

#print(opt(5, False))
'''
#测试github是否有用
b="asd"
c="123"
def qsort(lyst):
    if len(lyst) <= 1:
        return lyst
    poivt = lyst[0]
    r = [i for i in lyst[1:] if i > poivt]
    l = [i for i in lyst[1:] if i <= poivt]
    return qsort(r) + [poivt] + qsort(l)
print(qsort([1,2,6,5,2,9,7,3]))
a=""
b=["1","2","3"]
def asd(a,b):
    return a.join(b)
print(asd(a,b))
'''