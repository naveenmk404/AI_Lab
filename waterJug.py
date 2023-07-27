from collections import deque

def water_jug_problem(jug1, jug2, target):
    q, visited = deque([(0, 0, [])]), set()
    while q:
        x, y, path = q.popleft()
        if x == target or y == target:
            return path
        visited.add((x, y))
        for (nx, ny, action) in [(x, 0, 'Clear Y'), (0, y, 'Clear X'),
                                 (x, jug2, 'Fill Y'), (jug1, y, 'Fill X'), 
                                 (x - min(x, jug2 - y), y + min(x, jug2 - y), 'Pour X->Y'),
                                 (x + min(y, jug1 - x), y - min(y, jug1 - x), 'Pour Y->X')]:
            if (nx, ny) not in visited:
                q.append((nx, ny, path + [action]))
    return None

# Example usage:
jug1_capacity=int(input("Enter jug1 capacity : "))
jug2_capacity = int(input("Enter jug2 capacity : "))
target_amount = int(input("Enter target to measure : "))

result = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

if result:
    print(f"Steps to measure {target_amount} liters: {result}")
else:
    print(f"Cannot measure {target_amount} liters with the given jug capacities.")

