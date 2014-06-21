def C(n, m):
    """ 计算组合数 C m 取 n """
    return factorial(m) / (factorial(m-n) * factorial(n))


def factorial(n, memo=None):
    """ 计算 n! """
    assert isinstance(n, int)
    if memo is None:
        memo = {0: 1, 1: 1}
    if n not in memo:
        memo[n] = n * factorial(n-1)
    return memo[n]

p = [0 for i in range(7)]   # Probability list init
blue = 16   # ball number
red = 33
total = C(6, red) * C(1, blue)
p[1] = (C(6, 6) * C(1, 1)) / total  # 6+1
p[2] = (C(6, 6) * C(1, blue-1)) / total     # 6+0
p[3] = (C(5, 6) * C(1, red-6) * C(1, 1)) / total    # 5+1
# 5+0 || 4+1
p[4] = (C(5, 6)*C(1, red-6)*C(1, blue-1) + C(4, 6)*C(2, red-6)*C(1, 1)) / total
# 4+0 || 3+1
p[5] = (C(4, 6)*C(2, red-6)*C(1, blue-1) + C(3, 6)*C(3, red-6)*C(1, 1)) / total
# 2+1 || 1+1 || 0+1
p[6] = ((C(2, 6)*C(4, red-6)*C(1, 1) + C(1, 6)*C(5, red-6)*C(1, 1)
        + C(6, red-6)*C(1, 1)) / total)

expect1 = 5*p[6] + 10*p[5] + 200*p[4] + 3000*p[3]   # 无视一、二等奖
# 一二等假设为50W,500W 这个数字是不靠谱的
# expect2 = 5*p[6] + 10*p[5] + 200*p[4] + 3000*p[3] + 500000*p[2] + 5000000*p[1]
for i in range(1, 7):
    print("得奖概率: p[{0}] = {1}".format(i, p[i]))
print("数学期望: min = {0} ".format(expect1))
