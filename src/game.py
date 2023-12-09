import pygame 
import random
import sys
#from src.endgamebutton import GameApp
#import tkinter as tk
#from tkinter import messagebox

class Game:
    def findsize(self):
        self.x, self.y = pygame.display.get_window_size()

    def betting(self):
        pygame.init()
        window = pygame.display.set_mode()
        window.fill("black")
        pygame.display.flip()
        pygame.time.wait(200)
        hit_box_width = self.x / 2
        hit_box_height = self.y

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
                   pygame.quit()
                   sys.exit()
                text = font.render("Which Presidential Candidate do you think will win?", True, "white")
                window.blit(text, (20, self.y/2))    
                pygame.display.flip()
                if flag == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if hitboxes["green"].collidepoint(event.pos):
                            self.betchoice = "Presidential Candidate #2"
                        if hitboxes["blue"].collidepoint(event.pos):
                            self.betchoice = "Presidential Candidate #1"
                        return self.betchoice
    
    def dialogue(Questions, self): 
        Questions = [
            "If you became president, what would you do?",
            "What do we do about climate change?",
            "How do we deal with the cost of living crisis?",
            "How do you feel about taxes?",
            "Should ice cream be banned?",
            "What are your thoughts on cancel culture?",
            "Is war bad?",
            "Is racism bad?",
            "What are your thoughts on religion?",
            "Will you be in my bed tonight?",
            "How do we reform the education system?",
            "Should we have an age cap on politicians?",
            "How should we deal with the mental health crisis?",
            "Should kids really be staring at phones all day?",
            "Am I good Looking?",
            "Do Philip and Matt deserve an A on their final project?",
            "Which one of you is more based?",
        ]

        D = [
            "Tax the rich by 1000%!",
            "We'll just ask the sun to shine less, problem solved. I have the best connections with celestial bodies, believe me. I'm even older than they are! People love experience, right?",
            "What? HUH? What's that?",
            "Oh golly, where’s my script?",
            "Uh um uh uh uh you see uh it has uh shown to uh have good health, uh, benefits.",
            "I am the culture.",
            "No, dying helps build character. Only women should be drafted because we are progressive.",
            "Only if it's towards those I disagree with.",
            "Back in my day we didn't have religion. Instead we drooled over Zeus coming into my bed at night. Good times.",
            "You can guarantee it. I have lots of experience crawling into other people’s beds without permission.",
            "Just throw money at the problem until it fixes itself.",
            "I feel like this is a personal attack.",
            "What do you think of Russia?",
            "I say we take a page out of Canada's playbook and like, just not help them.",
            "Back in my day, we used to stare at rocks while we hunted for animals. I don't see how this is any different.",
            "Why yes, you are VERY good looking. Er, my transcript here says so.",
            "Of course! I am a big fan of Matt, he pushes P all the time!",
            "I am based. Ronny here is a soy. The biggest of them. He drinks so much soy that he is more of a wife than mine. He has bad opinions. Mine are good.",
        ]

        R = [
            "Lock Joux up! He stinky!",
            "It's a hoax, a total hoax. I mean, who even believes in science these days? I've got a revolutionary plan: we're going to build a giant fan, the biggest fan you've ever seen, and we'll just blow all the pollution away. ",
            "Oh what? I can't hear you over the sound of SLEEPY JOUX!",
            "Taxation is theft.",
            "You only support them because you are one, sleepy Joux! I call racism!",
            "I am the cancel.",
            "War is amazing, as long as it's in the middle east! I could really use that oil, it tastes great!",
            "Only if it's towards those I disagree with.",
            "Deuz Vult! Let's show those heathens that their religion is wrong! Only MINE is right!",
            "I am in your walls.",
            "Who needs education when everything's online?",
            "That would be awful, we’re clearly more qualified than anyone! Actually, I'M more qualified than anyone.",
            "It's like, bad. I'm gonna go to Mr Putin and tell him to stop. It’ll work.",
            "Just nuke them! They’re only good for beer and abs anyway!",
            "Let natural selection take its course and sell their bodies for their organs! No human is worth nothing!",
            "We don't even have kids to be staring at phones to begin with! Come on people! Can you like, get busy or something?",
            "Why yes, I AM very good looking. How could you tell?",
            "Gotta give Phil that 100, he sponsored me back when I needed a Million Dollars!",
            "No, I am based. I am the chad. The nordic chad. With the big chin and Muscles. That’s how you know my opinion is right. His is bad. I have the good opinions.",
        ]
        window = pygame.display.set_mode()
        font = pygame.font.Font(None, 48)
        TempQ = Questions
        TempD = D
        TempR = R
       # GameApp()
        #The base score for the democrat and rebublican is 0
        TotalScoreD=0
        TotalScoreR=0
        #Audience Text for rating the criminals, I mean politicians
        for _ in range(18):
            i = random.randint(0,TempQ.len)
            text = font.render("Question " + _ + " : " + TempQ[i], True, "white")
            window.blit(text, (20, self.y/2))    
            pygame.display.flip()
            pygame.time.wait(1000)
            TempQ.remove(i)
            
            text = font.render("D replies: " + TempD[i], True, "white")
            window.blit(text, (20, self.y/2))
            ScoreD = random.randint(1, 10)
            TotalScoreD += ScoreD   #After they respond, the audience will rate them, and random score will be provided. 
            window.blit("The audience gave 'D' a rating of " + ScoreD, (20, self.y/3))
            pygame.display.flip()
            pygame.time.wait(1000)
            TempD.remove(i)
            
            text = font.render("Alright, now it's your turn, R", True, "white")
            window.blit(text, (20, self.y/2))    
            pygame.display.flip()
            pygame.time.wait(1000)

            text = font.render("R replies: " + TempR[i], True, "white")
            window.blit(text, (20, self.y/2)) 
            ScoreR = random.randint(1, 10)
            TotalScoreR += ScoreR
            ScoreR += random.randint(1, 10)
            window.blit("The audience gave 'R' a rating of " + ScoreR, (20, self.y/3))
            pygame.display.flip()
            pygame.time.wait(1000)
            TempR.remove(i)

