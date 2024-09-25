from hotel import Hotel
import pygame

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hotel = Hotel()
        self.hotel.create_hotel()

    def update(self):
        self.hotel.update()

    def draw(self, screen):
        self.hotel.draw(screen)

    def handle_key_down(self, key):
        if key == pygame.K_UP:
            self.hotel.manager.set_movement("up", True)
        elif key == pygame.K_DOWN:
            self.hotel.manager.set_movement("down", True)
        elif key == pygame.K_LEFT:
            self.hotel.manager.set_movement("left", True)
        elif key == pygame.K_RIGHT:
            self.hotel.manager.set_movement("right", True)

    def handle_key_up(self, key):
        if key == pygame.K_UP:
            self.hotel.manager.set_movement("up", False)
        elif key == pygame.K_DOWN:
            self.hotel.manager.set_movement("down", False)
        elif key == pygame.K_LEFT:
            self.hotel.manager.set_movement("left", False)
        elif key == pygame.K_RIGHT:
            self.hotel.manager.set_movement("right", False)

    def handle_mouse_click(self, pos):
        self.hotel.handle_mouse_click(pos)
