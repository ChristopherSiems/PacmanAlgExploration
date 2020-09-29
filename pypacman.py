#!/usr/bin/env python3
# Pygame template - skeleton for a new pygame project
import pygame
import random
import time
import math
import os


SCATTER = { "red": (1,1) ,
            "blue": (26,1),
            "yellow": (1,29),
            "pink": (26,29)
}

PACMAN_TIMERS = {
    "normal": 999999999,
    "chase": 8
}
GHOST_TIMERS = {
    "red": {
        "jail": 2,
        "scatter": 10,
        "chase": 15,
        "random": 10
    },
    "blue": {
        "jail": 3,
        "scatter": 8,
        "chase": 15,
        "random": 10
    },
    "yellow": {
        "jail": 5,
        "scatter": 10,
        "chase": 15,
        "random": 10
    },
    "pink": {
        "jail": 6,
        "scatter": 12,
        "chase": 15,
        "random": 10
    }    
}

MAP = [     [52, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 53, 52, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 53], 
            [50,  2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2, 51],
            [50,  1, 34, 32, 32, 35,  1, 34, 32, 32, 32, 35,  1, 33, 33,  1, 34, 32, 32, 32, 35,  1, 34, 32, 32, 35,  1, 51],
            [50,  1, 33,  0,  0, 33,  1, 33,  0,  0,  0, 33,  1, 33, 33,  1, 33,  0,  0,  0, 33,  1, 33,  0,  0, 33,  1, 51],
            [50,  1, 36, 32, 32, 37,  1, 36, 32, 32, 32, 37,  1, 36, 37,  1, 36, 32, 32, 32, 37,  1, 36, 32, 32, 37,  1, 51],
            [50,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 51],
            [50,  1, 34, 32, 32, 35,  1, 34, 35,  1, 34, 32, 32, 32, 32, 32, 32, 35,  1, 34, 35,  1, 34, 32, 32, 35,  1, 51],
            [50,  1, 36, 32, 32, 37,  1, 33, 33,  1, 36, 32, 32, 35, 34, 32, 32, 37,  1, 33, 33,  1, 36, 32, 32, 37,  1, 51],
            [50,  1,  1,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1,  1,  1, 51],
            [54, 49, 49, 49, 49, 57,  1, 33, 36, 32, 32, 35,  1, 33, 33,  1, 34, 32, 32, 37, 33,  1, 56, 49, 49, 49, 49, 55],
            [ 0,  0,  0,  0,  0, 50,  1, 33, 34, 32, 32, 37,  1, 36, 37,  1, 36, 32, 32, 35, 33,  1, 51,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0, 50,  1, 33, 33,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 33, 33,  1, 51,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0, 50,  1, 33, 33,  1, 56, 49, 49, 17, 17, 49, 49, 57,  1, 33, 33,  1, 51,  0,  0,  0,  0,  0],
            [48, 48, 48, 48, 48, 58,  1, 36, 37,  1, 51, 64,  0,  0,  0,  0, 64, 50,  1, 36, 37,  1, 59, 48, 48, 48, 48, 48],
            [ 0,  0,  0,  0,  0,  0,  1,  1,  1,  1, 51, 64,  0,  0,  0,  0, 64, 50,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0],
            [49, 49, 49, 49, 49, 57,  1, 34, 35,  1, 51, 64,  0,  0,  0,  0, 64, 50,  1, 34, 35,  1, 56, 49, 49, 49, 49, 49],
            [ 0,  0,  0,  0,  0, 50,  1, 33, 33,  1, 59, 48, 48, 48, 48, 48, 48, 58,  1, 33, 33,  1, 51,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0, 50,  1, 33, 33,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 33, 33,  1, 51,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0, 50,  1, 33, 33,  1, 34, 32, 32, 32, 32, 32, 32, 35,  1, 33, 33,  1, 51,  0,  0,  0,  0,  0],
            [52, 48, 48, 48, 48, 58,  1, 36, 37,  1, 36, 32, 32, 35, 34, 32, 32, 37,  1, 36, 37,  1, 59, 48, 48, 48, 48, 53],
            [50,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 51],
            [50,  1, 34, 32, 32, 35,  1, 34, 32, 32, 32, 35,  1, 33, 33,  1, 34, 32, 32, 32, 35,  1, 34, 32, 32, 35,  1, 51],
            [50,  1, 36, 32, 35, 33,  1, 36, 32, 32, 32, 37,  1, 36, 37,  1, 36, 32, 32, 32, 37,  1, 33, 34, 32, 37,  1, 51],
            [50,  1,  1,  1, 33, 33,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 33, 33,  1,  1,  1, 51],
            [54, 32, 35,  1, 33, 33,  1, 34, 35,  1, 34, 32, 32, 32, 32, 32, 32, 35,  1, 34, 35,  1, 33, 33,  1, 34, 32, 55],
            [52, 32, 37,  1, 36, 37,  1, 33, 33,  1, 36, 32, 32, 35, 34, 32, 32, 37,  1, 33, 33,  1, 36, 37,  1, 36, 32, 53],
            [50,  1,  1,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1, 33, 33,  1,  1,  1,  1,  1,  1, 51],
            [50,  1, 34, 32, 32, 32, 32, 37, 36, 32, 32, 35,  1, 33, 33,  1, 34, 32, 32, 37, 36, 32, 32, 32, 32, 35,  1, 51], 
            [50,  1, 36, 32, 32, 32, 32, 32, 32, 32, 32, 37,  1, 36, 37,  1, 36, 32, 32, 32, 32, 32, 32, 32, 32, 37,  1, 51], 
            [50,  2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1 , 2 ,51], 
            [54, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 55], 
    ]

FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# count number of pacgums in map
def count_pacgums():
    y_length = len(MAP)
    x_length = len(MAP[0])
    pacgums = 0
    for y in range(y_length):
        for x in range(x_length):
            if MAP[y][x] in (1,2):
                pacgums += 1

    return pacgums


def display_map():
    y_length = len(MAP)
    x_length = len(MAP[0])
    for y in range(y_length):
        for x in range(x_length):
            c=MAP[y][x]
            if c in walls:
                surface.blit(walls[c],(x*24,y*24))
    
def collided():
    # See if the player block has collided with anything.
    hit_list = pygame.sprite.spritecollide(pacman, all_ghosts, False, pygame.sprite.collide_circle)
 
    return hit_list


class Pacman(pygame.sprite.Sprite):
    "pacman management"
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.reinit(x,y)

    def reinit(self,x,y):
        self.x = x
        self.y = y

        self.image = Pacman_pics['left'][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * 24 + 12 , self.y * 24 + 12)
        self.speed = 4
        self.direction = ""
        self.mode = "normal"
        self.allowed_moves = []
        self.count_moves = 0

        # for the timers
        self.start_time = time.time()
        self.mode_changed = False

        # for collisions
        self.radius = 6

    # Check what moves are allowed from this position
    def get_allowed_moves(self):
        self.allowed_moves = []

        # check walls
        if MAP[self.y][self.x-1] < 16:
            self.allowed_moves.append("left")
        if (self.x+1 < 28 and MAP[self.y][self.x+1] < 16) or (self.x == 27 and self.direction =="right"):
            self.allowed_moves.append("right")
        if MAP[self.y - 1][self.x] < 16:
            self.allowed_moves.append("up")
        if MAP[self.y + 1][self.x] < 16:
            self.allowed_moves.append("down")

    # Do we ate something ? Remove it from map, increment score, and could be mega pacgum
    def check_pacgums(self):
        global score
        global pacgums

        chase = False
        # Single pacgum : 10
        if MAP[self.y][self.x] ==1:
            score = score + 10
            MAP[self.y][self.x] = 0
            pacgums = pacgums - 1

        # Big pacgum : 50 It's time to chase !
        if MAP[self.y][self.x] == 2:
            score += 50
            MAP[self.y][self.x] = 0
            pacgums -= 1
            chase = True 

        return chase

    def change_mode(self):

        self.mode_changed = False
        current_time = time.time()

        # Enter chase mode 
        if self.check_pacgums():
            self.mode = "chase"
            self.start_time = current_time
            self.speed = 6
            self.mode_changed = True
            for ghost in Ghosts:
                ghost.change_mode("runaway")

        # rotate between modes based on timer
        else:
            mode_time = PACMAN_TIMERS[self.mode]
            if current_time - self.start_time > mode_time:
                if self.mode == "chase":
                    self.mode = "normal"
                    self.speed = 4
                self.start_time = current_time
                self.mode_changed = True

        if self.mode_changed:
            print("Pacman mode changed to",self.mode)
        
    # move pacman
    def update(self):

        # Choose a direction only when we're on a MAP coordinates
        if self.rect.x % 24 == 0 and self.rect.y % 24 == 0:
            self.x = int(self.rect.x / 24)
            self.y = int(self.rect.y / 24)

            self.change_mode()

            self.get_allowed_moves()

            keys=pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                if MAP[self.y][self.x-1] < 16:
                    self.direction = "left"
            if keys[pygame.K_RIGHT]:
                if self.x+1 <28 and MAP[self.y][self.x+1] < 16:
                    self.direction = "right"
            if keys[pygame.K_UP]:
                if MAP[self.y - 1][self.x] < 16:
                    self.direction = "up"
            if keys[pygame.K_DOWN]:
                if self.y + 1 < 30 and MAP[self.y + 1][self.x] < 16:
                    self.direction = "down"

        #print("Pacman: self.x=",self.x, "self.y=",self.y, "allowed_moves=",self.allowed_moves)
        # Direction is set : move the ghost
        moved = False

        if self.direction == "left" and "left" in self.allowed_moves:
            self.rect.x -= self.speed
            moved = True
            # go to right border
            if self.rect.x < 0:
                self.rect.x = WIDTH-24

        if self.direction == "right" and "right" in self.allowed_moves:
            self.rect.x += self.speed
            moved = True
            # go to left border
            if self.rect.x > WIDTH-24:
                self.rect.x = 0

        if self.direction == "up" and "up" in self.allowed_moves:
            self.rect.y -= self.speed
            moved = True
            if self.rect.y < 0:
                self.rect.y = HEIGHT-24

        if self.direction == "down" and "down" in self.allowed_moves:
            self.rect.y += self.speed
            moved = True
            if self.rect.y > HEIGHT-24:
                self.rect.y = 0

        if moved:
            self.count_moves += 1

        if self.direction:
            if moved:
                self.image = Pacman_pics[self.direction][self.count_moves % 3 + 1]
            else:
                self.image = Pacman_pics[self.direction][2]                
            self.image.set_colorkey(BLACK)

