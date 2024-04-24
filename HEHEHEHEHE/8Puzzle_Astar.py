from queue import PriorityQueue

def h(puzzle, target):
    # Heuristic function: number of misplaced tiles
    return sum(p != t for row_p, row_t in zip(puzzle, target) for p, t in zip(row_p, row_t) if p != 0)

def solve(puzzle, target):
    # A* algorithm
    queue = PriorityQueue()
    queue.put((0, puzzle))
    came_from = {str(puzzle): None}
    cost_so_far = {str(puzzle): 0}
    while not queue.empty():
        _, current = queue.get()
        if current == target:
            break
        for next in neighbors(current):
            new_cost = cost_so_far[str(current)] + 1
            if str(next) not in cost_so_far or new_cost < cost_so_far[str(next)]:
                cost_so_far[str(next)] = new_cost
                priority = new_cost + h(next, target)
                queue.put((priority, next))
                came_from[str(next)] = current
    return came_from, cost_so_far

def neighbors(puzzle):
    # Generate all possible neighbors
    def swap(p, i, j, new_i, new_j):
        p = [list(row) for row in p]
        p[i][j], p[new_i][new_j] = p[new_i][new_j], p[i][j]
        return tuple(map(tuple, p))
    i, j = [(i, row.index(0)) for i, row in enumerate(puzzle) if 0 in row][0]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in directions:
        if 0 <= i + di < 3 and 0 <= j + dj < 3:
            yield swap(puzzle, i, j, i + di, j + dj)

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[str(current)]
    path.append(start) 
    path.reverse() 
    return path

# Example usage:
puzzle = ((1, 2, 5), (3, 4, 0), (6, 7, 8))
target = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
came_from, cost_so_far = solve(puzzle, target)
path = reconstruct_path(came_from, puzzle, target)

# Print the solution path
for state in path:
    for row in state:
        print(row)
    print()