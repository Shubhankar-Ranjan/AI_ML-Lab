from copy import deepcopy

def hill_climbing(initial_state, heuristic, max_iterations=1000):
    current_state = initial_state
    for i in range(max_iterations):
        print(f"Iteration {i+1}")
        print("Current state:")
        for row in current_state:
            print(row)
        print("Heuristic value:", heuristic(current_state))
        neighbors = get_neighbors(current_state)
        next_state = min(neighbors, key=heuristic)
        if heuristic(next_state) >= heuristic(current_state):
            return current_state, "No better neighbor found"
        current_state = next_state
    return current_state, "Maximum iterations reached"

def get_neighbors(state):
    # Find the empty tile
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
        if x is not None:
            break

    # Generate all possible moves
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    neighbors = []
    for move in moves:
        if 0 <= move[0] < 3 and 0 <= move[1] < 3:
            new_state = deepcopy(state)
            new_state[x][y], new_state[move[0]][move[1]] = new_state[move[0]][move[1]], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def heuristic(state):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                for m in range(3):
                    for n in range(3):
                        if state[i][j] == goal[m][n]:
                            cost += abs(i - m) + abs(j - n)
    return cost

# Example usage:
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]  # This should be your initial state
final_state, reason = hill_climbing(initial_state, heuristic)
print(final_state)
print("Stopped because:", reason)