class Ghost(pygame.sprite.Sprite):

    moves = ["left","right","up","down"]
    opposite = ["right", "left", "down", "up" ]

    def __init__(self, x, y, color, mode):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.reinit(x,y,mode)

    def reinit(self,x,y,mode):
        self.x = x
        self.y = y

        self.mode = mode
        self.old_mode = ""
        self.distances = dict()
        self.allowed_moves = []
        self.forbid_turnback = True
        self.direction = ""
        self.speed = 4
        self.count_moves = 0

        # for collisions
        self.radius = 6

        # for the timers
        self.start_time = time.time()
        self.mode_changed = False

        self.image = Ghost_pics[self.color]['left'][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * 24 +12 , self.y * 24 + 12)

    # In chase or runaway modes, we calculate distance between ghost and pacman
    def distance_based_direction(self):
        x = self.x
        y = self.y
        self.distances = dict()

        # Previously in jail: target just outside jail to go outside
        if self.old_mode == "jail":
            x_target = 14
            y_target = 11
            # We're outside : go to normal coordinates
            if self.y <= 11:
                self.old_mode = ""
               
        elif self.mode == "scatter":
            x_target = SCATTER[self.color][0]
            y_target = SCATTER[self.color][1]
        else:
            x_target = pacman.x
            y_target = pacman.y

        # We calculate for each possible moves
        for direction in self.allowed_moves:
            x = self.x
            y = self.y
            if direction == "up":
                y = self.y - 1
            elif direction == "down":
                y = self.y + 1
            elif direction == "left":
                x = self.x - 1
            else:
                # right
                x = self.x + 1
            
            # Pythagore, of course
            dist_x = abs(x - x_target)
            dist_y = abs(y - y_target)
            distance = round(math.sqrt(dist_x*dist_x + dist_y*dist_y))
