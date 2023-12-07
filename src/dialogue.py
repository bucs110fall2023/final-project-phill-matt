import pygame

class Dialogue:

    def askQuestion(Questions,num):
        font = pygame.font.Font(None, 48)
        window = pygame.display.set_mode()
        x, y = pygame.display.get_window_size()
        text = font.render(Questions[num], True, "white")
        window.blit(text, (20, y/2))    
        pygame.display.flip()
        Questions[1]
