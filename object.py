import util
import pygame as pg


class Object:
    name = None
    spr = None
    pos = None
    rect = None
    ovrrect = None
    colis = None

    def __init__(self, spr_path, pos=(0, 0), can_colide=False, name="unnamed"):
        self.spr = util.load_img(spr_path)
        self.rect = self.spr.get_rect()
        self.pos = pos
        self.colis = can_colide
        self.name = name

    def set_posxy(self, pos):
        self.pos = pos

    def set_pos(self, x, y):
        self.pos = (x, y)

    def set_x(self, x):
        self.pos = (x, self.pos[1])

    def set_y(self, y):
        self.pos = (self.pos[0], y)

    def offset_x(self, x):
        self.pos = (self.pos[0] + x, self.pos[1])

    def offset_y(self, y):
        self.pos = (self.pos[0], self.pos[1] + y)

    def set_spr(self, spr):
        self.spr = spr
        self.rect = self.spr.get_rect()

    def scale(self, x=1, y=1):
        scl = self.spr.get_rect()
        newx = int(scl[2] * x)
        newy = int(scl[3] * y)
        self.spr = pg.transform.scale(self.spr, (newx, newy))
        self.rect = self.spr.get_rect()

    def get_col_rec(self):
        if not self.colis:
            return False

        if self.ovrrect:
            return self.ovrrect
        else:
            return self.rect
