# Import modules
import pygame
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import os
import time

#COLORS!
bgcolor = (56, 167, 226)
black = (0, 0, 0)
grey = (105,105,105)
white = (255, 255, 255)
cyan = (79, 234, 226)
indigo = (81, 116, 205)

# Get weather stuff
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
res = requests.get(f'https://www.google.com/search?q=Lansdale+weather&oq=Lansdale+weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')   
info = soup.select('#wob_dc')[0].getText().strip() 
degrees = str(soup.select('#wob_tm')[0].getText().strip())

# Keyword to image list
weather = {
    "cloudy" : "cloud.png",
    "sunny" : "sun.png",
    "clear" : "sun.png",
    "mostly sunny" : "mostlysunny.png",
    "partly cloudy" : "mostlysunny.png",
    "scattered showers" : "showers.png",
    "rain" : "showers.png"

}

pygame.init()

def getTime():
    # Gets current time
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    return current_time

def fillSurface(surface, color):
    # Fill all pixels of a surface with specified color
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def renderText(text, font, x, y, color):
    # Renders text
    renderedText = font.render(text, True, color)
    renderedTextRect = renderedText.get_rect()
    renderedTextRect.center = (x, y)
    win.blit(renderedText, renderedTextRect)

def renderShadowText(text, font, x, y, offset, color, dropColor):
    # Renders dropshadow text
    renderText(text, font, x+offset, y+offset, dropColor)
    renderText(text, font, x, y, color)
 

def renderImage(image, x, y, color=""):
    # Renders images
    renderedImg = pygame.image.load(image)
    renderedImgRect = renderedImg.get_rect()
    renderedImgRect.center = (x, y)
    win.blit(renderedImg, renderedImgRect)

def renderShadowImage(image, x, y, offset,  dropcolor, color=""):
    renderedShadowImg = pygame.image.load(image)
    renderedShadowImgRect = renderedShadowImg.get_rect()
    renderedShadowImgRect.center = (x + offset, y + offset)
    fillSurface(renderedShadowImg, dropcolor)
    win.blit(renderedShadowImg, renderedShadowImgRect)
    renderImage(image, x, y)



# Fonts and pygame display variables
clockFont = pygame.font.Font(os.path.join("fonts", "ShareTechMono.ttf"), 150)
weatherFont = pygame.font.Font(os.path.join("fonts", "ShareTechMono.ttf"), 180)
bgImage = pygame.image.load(os.path.join("images", "bg.png"))
width = 1280
height = 720
fps = 60
win = pygame.display.set_mode((width, height))

# On what seconds to display certain screens
screen1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

pygame.display.set_caption("Dashboard")

run = True
while run:
    time.sleep(1/fps)
    now = datetime.now()
    current_seconds = int(now.strftime("%S"))

    if current_seconds in screen1:
        # Weather Screen
        weatherImg = os.path.join("images", weather[info.lower()])
        #win.fill(bgcolor)
        win.blit(bgImage, (0, 0))
        renderShadowText(degrees + "°F", weatherFont, width/2, height/6*5, 7, cyan, indigo)
        renderShadowImage(weatherImg, width/2, height/3, 7, grey)

    else:
        # Time Screen
        #win.fill(bgcolor)
        win.blit(bgImage, (0, 0))
        renderShadowText(getTime(), clockFont, width/2, height/2, 7, cyan, indigo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                run = False


    pygame.display.update()