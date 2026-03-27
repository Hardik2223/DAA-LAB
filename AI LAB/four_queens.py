def solve_four_queens():
    n = 4
    solutions = []
    def backtrack(row, cols, d1, d2, path):
        if row == n:
            solutions.append(path[:]); return
        for c in range(n):
            if c in cols or (row-c) in d1 or (row+c) in d2: continue
            cols.add(c); d1.add(row-c); d2.add(row+c); path.append(c)
            backtrack(row+1, cols, d1, d2, path)
            cols.remove(c); d1.remove(row-c); d2.remove(row+c); path.pop()
    backtrack(0,set(),set(),set(),[])
    return solutions

if __name__ == "__main__":
    print("Four Queens solutions:", solve_four_queens())
