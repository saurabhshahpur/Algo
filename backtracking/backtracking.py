import time


class BackTracking:
    def __init__(self):
        pass

    def print_knight_solution(self, sol, n):
        for i in range(0, n):
            for j in range(0, n):
                print sol[i][j],
            print "\n"
        return

    def print_queen_solution(self, sol, n):
        for i in range(0, n):
            for j in range(0, n):
                print sol[i][j],
            print "\n"
        return

    def check_pos(self, x, y, n, sol):

        return 0 <= x < n and 0 <= y < n and sol[x][y] == -1

    def knight_tour_problem(self, path_count, n, x, y, sol):
        if path_count == n*n:
            self.print_knight_solution(sol, n)
            return True

        x_pos = [2, 1, -1, -2, -2, -1, 1, 2]
        y_pos = [1, 2, 2, 1, -1, -2, -2, -1]
        # if path_count == 63:
        #     print sol
        for k in range(0, 8):
            x_next = x + x_pos[k]
            y_next = y + y_pos[k]
            if self.check_pos(x_next, y_next, n, sol):
                sol[x_next][y_next] = path_count

                if self.knight_tour_problem(path_count+1, n, x_next, y_next, sol):
                    return True
                else:
                    sol[x_next][y_next] = -1

        return False

    def check_queen_pos(self, x, y, n, queen):
        if 0 <= x < n and 0 <= y < n:
            for i in range(0, n):
                if queen[x][i] != -1:
                    return False
            for i in range(0, n):
                if queen[i][y] != -1:
                    return False
            for i, j in zip(range(0, n), range(0, n)):
                if 0 <= x-i < n and 0 <= y-j < n:
                    if queen[x-i][y-j] != -1:
                        return False
                if 0 <= x+i < n and 0 <= y+j < n:
                    if queen[x+i][y+j] != -1:
                        return False
                if 0 <= x+i < n and 0 <= y-j < n:
                    if queen[x+i][y-j] != -1:
                        return False
                if 0 <= x - i < n and 0 <= y + j < n:
                    if queen[x - i][y + j] != -1:
                        return False
            return True

        return False

    def n_queen_problem(self, n, count, col, queen):
        if count == n:
            self.print_queen_solution(queen, n)
            return True
        for i in range(0, n):
            if self.check_queen_pos(i, col, n, queen):
                queen[i][col] = count
                if self.n_queen_problem(n, count+1, col+1, queen):
                    return True
                else:
                    queen[i][col] = -1

        return False


sol = []
for i in range(0, 8):
    temp = []

    for j in range(0, 8):

        temp.append(-1)
    sol.append(temp)

sol[0][0] = 0
bk = BackTracking()
# bk.print_knight_solution(sol, 8)
# print bk.knight_tour_problem(1, 8, 0, 0, sol)

queen = []
for i in range(0, 20):
    temp = []

    for j in range(0, 20):

        temp.append(-1)
    queen.append(temp)

print time.time()
bk.n_queen_problem(20, 0, 0, queen)
print time.time()

