class DP:
    def __init__(self):
        pass

    def fib(self, n):
        if n == 0:
            return 0
        if n < 3:
            return 1
        a = 1
        b = 1
        for i in range(3, n+1):
            t = b
            b += a
            a = t
        return b


dp = DP()

print dp.fib(9)