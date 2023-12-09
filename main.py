import pygame
from src.controller import Controller
#from src.endgamebutton import GameApp
from src.game import Game


def main():
    pygame.init()
    Game()
    Controller()
    
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
