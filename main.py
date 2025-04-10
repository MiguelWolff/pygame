import pygame as pg
from obj import Obj
from menu import Menu
from game import Game


class Main:
    
    def __init__(self, sizex, sizey, title):

        self.window = pg.display.set_mode([sizex, sizey])
        self.title = pg.display.set_caption(title)

        self.menu = Menu()
        self.game = Game()

        self.loop = True

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)

    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                self.loop = False
    
    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pg.display.update()

game = Main(360, 640, "BeeHoney")
game.update()
