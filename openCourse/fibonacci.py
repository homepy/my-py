def fib(x):
    """fibonacci number f(x)"""
    global calls1
    calls1 += 1
    # print('fib({0}) , {1} calls'.format(x, calls1))

    if x == 1 or x == 0:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def fast_fib(x, memo={0: 1, 1: 1}):
    """memo, memoization"""
    assert isinstance(x, int), 'x should be a integer.'
    global calls2
    calls2 += 1
    # print('fib({0}) , {1} calls'.format(x, calls2))

    if x not in memo:
        memo[x] = fast_fib(x - 1) + fast_fib(x - 2)
    return memo[x]


n = int(input('input a integer'))
calls1 = 0
calls2 = 0
print(fib(n), calls1)
print(fast_fib(n), calls2)
