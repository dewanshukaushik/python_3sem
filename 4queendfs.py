def solve_n_queens(n):
  """
  Solves the n-queens problem using depth first search.

  Args:
    n: The number of queens.

  Returns:
    A list of lists, where each list represents the position of a queen on the board.
  """

  # Initialize the board to an empty list of lists.
  board = [[0] * n for _ in range(n)]

  # Recursively solve the problem.
  return _solve_n_queens(board, 0)

def _solve_n_queens(board, row):
  # If we have placed all of the queens, return the board.
  if row == len(board):
    return board

  # Try placing a queen in the current row.
  for col in range(len(board[row])):
    if is_safe(board, row, col):
      board[row][col] = 1
      solution = _solve_n_queens(board, row + 1)
      if solution:
        return solution

  # If we couldn't place a queen in the current row, backtrack.
  board[row][col] = 0
  return None

def is_safe(board, row, col):
  # Check if there is a queen in the current row.
  for i in range(len(board[row])):
    if board[row][i] == 1:
      return False

  # Check if there is a queen in the current column.
  for i in range(len(board)):
    if board[i][col] == 1:
      return False

  # Check if there is a queen on either diagonal.
  for i in range(len(board)):
    if board[i][i] == 1 and i != row and i != col:
      return False
    if board[i][len(board) - 1 - i] == 1 and i != row and i != col:
      return False

  # No queens found, so it is safe to place a queen in the current row and column.
  return True