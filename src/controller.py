import pygame
import sys
from game import Game
from dialogue import Dialogue

class Controller:
  
  def mainloop(self):
       pass

    #select state loop

  ### below are some sample loop states ###
  
  def __init__(self):
    pygame.init()
    window = pygame.display.set_mode()
    window.fill("black")
    pygame.display.flip()
    pygame.time.wait(200)
    global x, y
    x, y = pygame.display.get_window_size()
                

  def gameloop(self):
    #event loop
    while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for a mouse button press
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
               Dialogue()
                
              
      #update data

      #redraw
    

