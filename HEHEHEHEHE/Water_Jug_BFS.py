from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target1, target2):
    visited = set()
    queue = deque([((0,0), [])])

    while queue:
        (jug1, jug2), path = queue.popleft()

        if(jug1, jug2) == (target1, target2):
            return path + [(jug1, jug2)]
        
        if(jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        #Fill jug1
        queue.append(((jug1_capacity, jug2), path + [(jug1, jug2)]))

        #Fill jug2
        queue.append(((jug1, jug2_capacity), path + [(jug1, jug2)]))

        #Empty jug1
        queue.append(((0, jug2), path + [(jug1, jug2)]))

        #Empty jug2
        queue.append(((jug1, 0), path + [(jug1, jug2)]))

        #Pour from jug1 to jug2
        queue.append(((jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)), path + [(jug1, jug2)]))

        #Pour from jug2 to jug1
        queue.append(((jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)), path + [(jug1, jug2)]))
    
    return None

jug1_capacity = int(input("Enter jug1 capacity: "))
jug2_capacity = int(input("Enter jug2 capacity: "))
target1 = int(input("Enter target amount for jug1: "))
target2 = int(input("Enter target amount for jug2: "))

ans = water_jug_bfs(jug1_capacity, jug2_capacity, target1, target2)

print(ans);