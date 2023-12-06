import pygame
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
    
  def betting(self):
    pygame.init()
    window = pygame.display.set_mode()
    window.fill("black")
    pygame.display.flip()
    pygame.time.wait(200)
    x, y = pygame.display.get_window_size()
    hit_box_width = x / 2
    hit_box_height = y

    hitboxes = {
        "green": pygame.Rect(0, 0, hit_box_width, hit_box_height),
        "blue": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    }

    hitboxes["green"].left = hitboxes["blue"].right
    # Define main colors
    main_colors = {
    "green": (0, 200, 0),
    "blue": (0, 0, 200),
    }
    # Define highlight colors
    highlight_colors = {
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    }
    font = pygame.font.Font(None, 48)

    done = False # a flag variable to determine when the program is done

    for c, hb in hitboxes.items(): #reset boxes to main color
                pygame.draw.rect(window, main_colors[c], hb)
                pygame.draw.rect(window, highlight_colors[c], hitboxes[c])
                pygame.display.flip()
    for color, hitbox in hitboxes.items():
                pygame.draw.rect(window, highlight_colors[color], hitboxes[color])
                pygame.display.flip()
    running = True
    flag = 0
    while running: #mainloop -1 frame
    #1. event loop
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                running = False
            text = font.render("Which Presidential Candidate do you think will win?", True, "white")
            window.blit(text, (20, y/2))    
            pygame.display.flip()
            if flag == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hitboxes["green"].collidepoint(event.pos):
                        self.betchoice = "Presidential Candidate #2"
                    if hitboxes["blue"].collidepoint(event.pos):
                        self.betchoice = "Presidential Candidate #1"
                    return self.betchoice
                
  def dialogue(self):
       ok    
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
