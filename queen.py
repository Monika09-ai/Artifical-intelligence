def solve(row,queens,solutions,n):
    if row == n:
        solutions.append(queens[:])
        return
    for col in range(n):
        if all(col !=c and abs(col-c) != row - r for r,c in enumerate(queens)):
            queens.append(col)
            solve(row+1,queens,solutions,n)
            queens.pop()

def print_solutions (solutions,n):
    for sol in solutions:
        for col in sol:
            print('.' * col + 'Q'+'.'*(n - col -1))
        print()

n=4
solutions = []
solve(0,[],solutions,n)
print(f"Found {len(solutions)} solutions:\n")
print_solutions(solutions,n)                       