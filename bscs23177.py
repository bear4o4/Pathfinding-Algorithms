import heapq
from collections import deque

#Part B

#Question 1:
def uniform_cost_search(grid, start, goal):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(0, start)]#cost, position
    costs = {start: 0}
    parents = {start: None}
    while queue:
        (current_cost, current_position) = heapq.heappop(queue)

        if current_position == goal:
            path = []
            while current_position is not None:
                path.append(current_position)
                current_position = parents[current_position]
            return path[::-1]


        for direction in directions:
            new_row = current_position[0] + direction[0]
            new_col = current_position[1] + direction[1]
            new_position = (new_row, new_col)

            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                new_cost = current_cost + grid[new_row][new_col]

                if new_position not in costs or new_cost < costs[new_position]:
                    costs[new_position] = new_cost
                    parents[new_position] = current_position
                    heapq.heappush(queue, (new_cost, new_position))
    return []

grid = [
    [1, 3, 1, 1],
    [1, 1, 1, 1],
    [1, 3, 5, 1],
    [1, 1, 1, 1]
]
start = (0, 0)
goal = (3, 3)
path = uniform_cost_search(grid, start, goal)
print(path)

print("##################")

#Question 2:
#check  state is valid missionaries are not outnumbered
def is_valid(state):
    M, C, _ = state
    return (M == 0 or M >= C) and ((3 - M) == 0 or (3 - M) >= (3 - C))

#check all vlaid next states
def get_next_states(state):
    M, C, B = state
    next_states = []
    for m in range(3):
        for c in range(3):
            if (m + c) in [1, 2]:
                if B == 1:
                    new_state = (M - m, C - c, 0)
                else:
                    new_state = (M + m, C + c, 1)
                if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3:
                    if is_valid(new_state):
                        next_states.append(new_state)
    return next_states

def solve_missionaries_and_cannibals():
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)

    queue = deque([(initial_state, [initial_state])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        if current_state not in visited:
            visited.add(current_state)
            for next_state in get_next_states(current_state):
                if next_state not in visited:
                    queue.append((next_state, path + [next_state]))

    return None

solution_path = solve_missionaries_and_cannibals()
print("Solution Path:", solution_path)

print("##################")

#Question 3:
#calculate ditance
def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal, obstacles):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = [(0 + heuristic(start, goal), 0, start)]#  cost + heuristic, cost, position
    costs = {start: 0}
    parents = {start: None}

    while queue:
        _, current_cost, current_position = heapq.heappop(queue)

        if current_position == goal:
            path = []
            while current_position is not None:
                path.append(current_position)
                current_position = parents[current_position]
            return path[::-1]

        for direction in directions:
            new_row = current_position[0] + direction[0]
            new_col = current_position[1] + direction[1]
            new_position = (new_row, new_col)
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and new_position not in obstacles:
                new_cost = current_cost + 1
                if new_position not in costs or new_cost < costs[new_position]:
                    costs[new_position] = new_cost
                    parents[new_position] = current_position
                    heapq.heappush(queue, (new_cost + heuristic(new_position, goal), new_cost, new_position))


    return "No path"

grid = [[0] * 5 for _ in range(5)]
start = (0, 0)
goal = (4, 4)
obstacles = [(1, 1), (2, 2), (3, 3)]
path = a_star_search(grid, start, goal, obstacles)
print("Shortest Path:", path)
