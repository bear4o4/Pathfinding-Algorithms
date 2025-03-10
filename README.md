# A* Pathfinding Algorithm

This repository contains an implementation of the A* search algorithm for finding the shortest path on a 5x5 grid. The algorithm uses the Manhattan distance as the heuristic to efficiently find the optimal path from a start point to a goal while avoiding obstacles.

## Features

- **A* Search Algorithm**: Implements the A* search algorithm to find the shortest path on a grid.
- **Manhattan Distance Heuristic**: Uses the Manhattan distance to estimate the cost from any node to the goal.
- **Obstacle Handling**: Allows specifying obstacles on the grid that the path must avoid.
- **Customizable Grid Size**: Easily adaptable to different grid sizes.

## Usage

### Input

- **Grid**: A 5x5 grid represented as a 2D list.
- **Start Point**: A tuple representing the starting coordinates `(row, column)`.
- **Goal Point**: A tuple representing the goal coordinates `(row, column)`.
- **Obstacles**: A list of tuples representing the coordinates of obstacles on the grid.

### Output

- **Shortest Path**: A list of coordinates representing the shortest path from the start to the goal, or "No path" if no path exists.

### Example

```python
grid = [[0] * 5 for _ in range(5)]  # 5x5 grid
start = (0, 0)
goal = (4, 4)
obstacles = [(1, 1), (2, 2), (3, 3)]

# Find the shortest path
path = a_star_search(grid, start, goal, obstacles)
print("Shortest Path:", path)
