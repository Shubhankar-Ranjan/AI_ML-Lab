from collections import deque

# Function to check if the current player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to generate all possible moves
def generate_moves(board, player):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = [row[:] for row in board]  # Make a copy
                new_board[i][j] = player
                moves.append(new_board)
    return moves

# Breadth First Search
def bfs_tic_tac_toe():
    initial_state = [[' ']*3 for _ in range(3)]
    queue = deque([(initial_state, 'X')])  # Start with X
    visited = set()

    final_state = None
    winner = None

    while queue:
        current_state, current_player = queue.popleft()
        if tuple(map(tuple, current_state)) in visited:
            continue
        visited.add(tuple(map(tuple, current_state)))

        # Check if current player has won
        if is_winner(current_state, 'X'):
            final_state = current_state
            winner = 'X'
            break
        if is_winner(current_state, 'O'):
            final_state = current_state
            winner = 'O'
            break

        # Check for draw
        if all(all(cell != ' ' for cell in row) for row in current_state):
            final_state = current_state
            winner = 'Draw'
            break

        # Generate successor states
        moves = generate_moves(current_state, current_player)
        next_player = 'O' if current_player == 'X' else 'X'
        queue.extend((move, next_player) for move in moves)

    # Print final state
    print("Final State:")
    for row in final_state:
        print(" | ".join(row))
        print("-" * 10)
    print("Winner:", winner)

bfs_tic_tac_toe()