#            distance = math.sqrt(dist_x*dist_x + dist_y*dist_y)
            self.distances[direction] = distance

        if self.mode == "chase" or self.mode == "scatter":
            min = 99999999999
        elif self.mode == "runaway":
            min = -1

        for key, value in self.distances.items():
            # In chase mode : select the nearest direction
            if self.mode == "chase" or self.mode == "scatter":
                if value < min:
                    min = value
                    self.direction = key
            # In run away mode: select the farthest direction
            elif self.mode == "runaway":
                if value > min:
                    min = value
                    self.direction = key

    # Direction is choosen in allowed directions
    def choose_direction(self):
        if self.mode == "random" or self.mode == "jail":
            self.direction=random.choice(self.allowed_moves)
        elif self.mode == "chase" or self.mode == "runaway" or self.mode == "scatter":
            self.distance_based_direction()

    # Checks the free positions around the ghost
    def get_allowed_moves(self):
        self.allowed_moves = []

        # check walls
        if MAP[self.y][self.x-1] < 16:
            self.allowed_moves.append("left")
        if self.x+1 < 28 and MAP[self.y][self.x+1] < 16:
            self.allowed_moves.append("right")
        # if in jail, and no more in jail mode, we can go outside
        if MAP[self.y - 1][self.x] < 16 or (self.mode != "jail" and MAP[self.y - 1][self.x] == 17):
            self.allowed_moves.append("up")
        if MAP[self.y + 1][self.x] < 16:
            self.allowed_moves.append("down")

        # Remove opposition direction By default : no turn back
        if self.forbid_turnback and self.direction != '':
            reverse=self.opposite[self.moves.index(self.direction)]
            if reverse in self.allowed_moves:
                self.allowed_moves.remove(reverse)

    # Check time spent in current mode then change it based on a timer
    def change_mode(self,mode = False):

        current_time = time.time()

        if mode == "runaway":
            # start time of runaway is aways the same as pacman in chase
            self.start_time = pacman.start_time 
            self.old_mode = self.mode
            self.mode = "runaway"
            self.mode_changed = True
            #self.get_allowed_moves()
            #self.choose_direction()
        else: 
            # rotate between modes
            mode_time = GHOST_TIMERS[self.color][self.mode]
            if current_time - self.start_time > mode_time:
                self.old_mode = self.mode
                if self.mode == "jail":
                    self.mode = "scatter"
                elif self.mode == "scatter":
                    self.mode = "chase"
                elif self.mode == "chase":
                    self.mode = "scatter"
                elif self.mode == "runaway":
                    self.mode = "jail"
                    GHOST_TIMERS[self.color]['jail'] = 0
                self.start_time = current_time
                self.mode_changed = True
            else:
                self.mode_changed = False

        if self.mode_changed:
            self.forbid_turnback = False
            print(self.color,"mode changed to ",self.mode)

    # main function
    def update(self):

        # change mode based on timer
        self.change_mode()

        # Choose a direction only when we're on a MAP coordinates
        if self.rect.x % 24 == 0 and self.rect.y % 24 == 0:
            self.x = int(self.rect.x / 24)
            self.y = int(self.rect.y / 24)

            # We moved one case
            self.count_moves += 1

            # What are the allowed moves ?
            self.get_allowed_moves()

            # choose a direction, based on the ghost mode
            self.choose_direction()

            # change mode alreay done, directino alreay set, we can forbid
            self.forbid_turnback = True

        # Direction is set : move the ghost
        if self.direction == "left":
            self.rect.x -= self.speed
            # go to right border
            if self.rect.x < 0:
                self.rect.x = WIDTH-12

        if self.direction == "right":
            self.rect.x += self.speed
            # go to left border
            if self.rect.x > WIDTH-12:
                self.rect.x = 0

        if self.direction == "up":
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = HEIGHT-12

        if self.direction == "down":
            self.rect.y += self.speed
            if self.rect.y > HEIGHT-12:
                self.rect.y = 0

        if self.mode == "runaway":
            current_time = time.time()
            if GHOST_TIMERS[self.color]['runaway'] - (current_time - self.start_time) < 3:
                self.image = Frightened_ghost_blinking[self.count_moves % 4 + 1] 
            else:
                self.image = Frightened_ghost[self.count_moves % 2 + 1] 
        else:
            self.image = Ghost_pics[self.color][self.direction][self.count_moves % 2 + 1] 
        self.image.set_colorkey(BLACK)

        # For debug
        #print("color=",self.color, "map_x=",self.x, "map_y=",self.y,"x=",self.rect.x,"y=",self.rect.y, "old mode=",self.old_mode, "mode=",self.mode, "f.direction=", self.direction, "allowed_moves=",self.allowed_moves, "distances=",self.distances)

