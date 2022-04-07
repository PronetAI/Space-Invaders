import pygame
from pygame.locals import *
import random
import time
import Mod_Colors
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Space Invaders")
a = 100
b = 100
change = 5
left = 0
right = 0
Spacer = 0
Score = 0
class Alien:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 100
        self.image = pygame.image.load("Alien 2.jpg")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.hit = 0
    def Display(self):
        screen.blit(self.image,(self.x,self.y))
class Space_Ship:
    def __init__(self,x):
        self.x = x
        self.y = 550
    def Display(self):
        pygame.draw.rect(screen,(255,0,0),(self.x,self.y,100,50))
    def Movment(self,change):
        self.x = self.x + change
class Bullet():
    def __init__(self):
        self.x = space.x + 50
        self.y = 550
    def Display(self):
        pygame.draw.rect(screen,(255,255,0),(self.x,self.y,10,10))
    def Movment(self):
        self.y = self.y - 10
space = Space_Ship(200)
A1 = []
bullet = Bullet()
for i in range(1,6,1):
    A2 = Alien(a,b)
    A1.append(A2)
    a = a + 100
a = 100
while True:
    pygame.display.update()
    screen.fill((0,0,0))
    if bullet.y <= 0 :
        Spacer = 0
        bullet.y = space.y - 10
        bullet.x = space.x + 50
    for i in A1:
        i.Display()
        # a.y = a.y + 1
    space.Display()
    if left == 1:
        space.Movment(-10)
        left = 0
    if right == 1:
        space.Movment(10)
        right = 0
    if Spacer == 1:
        bullet.Movment()
        bullet.Display()
        #pygame.display.update()
        #Spacer = 0
    for a in A1:
        if bullet.y in range(a.y, a.y + 50) and bullet.x in range(a.x, a.x + 50):
            A1.remove(a)
            Score = Score + 1
            print("Your Score is",Score)
    if A1 == []:
        print("Game Over!")
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                left = 1
            if event.key == K_d:
                right = 1
            if event.key == K_SPACE:
                Spacer = 1
