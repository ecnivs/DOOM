# DOOM Scout
# by Vince Swu

from wad_data import WADData
from settings import *
import pygame as pg
import sys
from map_renderer import MapRenderer
from player import Player
from bsp import BSP
from seg_handler import SegHandler
from view_renderer import ViewRenderer

class DoomEngine:
    def __init__(self, wad_path='wad/DOOM1.WAD'):
        self.wad_path = wad_path
        self.screen = pg.display.set_mode(WIN_RES, pg.SCALED)
        self.framebuffer = pg.surfarray.array3d(self.screen)
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 1 / 60
        self.level = LEVEL
        self.on_init()

    def on_init(self):
        self.wad_data = WADData(self, map_name='E1M'+str(self.level))
        self.map_renderer = MapRenderer(self)
        self.player = Player(self)
        self.bsp = BSP(self)
        self.seg_handler = SegHandler(self)
        self.view_renderer = ViewRenderer(self)

    def update(self):
        self.player.update()
        self.seg_handler.update()
        self.bsp.update()
        self.dt = self.clock.tick()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        pg.surfarray.blit_array(self.screen, self.framebuffer)
        self.view_renderer.draw_sprite()
        pg.display.flip()

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()
            if e.type == pg.KEYDOWN:
                if pg.K_1 <= e.key <= pg.K_9:
                    if self.level != e.key - pg.K_0:
                        self.level = e.key - pg.K_0
                        self.on_init()

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    doom = DoomEngine()
    doom.run()