# Display text in center
def display_text(surface, my_text):
    font = pygame.font.Font('freesansbold.ttf', 32)   
    text = font.render(my_text, True, WHITE) 
    textRect = text.get_rect()  
    textRect.center = (int(WIDTH / 2), int(HEIGHT / 2)) 
    surface.blit(text, textRect)

def load_bitmaps():
    global Pacman_pics
    global Dead_pacman
    global Ghost_pics
    global Frightened_ghost
    global Frightened_ghost_blinking
    global walls

    # load ghost pictures
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'img')

    Frightened_ghost = dict()
    Frightened_ghost[1] = pygame.image.load(os.path.join(img_folder, 'frightened_ghost_1.png')).convert()
    Frightened_ghost[2] = pygame.image.load(os.path.join(img_folder, 'frightened_ghost_2.png')).convert()

    Frightened_ghost_blinking = dict()
    Frightened_ghost_blinking[1] = Frightened_ghost[1]
    Frightened_ghost_blinking[2] = pygame.image.load(os.path.join(img_folder, 'frightened_ghost_3.png')).convert()
    Frightened_ghost_blinking[3] = Frightened_ghost[2]
    Frightened_ghost_blinking[4] = pygame.image.load(os.path.join(img_folder, 'frightened_ghost_4.png')).convert()

    Ghost_pics = dict()
    for color in ('red','yellow','blue','pink'):
        Ghost_pics[color] = dict()
        for direction in ('left','right','up','down'):
            Ghost_pics[color][direction] = dict()
            for i in range(1,3):
                Ghost_pics[color][direction][i] = pygame.image.load(os.path.join(img_folder, color+'_'+direction+'_ghost_'+str(i)+'.png')).convert()

    # load pacman pictures
    Pacman_pics = dict()
    for direction in ('left','right','up','down'):
        Pacman_pics[direction] = dict()
        for i in range(1,4):
            Pacman_pics[direction][i] = pygame.image.load(os.path.join(img_folder, 'pacman_'+direction+'_'+str(i)+'.png')).convert()

    # load dead pacman pictures
    Dead_pacman = dict()
    for i in range(1,11):
        Dead_pacman[i] = pygame.image.load(os.path.join(img_folder, 'pacman_dead_'+str(i)+'.png')).convert()

    # load walls based on values in MAP and if associated png exists
    walls = dict()
    for l in MAP:
        for c in l:
            if c not in walls:
                png = os.path.join(img_folder, str(c) + ".png")
                if(os.path.exists(png)):
                    walls[c] = pygame.image.load(png).convert()

def display_lifes(surface):
    for live in range(0, lifes - 1 ):
        surface.blit(Pacman_pics['right'][2],(live*32+24,4))

def play():
    global score
    global lifes
    global scale

    clock = pygame.time.Clock()
    # Game loop
    running = True
    while running:

        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        pacman.update()
        all_ghosts.update()

        display_board_game()

#        frame = scale_output(fake_screen, scale)

        # Everything on screen
        screen.blit(scale_output(fake_screen, scale), (0, 0))

        # *after* drawing everything, flip the display
        pygame.display.flip()


        # Collision test
        hit_list = collided()
        if hit_list:
            if pacman.mode == "chase":
                for ghost in hit_list:
                    if ghost.mode == "runaway":
                        ghost.x = 14
                        ghost.y = 15
                        ghost.rect.center = (ghost.x * 24 + 12 , ghost.y * 24 + 12)
                        ghost.mode = "jail"
                        GHOST_TIMERS[ghost.color]['jail'] = random.randint(1,10)
                        score += 200
                    else:
                        lifes -= 1
                        loose_life()
            else:
                lifes -= 1
                loose_life()

        # Won ?
        if pacgums == 0:
            running = False

        if lifes == 0:
            running = False

