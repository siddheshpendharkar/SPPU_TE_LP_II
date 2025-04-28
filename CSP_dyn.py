# Take input for colors
colors = input("Enter colors separated by space: ").split()

# Take input for states
states = input("Enter states separated by space: ").split()

# Take input for neighbors
neighbors = {}
for state in states:
    neighbor_list = input(f"Enter neighbors of {state} separated by space: ").split()
    neighbors[state] = neighbor_list

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state, []):
        if colors_of_states.get(neighbor) == color:
            return False
    return True

def backtrack(state_index):  
    if state_index == len(states):
        return True
    state = states[state_index]
    for color in colors:
        if promising(state, color):
            colors_of_states[state] = color
            if backtrack(state_index + 1):
                return True
            colors_of_states[state] = None
    return False

def main():
    if backtrack(0):
        print("\nColor assignment:")
        for state in states:
            print(f"{state}: {colors_of_states[state]}")
    else:
        print("No solution found.")

main()
