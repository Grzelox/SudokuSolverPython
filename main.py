from resources.sudoku_solver import solve, print_board

board = board = [
[1, 0, 0, 0, 4, 0, 0, 0, 0],
[0, 9, 2, 6, 0, 0, 3, 0, 0],
[3, 0, 0, 0, 0, 5, 1, 0, 0],
[0, 7, 0, 1, 0, 0, 0, 0, 4],
[0, 0, 4, 0, 5, 0, 6, 0, 0],
[2, 0, 0, 0, 0, 4, 0, 8, 0],
[0, 0, 9, 4, 0, 0, 0, 0, 1],
[0, 0, 8, 0, 0, 6, 5, 2, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 6]
]
print_board(board)
solve(board)
print("\n")
print_board(board)