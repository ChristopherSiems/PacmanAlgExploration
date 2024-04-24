class Clockwise():
    
    game = None
    move_counter = 0
    def setup(self):
        pass
    
    def get_dir(self):
        poss_moves = self.game.pacman.allowed_moves
        current_dir = self.game.pacman.direction
        clockwise_dirs = ["up", "right", "down", "left"]
        opposite_dir_index = (clockwise_dirs.index(current_dir) + 2) % 4
        opposite_dir = clockwise_dirs[opposite_dir_index]
        
        if self.move_counter == 0:
            current_dir = 'right'
            self.move_counter += 1
            return current_dir
        
        elif poss_moves != ["left", "right"] and poss_moves != ["up", "down"]:
            
            filtered_dirs = [dir for dir in clockwise_dirs if dir != opposite_dir]
            for item in range(len(filtered_dirs)):
                next_dir_index = (clockwise_dirs.index(current_dir) + 1) % 4
                next_dir = clockwise_dirs[next_dir_index]
                if next_dir in poss_moves:
                    self.move_counter += 1
                current_dir = next_dir
                return current_dir
                    
        elif poss_moves == ["left", "right"] or poss_moves == ["up", "down"]:
            self.move_counter += 1
            return current_dir

        self.move_counter += 1
        return current_dir
        
            
        
        #Need to make code that makes sure p

                

    
            
