# How this code works?
# This Python code is an implementation of the best-first search algorithm to solve the 8-puzzle problem. Here's a breakdown of how it works:

# Heuristic Function: The heuristic function calculates the Manhattan distance, which is the sum of the distances of each tile from its target position. This is used as the heuristic to guide the search.

# Find Function: The find function locates the position of a given number in the puzzle.

# Solve Function: The solve function is where the best-first search algorithm is implemented. It maintains a priority queue of puzzles to explore, with the priority determined by the heuristic function. The puzzle with the lowest heuristic value (i.e., the one that is closest to the target) is explored first.

# The function starts by adding the initial puzzle to the queue.
# Then it enters a loop that continues until the queue is empty or the puzzle is solved.
# In each iteration of the loop, it removes the puzzle with the lowest heuristic value from the queue.
# If this puzzle is the target, it returns the path of moves used to reach this state.
# Otherwise, it generates all possible next states by moving the blank tile up, down, left, or right. Each of these states is added to the queue to be explored later.
# To avoid exploring the same state multiple times, it keeps a set of visited states.
# Example Usage: The last part of the code creates an example puzzle and target, and then calls the solve function to solve the puzzle. The solution is then printed to the console.

# The output of the program is a string of moves (e.g., "DR") that transforms the initial puzzle into the target puzzle. If no solution is found, it returns "No solution".
import heapq

def heuristic(puzzle, target):
    return sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in ((find(puzzle, i), find(target, i)) for i in range(1, 9)))

def find(matrix, num):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == num:
                return i, j

def solve(puzzle, target):
    queue = [(heuristic(puzzle, target), puzzle, "")]
    heapq.heapify(queue)
    visited = set()
    while queue:
        (h, puzzle, path) = heapq.heappop(queue)
        if puzzle == target:
            return path
        for (d, move) in (((-1, 0), "U"), ((1, 0), "D"), ((0, -1), "L"), ((0, 1), "R")):
            new_puzzle = [row[:] for row in puzzle]
            i, j = find(new_puzzle, 0)
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_puzzle[i][j], new_puzzle[ni][nj] = new_puzzle[ni][nj], new_puzzle[i][j]
                if str(new_puzzle) not in visited:
                    visited.add(str(new_puzzle))
                    heapq.heappush(queue, (heuristic(new_puzzle, target), new_puzzle, path + move))
    return "No solution"

# Example usage:
puzzle = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
target = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(solve(puzzle, target))

puzzle = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
target = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
print(solve(puzzle, target))
