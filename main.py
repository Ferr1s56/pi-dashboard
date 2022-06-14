import pygame
from datetime import datetime

def timegetter():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    return current_time

print(timegetter())

bgcolor = (14, 12, 81)

pygame.init()

font = pygame.font.Font("fonts\ShareTechMono.ttf", 150)
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Dashboard")

run = True
while run:
    win.fill(bgcolor)

    testText = font.render(timegetter(), True, (255, 255, 255))
    testTextRect = testText.get_rect()
    testTextRect.center = (640.5, 360.5)

    win.blit(testText, testTextRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()