import pygame
from utils import ft_to_pix

class Room:
    def __init__(self, name, loc, size):
        self.name = name
        self.size = (ft_to_pix(size[0]), ft_to_pix(size[1]))
        self.loc = (ft_to_pix(loc[0]), ft_to_pix(loc[1]))
        self.door_list = []
        self.color = (0, 0, 0)

    def add_door(self, door):
        self.door_list.append(door)

    def draw(self, screen, offset):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.loc[0] + offset[0], self.loc[1] + offset[1], self.size[0], self.size[1]
        ))

    def is_clicked(self, pos):
        return (self.loc[0] <= pos[0] <= self.loc[0] + self.size[0]) and (self.loc[1] <= pos[1] <= self.loc[1] + self.size[1])

class Door:
    LINE_THICKNESS = 5
    COLOR = (139, 69, 19)

    def __init__(self, loc, size, is_ver, pos_room, neg_room):
        self.size = (ft_to_pix(size[0]), ft_to_pix(size[1]))
        self.loc = (ft_to_pix(loc[0]), ft_to_pix(loc[1]))
        self.is_ver = is_ver
        self.pos_room = pos_room
        self.neg_room = neg_room

    def draw(self, screen, offset):
        if self.is_ver:
            pygame.draw.line(screen, Door.COLOR, 
                             (self.loc[0] + offset[0], self.loc[1] + offset[1]), 
                             (self.loc[0] + offset[0], self.loc[1] + offset[1] + self.size[1]), 
                             Door.LINE_THICKNESS)
        else:
            pygame.draw.line(screen, Door.COLOR, 
                             (self.loc[0] + offset[0], self.loc[1] + offset[1]), 
                             (self.loc[0] + offset[0] + self.size[0], self.loc[1] + offset[1]), 
                             Door.LINE_THICKNESS)
