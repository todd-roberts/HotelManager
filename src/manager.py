import pygame
from utils import ft_to_pix
from constants import screenWidth, screenHeight

class Manager:
    CHECK_IN_STATE = 'check in interaction'

    def __init__(self, loc_ft, rad_ft, speed_ft_s, current_room):
        self.loc = [ft_to_pix(loc_ft[0]), ft_to_pix(loc_ft[1])]
        self.rad = ft_to_pix(rad_ft)
        self.speed = ft_to_pix(speed_ft_s) / 60
        self.current_room = current_room
        self.set_bounds(self.current_room)
        self.current_door = None
        self.movement = {'up': False, 'down': False, 'left': False, 'right': False}
        self.interactable_state = None
        self.screen_center = [screenWidth/2, screenHeight/2]

    def set_bounds(self, space):
        self.pos_x_bnd = space.loc[0] + space.size[0]
        self.neg_x_bnd = space.loc[0]
        self.pos_y_bnd = space.loc[1] + space.size[1]
        self.neg_y_bnd = space.loc[1]

    def set_movement(self, direction, is_moving):
        self.movement[direction] = is_moving

    def move(self):
        if self.movement['up']:
            self.loc[1] -= self.speed
        if self.movement['down']:
            self.loc[1] += self.speed
        if self.movement['left']:
            self.loc[0] -= self.speed
        if self.movement['right']:
            self.loc[0] += self.speed

    def update(self):
        self.move()

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.screen_center[0], self.screen_center[1]), int(self.rad))
    
    def get_offset(self):
        return [self.screen_center[0] - self.loc[0], self.screen_center[1] - self.loc[1]]
