import pygame as pg
from obj import Obj, Bee
from menu import Menu
from game import Game


class Main:
    
    def __init__(self, sizex, sizey, title):

        self.window = pg.display.set_mode([sizex, sizey])
        self.title = pg.display.set_caption(title)

        self.start_screen = Menu()
        self.game = Game()

        self.loop = True
        self.fps = pg.time.Clock()

    def draw(self):
        self.window.fill([0, 0, 0])
        if not self.start_screen.change_scene:
            self.start_screen.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()

    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                self.loop = False
            
            self.start_screen.events(events)
            self.game.bee.move_bee(events)

    
    def update(self):
        while self.loop:
            self.fps.tick(10)
            self.draw()
            self.events()
            pg.display.update()

game = Main(360, 640, "BeeHoney")
game.update()
