import pygame as pg
from obj import Obj
import random

class Game:
    def __init__(self):
        self.bg = Obj("BeeHoney/assets/bg.png", 0, 0)
        self.bg2 = Obj("BeeHoney/assets/bg.png", 0, -640)

        self.spider = Obj("BeeHoney/assets/spider1.png", random.randint(0, 281), -200)
        self.spider2 = Obj("BeeHoney/assets/spider1.png", random.randint(0, 281), -200)
        self.flower = Obj("BeeHoney/assets/flower1.png", random.randint(0, 332), -28)
        self.flower2 = Obj("BeeHoney/assets/flower1.png", random.randint(0, 332), -28)
        self.change_scene = False

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.flower.drawing(window)
        self.spider.drawing(window)
        self.spider2.drawing(window)

    def update(self):
        self.move_bg()
        self.move_flor()
        self.move_spider()
        self.spider.anim()
        self.spider2.anim()
        self.flower.flor()

    def move_spider(self):
        self.spider.sprite.rect[1] += random.randint(5, 10)
        self.spider2.sprite.rect[1] += random.randint(5, 10)
        if self.spider.sprite.rect[1] >= 640:
            self.spider.sprite.rect[1] = 0
            self.spider.sprite.rect[0] = random.randint(0, 281)
            self.spider.sprite.rect[1] += random.randint(5, 10)
        if self.spider2.sprite.rect[1] >= 640:
            self.spider2.sprite.rect[1] = 0
            self.spider2.sprite.rect[0] = random.randint(0, 281)
            self.spider2.sprite.rect[1] += random.randint(5, 10)


    def move_flor(self):
        self.flower.sprite.rect[1] += 1
        self.flower2.sprite.rect[1] += 1
        if self.flower.sprite.rect[1] >= 640:
            self.flower.sprite.rect[1] = 0
            self.flower.sprite.rect[0] = random.randint(0, 332)
        if self.flower2.sprite.rect[1] >= 0:
            self.flower2.sprite.rect[1] = -28
            self.flower2.sprite.rect[0] = random.randint(0, 332)
    
    def move_bg(self):
        self.bg.sprite.rect[1] += 1
        self.bg2.sprite.rect[1] += 1

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640


