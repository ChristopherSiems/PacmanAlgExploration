import heapq

class AStar:

    game = None
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(self, node):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        for direction in directions:
            next_node = (node[0] + direction[0], node[1] + direction[1])
            if 0 <= next_node[0] < self.width and 0 <= next_node[1] < self.height and self.grid[next_node[1]][next_node[0]] <= 15:
                result.append(next_node)
        return result

    def search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while not len(frontier) == 0:
            current = heapq.heappop(frontier)[1]

            if current == goal:
                break

            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

        return self.reconstruct_path(came_from, start, goal)

    def cost(self, from_node, to_node):
        if self.grid[to_node[1]][to_node[0]] > 15:
            return float('inf')  
        return 1 

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)  
        path.reverse()  
        return path