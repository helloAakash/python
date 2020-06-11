import pygame
from pygame import mixer

pygame.init() 

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('music player')

mixer.music.load('C:/Users/aakas/Music/Music/Mayer/john mayer - Paradise Valley/11 On the Way Home.mp3')
mixer.music.play()

print("Press 'p' to pause and 'r' to resume")
print("'q' to quit")
 
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
            elif event.key == pygame.K_r:
                mixer.music.unpause()
            elif event.key == pygame.K_q:
                run = False

pygame.QUIT
quit()
