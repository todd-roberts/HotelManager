import pygame
from utils import ft_to_pix

class Guest:
    def __init__(self, loc_pix, rad_ft, speed_ft_s, color):
        self.loc = [loc_pix[0], loc_pix[1]]
        self.rad = ft_to_pix(rad_ft)
        self.speed = ft_to_pix(speed_ft_s) / 60
        self.color = color

    def update(self):
        pass

    def draw(self, screen, offset):
        pygame.draw.circle(screen, self.color, 
                           (int(self.loc[0] + offset[0]), int(self.loc[1] + offset[1])), 
                           int(self.rad))

    def is_clicked(self, pos):
        dist = ((self.loc[0] - pos[0]) ** 2 + (self.loc[1] - pos[1]) ** 2) ** 0.5
        return dist <= self.rad
