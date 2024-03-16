class PacMan:
    def __init__(self, maze):
        self.maze = maze
        self.position = self.find_start_position()
        self.direction = 'left'
        self.game_over = False

    def find_start_position(self):
        # Find Pac-Man's starting position in the maze
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 'P':
                    return i, j
        return None

    def can_move(self, x, y):
        # Check if Pac-Man can move to the given position
        if 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]):
            return self.maze[x][y] != '#'
        return False

    def move(self):
        # Move Pac-Man according to the counter-clockwise algorithm
        if self.game_over:
            return False

        x, y = self.position
        if self.direction == 'left':
            if self.can_move(x, y - 1):
                self.position = (x, y - 1)
                self.direction = 'up'
            elif self.can_move(x - 1, y):
                self.position = (x - 1, y)
            elif self.can_move(x, y + 1):
                self.position = (x, y + 1)
                self.direction = 'down'
            else:
                self.game_over = True
        elif self.direction == 'up':
            if self.can_move(x - 1, y):
                self.position = (x - 1, y)
            elif self.can_move(x, y + 1):
                self.position = (x, y + 1)
                self.direction = 'down'
            elif self.can_move(x + 1, y):
                self.position = (x + 1, y)
                self.direction = 'right'
            else:
                self.game_over = True
        elif self.direction == 'down':
            if self.can_move(x + 1, y):
                self.position = (x + 1, y)
                self.direction = 'right'
            elif self.can_move(x, y - 1):
                self.position = (x, y - 1)
            elif self.can_move(x - 1, y):
                self.position = (x - 1, y)
                self.direction = 'up'
            else:
                self.game_over = True
        elif self.direction == 'right':
            if self.can_move(x, y + 1):
                self.position = (x, y + 1)
                self.direction = 'down'
            elif self.can_move(x + 1, y):
                self.position = (x + 1, y)
                self.direction = 'right'
            elif self.can_move(x, y - 1):
                self.position = (x, y - 1)
                self.direction = 'up'
            else:
                self.game_over = True
        return not self.game_over

# Example usage:
maze = [
    ['#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '.', 'P', '.', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#']
]

pacman = PacMan(maze)

while pacman.move():
    print("Pac-Man's current position:", pacman.position)

if pacman.game_over:
    print("Game over! Pac-Man cannot move further.")