def display_board_game():
    # Draw all
    surface.fill(BLACK)
    top.fill(BLACK)
    bottom.fill(BLACK)

    # draw walls
    display_map()

    # Draw sprites
    all_sprites.draw(surface)

    display_lifes(bottom)
    fake_screen.blit(top,(0,0))
    fake_screen.blit(surface,(0,32))
    fake_screen.blit(bottom,(0,HEIGHT+32))

def loose_life():
    global scale

    i = 1
    while i<10:
        print("In loop",i)
        time.sleep(0.1)

        # evaluate the pygame event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        # Draw all
        surface.fill(BLACK)
        top.fill(BLACK)
        bottom.fill(BLACK)

        # draw walls
        display_map()

        # Animate the dead pacman
        surface.blit(Dead_pacman[i], (pacman.rect.x, pacman.rect.y))
        display_lifes(bottom)
        fake_screen.blit(top,(0,0))
        fake_screen.blit(surface,(0,32))
        fake_screen.blit(bottom,(0,HEIGHT+32))

        screen.blit(scale_output(fake_screen, scale), (0, 0))

        # *after* drawing everything, flip the display
        pygame.display.flip()
        i += 1
    
    # Reinit everything
    pacman.reinit(14,17)
    for ghost in Ghosts:
        if ghost.color == "red":
            ghost.reinit(14,14,"jail")
        if ghost.color == "blue":
            ghost.reinit(13,14,"jail")
        if ghost.color == "yellow":
            ghost.reinit(13,14,"jail")
        if ghost.color == "pink":
            ghost.reinit(15,14,"jail")

def scale_output(my_surface,scale):
    # Scale ?
    if scale != 1:
        frame = pygame.transform.scale(my_surface, (int(FULL_WIDTH*scale), int(FULL_HEIGHT*scale)))
    else:
        frame = my_surface
    return frame
 
# Root code
def main():

    global pacman
    global all_ghosts
    global all_sprites
    global screen, fake_screen
    global Ghosts
    global surface, top, bottom
    global score
    global pacgums
    global scale
    global lifes
    global WIDTH, HEIGHT, FULL_WIDTH, FULL_HEIGHT

    WIDTH = len(MAP[0])*24
    HEIGHT = len(MAP)*24

    FULL_WIDTH = WIDTH
    FULL_HEIGHT = HEIGHT + 64 

    lifes = 3

    pacgums = count_pacgums()
    score = 0

    scale = 1

    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()

    # Check vertical resolution
    display_infos = pygame.display.Info()

    y_resolution = display_infos.current_h

    if y_resolution < 800:
        scale = 0.75


    screen = pygame.display.set_mode((int(FULL_WIDTH*scale), int(FULL_HEIGHT*scale)))
    fake_screen = pygame.Surface((FULL_WIDTH, FULL_HEIGHT))
    pygame.display.set_caption("Pacman by Slyce")
    
    # create a surface to work on
    surface = pygame.Surface((WIDTH, HEIGHT))
    top = pygame.Surface((WIDTH, 32))
    bottom = pygame.Surface((WIDTH, 32))

    # load bitmaps                                                                                                                               
    load_bitmaps()

    # declare sprites
    all_sprites = pygame.sprite.Group()
    all_ghosts = pygame.sprite.Group()

    Ghosts = []
    # declare the four ghosts
    Ghosts.append(Ghost(14,14, "red", "jail"))
    Ghosts.append(Ghost(13,14, "blue", "jail"))
    Ghosts.append(Ghost(13,14, "yellow","jail"))
    Ghosts.append(Ghost(15,14, "pink","jail"))


    # Prepare runaway values
    for ghost in Ghosts:
        GHOST_TIMERS[ghost.color]['runaway'] = PACMAN_TIMERS['chase']

    # declare pacman
    pacman = Pacman(14, 17)

    all_sprites.add(pacman)
    all_sprites.add(Ghosts)
    all_ghosts.add(Ghosts)

    play()
        
    print("Remaining pacgums:", pacgums)
    print("Score:", score)

    pygame.quit()

if __name__ == "__main__":
    # execute only if run as a script
    main()
