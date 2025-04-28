initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

def heuristic(state, goal_state):
    return sum(1 for i in range(9) if state[i] != goal_state[i] and state[i] != 0)

def get_successors(state):
    successors = []
    zero_index = state.index(0)
    moves = {
        "UP": -3, "DOWN": 3, "LEFT": -1, "RIGHT": 1
    }

    for move, shift in moves.items():
        new_index = zero_index + shift
        if 0 <= new_index < 9:
            if move == "LEFT" and zero_index % 3 == 0:
                continue
            if move == "RIGHT" and zero_index % 3 == 2:
                continue
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            successors.append((move, new_state))
    return successors

# A* Algorithm
def a_star(start, goal):
    open_list = [(start, 0, [], 0)]  # (state, g(n), path, level)
    visited = set()

    while open_list:
        # Find node with lowest f(n) = g + h
        current_index = 0
        lowest_f = float('inf')
        for i, (state, g, path, level) in enumerate(open_list):
            f = g + heuristic(state, goal)
            if f < lowest_f:
                lowest_f = f
                current_index = i

        current_state, g, path, level = open_list.pop(current_index)
        state_tuple = tuple(current_state)
        
        h_value = heuristic(current_state, goal)
        print(f"Level {level} - Current State: {current_state}")
        print(f"g(n) = {g}, h(n) = {h_value}, f(n) = {g + h_value}")
        print()

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current_state == goal:
            return path + [current_state]

        for move, next_state in get_successors(current_state):
            if tuple(next_state) not in visited:
                open_list.append((next_state, g + 1, path + [current_state], level + 1))

    return None

solution = a_star(initial_state, goal_state)

if solution:
    print("Steps to solve the puzzle:\n")
    for idx, step in enumerate(solution):
        print(f"Step {idx}:")
        for i in range(0, 9, 3):
            print(step[i:i+3])
        h_value = heuristic(step, goal_state)
        print(f"Misplaced Tiles Heuristic (h(n)) = {h_value}\n")
else:
    print("No solution found.")
