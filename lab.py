import heapq

# Helper function to find the position of 0 (blank tile)
def find_blank_tile(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

# Heuristic function: Number of misplaced tiles
def heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank_tile(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

g_score = {}
f_score = {}

# A* search algorithm with debug prints
def a_star_search(start_state):
    open_list = []
    heapq.heappush(open_list, (0, start_state))
    came_from = {}
    g_score[str(start_state)] = 0
    f_score[str(start_state)] = heuristic(start_state)

    while open_list:
        # Debug: Print the priority queue before popping
        print("Current states in the heap :  *************************")
        for item in open_list:
            print(f"f_value: {item[0]}, state:")
            for row in item[1]:
                print(row)
            print()
        print()
        
        input()
        
        _, current = heapq.heappop(open_list)

        if current == goal_state:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[str(current)] + 1
            if str(neighbor) not in g_score or tentative_g_score < g_score[str(neighbor)]:
                came_from[str(neighbor)] = current
                g_score[str(neighbor)] = tentative_g_score
                f_score[str(neighbor)] = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_list, (f_score[str(neighbor)], neighbor))
    return None

# Reconstruct the path from start to goal
def reconstruct_path(came_from, current):
    path = [current]
    while str(current) in came_from:
        current = came_from[str(current)]
        path.append(current)
    path.reverse()
    return path

# Test the algorithm
start_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
# Define the goal state
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

print("Initial State")
for step in start_state:
    print(step)
print()

print("Goal State")
for step in goal_state:
    print(step)
print()

solution = a_star_search(start_state)

# Print the solution steps
if solution:
    print("Solution found in {} steps:".format(len(solution) - 1))
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")