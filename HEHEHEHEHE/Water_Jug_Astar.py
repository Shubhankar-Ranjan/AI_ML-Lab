import heapq

def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar(start, goal, capacity1, capacity2):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            break
        for next in [(current[0], capacity2), 
                    (current[0], 0), 
                    (capacity1, current[1]), 
                    (0, current[1]), 
                    (current[0] - min(current[0], capacity2 - current[1]), current[1] + min(current[0], capacity2 - current[1])), 
                    (current[0] + min(current[1], capacity1 - current[0]), current[1] - min(current[1], capacity1 - current[0]))]:
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(pq, (priority, next))
                came_from[next] = current
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

capacity1 = int(input("Enter the capacity of the first jug: "))
capacity2 = int(input("Enter the capacity of the second jug: "))
target1 = int(input("Enter the target amount for the first jug: "))
target2 = int(input("Enter the target amount for the second jug: "))

start = (0, 0)
goal = (target1, target2)
came_from, cost_so_far = astar(start, goal, capacity1, capacity2)
path = reconstruct_path(came_from, start, goal)
print(path)