import pygame as pg
from obj import Obj

class Game:
    def __init__(self):
        self.bg = Obj("BeeHoney/assets/bg.png", 0, 0)
        self.bg2 = Obj("BeeHoney/assets/bg.png", 0, -640)

        self.spider = Obj("BeeHoney/assets/spider1.png", 200, 200)
        #self.spider = Obj("BeeHoney/assets/spider1.png", 200, 200)
        self.flower = Obj("BeeHoney/assets/flower1.png", 50, 50)
        self.change_scene = False

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)

    def update(self):
        self.move_bg()
        self.spider.anim()
        #self.flower.anim()
    
    def move_bg(self):
        self.bg.sprite.rect[1] += 1
        self.bg2.sprite.rect[1] += 1

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640


