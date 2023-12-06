import pygame 
import random
import math
pygame.init() 

class UI:
    def __init__():
         

# Part B
#Screen choosing
screen= pygame.display.set_mode()
width,height = pygame.display.get_window_size()

hit_box_width = width / 2
hit_box_height = height 

hitboxes = {
    "green": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "yellow": pygame.Rect(0, 0, hit_box_width, hit_box_height),
}

hitboxes["green"].left = hitboxes["yellow"].right

for box_color in hitboxes:
    pygame.draw.rect(screen,box_color,hitboxes[box_color])

pygame.display.flip()
pygame.time.wait(2000)


class Rectangle:
#Method
    def __init__(self, x, y, h, w):