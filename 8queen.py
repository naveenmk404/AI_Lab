import random

def initial_board(n):
    """Generate an initial random board state."""
    return [random.randint(0, n-1) for _ in range(n)]

def heuristic(board):
    """Calculate the number of conflicts on the board."""
    n = len(board)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1

    return conflicts

def print_board(board):
    """Print the board state."""
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if col == board[row]:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def hill_climbing(n):
    """Solve the N-Queens problem using hill climbing."""
    current_board = initial_board(n)
    current_cost = heuristic(current_board)

    while current_cost > 0:
        neighbors = []

        for i in range(n):
            for j in range(n):
                if current_board[i] != j:
                    neighbor_board = list(current_board)
                    neighbor_board[i] = j
                    neighbors.append((neighbor_board, heuristic(neighbor_board)))

        neighbors.sort(key=lambda x: x[1])

        if neighbors[0][1] >= current_cost:
            # Stuck in a local minimum
            break

        current_board, current_cost = neighbors[0]

    return current_board

if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    solution = hill_climbing(n)
    print("Solution found:")
    print_board(solution)
