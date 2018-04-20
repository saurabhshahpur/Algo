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

    def check_array(self, n, k, arr, i):
        return 0 <= i < n and 0 <= arr[i] <= k

    def print_subset_arr(self, n, arr):
        for i in range(0, n):
            if arr[i] < 0:
                print -1*arr[i],
        print "\n"

    def subset_sum(self, n, k, arr):
        if k == 0:
            print "subset found"
            self.print_subset_arr(n, arr)
            return True

        for i in range(0, n):
            if self.check_array(n, k, arr, i):
                arr[i] *= -1
                if self.subset_sum(n, k+arr[i], arr):
                    return True
                else:
                    arr[i] *= -1
        return False

    def print_sudoku(self, matrix):
        for i in range(0, 9):
            for j in range(0, 9):
                print matrix[i][j],
            print ""

    def get_empty_cell(self, matrix, point):
        for i in range(0, 9):
            for j in range(0, 9):
                if not matrix[i][j]:
                    point[0] = i
                    point[1] = j
                    return True
        return False

    def check_sudoku_pos(self, matrix, x, y, key):
        if 0 <= x < 9 and 0 <= y < 9:
            # check horizontal
            for i in range(0, 9):
                if matrix[x][i] == key:
                    return False
            # check vertical
            for i in range(0, 9):
                if matrix[i][y] == key:
                    return False
            # check square
            x_mod = x - x % 3
            y_mod = y - y % 3
            for i in range(0, 3):
                for j in range(0, 3):
                    if matrix[i + x_mod][j + y_mod] == key:
                        return False

            return True

        return False

    def sudoku(self, matrix):
        point = [0, 0]

        if not self.get_empty_cell(matrix, point):
            self.print_sudoku(matrix)
            return True
        for i in range(1, 10):
            if self.check_sudoku_pos(matrix, point[0], point[1], i):
                matrix[point[0]][point[1]] = i
                if self.sudoku(matrix):
                    return True
                else:
                    matrix[point[0]][point[1]] = 0
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

# print time.time()
# bk.n_queen_problem(20, 0, 0, queen)
# print time.time()

arr = [10, 7, 5, 18, 12, 20, 15]
bk.subset_sum(7, 24, arr)


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                      [5, 2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 8, 7, 0, 0, 0, 0, 3, 1],
                      [0, 0, 3, 0, 1, 0, 0, 8, 0],
                      [9, 0, 0, 8, 6, 3, 0, 0, 5],
                      [0, 5, 0, 0, 9, 0, 6, 0, 0],
                      [1, 3, 0, 0, 0, 0, 2, 5, 0],
                      [0, 0, 0, 0, 0, 0, 0, 7, 4],
                      [0, 0, 5, 2, 0, 6, 3, 0, 0]]

bk.sudoku(grid)