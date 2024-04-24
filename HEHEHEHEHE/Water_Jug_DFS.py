def water_jug_dfs(jug1_capacity, jug2_capacity, target1, target2):
    visited = set()
    stack =[((0,0), [])]

    while stack:
        (jug1, jug2), path = stack.pop()

        if(jug1, jug2) == (target1, target2):
            return path + [(jug1, jug2)]
        
        if(jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Fill jug1
        stack.append(((jug1_capacity, jug2), path + [(jug1, jug2)]))

        # Fill jug2
        stack.append(((jug1, jug2_capacity), path + [(jug1, jug2)]))

        # Empty jug1
        stack.append(((0, jug2), path + [(jug1, jug2)]))

        # Empty jug2
        stack.append(((jug1, 0), path + [(jug1, jug2)]))

        # Pour from jug1 to jug2
        stack.append(((jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug2, jug1_capacity - jug1)), path + [(jug1, jug2)]))

        # Pour from jug2 to jug1
        stack.append(((jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)), path + [(jug1, jug2)]))

    return None;

jug1_capacity = int(input("Enter jug1 capacity: "))
jug2_capacity = int(input("Enter jug2 capacity: "))
target1 = int(input("Enter target amount for jug1: "))
target2 = int(input("Enter target amount for jug2: "))

ans = water_jug_dfs(jug1_capacity, jug2_capacity, target1, target2)

print(ans);

