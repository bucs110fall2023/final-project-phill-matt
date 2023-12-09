import pygame 
import random
import math
pygame.init()
import tkinter as tk
from tkinter import messagebox

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

done = False # a flag variable to determine when the program is done

guess = None
while not guess:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["green"].collidepoint(event.pos):
                guess="green"
                
            elif hitboxes["yellow"].collidepoint(event.pos):
                guess="yellow"
