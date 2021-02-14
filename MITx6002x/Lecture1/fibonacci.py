def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# for i in range(121):
#     print(f"fib({str(i)}) = {fib(i)}")


def fastFib(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


for i in range(121):
    print(f"fastFib({str(i)}) = {fastFib(i)}")
