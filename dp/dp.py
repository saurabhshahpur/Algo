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

    def print_lcs(self, matrix, m, n, s1):
        i = m-1
        j = n-1
        s = ""
        while i >= 0 and j >= 0 and matrix[i][j]:
            if matrix[i][j-1] == matrix[i][j]:
                j -= 1
            if matrix[i-1][j] == matrix[i][j]:
                i -= 1
            s += s1[i-1]
            i -= 1
            j -= 1
        s = s[::-1]
        print s

    def lcs(self, s1, s2):
        m = 1 + len(s1)
        n = 1 + len(s2)
        matrix = []
        for i in range(0, m):
            temp = []
            for j in range(0, n):
                temp.append(0)
            matrix.append(temp)

        for i in range(1, m):
            for j in range(1, n):
                if s1[i-1] == s2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

        self.print_lcs(matrix, m, n, s1)


dp = DP()

print dp.fib(9)

dp.lcs("ABCDGH", "AEDFHR")