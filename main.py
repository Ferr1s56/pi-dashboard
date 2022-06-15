from turtle import width
import pygame
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import os

bgcolor = (56, 167, 226)
black = (0, 0, 0)
white = (255, 255, 255)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
res = requests.get(f'https://www.google.com/search?q=Lansdale+weather&oq=Lansdale+weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')   
info = soup.select('#wob_dc')[0].getText().strip() 
degrees = str(soup.select('#wob_tm')[0].getText().strip())

weather = {
    "cloudy" : "cloud.png",
    "sunny" : "sun.png",
    "clear" : "sun.png",
    "mostly sunny" : "mostlysunny.png",
    "partly cloudy" : "mostlysunny.png",
    "scattered showers" : "showers.png"

}

pygame.init()

def timegetter():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    return current_time

def renderText(text, font, x, y, color):
        renderedText = font.render(text, True, color)
        renderedTextRect = renderedText.get_rect()
        renderedTextRect.center = (x, y)

        win.blit(renderedText, renderedTextRect)

def renderImage(image, x, y):
    renderedImg = pygame.image.load(image)
    renderedImgRect = renderedImg.get_rect()
    renderedImgRect.center = (x, y)
    win.blit(renderedImg, renderedImgRect)


clockFont = pygame.font.Font(os.path.join("fonts", "ShareTechMono.ttf"), 150)
weatherFont = pygame.font.Font(os.path.join("fonts", "ShareTechMono.ttf"), 180)
width = 1280
height = 720
win = pygame.display.set_mode((width, height))

screen1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

pygame.display.set_caption("Dashboard")

run = True
while run:
    now = datetime.now()
    current_seconds = int(now.strftime("%S"))

#    if current_seconds in screen1:
    if True:
#    if False:
        win.fill(bgcolor)
        renderText(degrees + "°F", weatherFont, width/2, height/12*10, black)
        weatherImg = os.path.join("images", weather[info.lower()])
        renderImage(weatherImg, width/2, height/3)

#    if True:
    if False:
        win.fill(bgcolor)
        renderText(timegetter(), clockFont, width/2, height/2, black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()