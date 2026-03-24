def solve_n_queens(n):
    def backtrack(row, cols, diag1, diag2, path, solutions):
        if row == n:
            solutions.append(path[:])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            path.append(col)
            backtrack(row + 1, cols, diag1, diag2, path, solutions)
            path.pop(); cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
    sol = []
    backtrack(0, set(), set(), set(), [], sol)
    return sol

if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print("Number of solutions:", len(solutions))
    for s in solutions:
        print(s)
