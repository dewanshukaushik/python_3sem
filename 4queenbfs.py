import collections

def bfs(initial_state):
  """Solves the 4 queens problem using breadth-first search.

  Args:
    initial_state: The initial state of the board, represented as a list of tuples.

  Returns:
    A list of lists representing the solution, or None if no solution exists.
  """

  queue = collections.deque()
  queue.append(initial_state)

  while queue:
    state = queue.popleft()
    if is_solution(state):
      return state

    for next_state in get_next_states(state):
      queue.append(next_state)

  return None

def get_next_states(state):
  """Returns all possible next states of the given state.

  Args:
    state: The current state of the board, represented as a list of tuples.

  Returns:
    A list of lists representing the possible next states.
  """

  next_states = []
  for row in range(4):
    for col in range(4):
      if state[row][col] is None:
        new_state = list(state)
        new_state[row][col] = 1
        next_states.append(new_state)

  return next_states

def is_solution(state):
  """Returns whether the given state is a solution to the 4 queens problem.

  Args:
    state: The current state of the board, represented as a list of tuples.

  Returns:ṇ
    True if the state is a solution, False otherwise.
  """

  for row in range(4):
    for col in range(4):
      if state[row][col] is not None:
        for other_col in range(4):
          if col != other_col and state[row][other_col] is not None:
            if row == other_col:
              return False
            if abs(row - other_col) == abs(col - other_col):
              return False

  return True