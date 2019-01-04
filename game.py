import pygame as pg
import util


class Game:
    running = None
    max_fps = None

    screen = None
    screen_width = None
    screen_height = None
    logo = None

    font_cs = None
    debug = None

    bkg = None
    objs = [[], [], [], [], []]

    def __init__(self, w=1280, h=720, cap="HM", logo_path="src/ico/tsujita.jpg",
                 deb_font="Comic Sans MS", deb_font_size=30,
                 max_fps=60, run=True):
        pg.init()

        pg.font.init()
        self.font_cs = pg.font.SysFont(deb_font, deb_font_size)
        self.debug = self.font_cs.render('Some Text', False, (255, 255, 255))

        self.logo = util.load_img(logo_path)
        pg.display.set_icon(self.logo)
        pg.display.set_caption(cap)

        self.screen_width = w
        self.screen_height = h
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))

        self.max_fps = max_fps
        self.running = run

    def set_debug(self, text=""):
        self.debug = self.font_cs.render(text, False, pg.Color('white'))

    def load_bkg(self, path):
        self.bkg = util.load_img(path)
        self.bkg = pg.transform.scale(self.bkg, (self.screen_width, self.screen_height))

    def draw(self):
        self.screen.blit(self.bkg, (0, 0))
        for layer in reversed(self.objs):
            for sprite in layer:
                self.screen.blit(sprite.spr, sprite.pos)
        self.screen.blit(self.debug, (10, 5))

    def new_obj(self, obj, layer):
        self.objs[layer].append(obj)

    def chk_colision(self, obj):
        rec1 = obj.get_col_rec()

        if rec1:  # if object has colision
            rec1.topleft = obj.pos  # offset object to real world location
            for layer in reversed(self.objs):
                for sprite in layer:
                    # for each object placed in the world
                    if sprite != obj:  # guarantee it is not itself
                        rec2 = sprite.get_col_rec()
                        if rec2:  # if object has colision
                            rec2.topleft = sprite.pos  # offset object to real world location
                            if rec1.colliderect(rec2):  # test
                                return True

        return False

