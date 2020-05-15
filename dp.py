#递归
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
#动态规划


def dp_fib(n):
    if n <= 2:
        return 1
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]
#记忆化搜索
def memoization_fib(n):
    
print(dp_fib(10))
for i in range(1, 10):
    print(dp_fib(i), end=" ")
