import object
import pygame as pg
import util


class Player(object.Object):
    game = None
    dt = None
    spd = 16*4 * 2
    key_binds = None

    def __init__(self, spr_path, game, pos=(0, 0)):
        super().__init__(spr_path, pos, True, "Player")
        self.game = game
        self.key_binds = [
            [pg.K_w, self.try_move, (util.Y, -self.spd)],
            [pg.K_UP, self.try_move, (util.Y, -self.spd)],

            [pg.K_a, self.try_move, (util.X, -self.spd)],
            [pg.K_LEFT, self.try_move, (util.X, -self.spd)],

            [pg.K_s, self.try_move, (util.Y,  self.spd)],
            [pg.K_DOWN, self.try_move, (util.Y,  self.spd)],

            [pg.K_d, self.try_move, (util.X,  self.spd)],
            [pg.K_RIGHT, self.try_move, (util.X,  self.spd)]
        ]

    def chk_imp(self, dt):
        self.dt = dt
        pressed = pg.key.get_pressed()
        for key in self.key_binds:
            if pressed[key[0]]:
                key[1](key[2])

    # parameters: direction, speed
    def try_move(self, p=(0, 0)):
        _dir = p[0]
        spd = p[1]

        prev_pos = self.pos
        if _dir == util.Y:
            self.offset_y(spd * self.dt)
        elif _dir == util.X:
            self.offset_x(spd * self.dt)
        else:
            return

        if self.game.chk_colision(self):
            self.set_posxy(prev_pos)
