import pygame as pg
import game
import object
import player
import spritesheet

g = None


def spritesheettest():
    ss = spritesheet.Spritesheet("src/sht/sprites.gif")
    image = ss.image_at((0, 128, 16, 16), colorkey=(20, 20, 20))
    image = pg.transform.scale(image, (64, 64))
    return image


def main():
    global g
    g = game.Game()
    g.load_bkg("src/env/background1_2x.png")

    o = object.Object("src/env/bag.png", (50, 50), can_colide=True, name="the only fucking thing")
    g.new_obj(o, 1)
    # o.set_spr(spritesheettest())
    p = player.Player("src/chr/knight/knight_0.png", g, (150, 50))
    # p.scale(0.25, 0.25)
    g.new_obj(p, 0)

    c = pg.time.Clock()
    while g.running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                g.running = False

        dt = c.tick(g.max_fps) / 1000
        fps = int(c.get_fps())

        g.set_debug(str(fps) + " / " + str(dt))
        p.chk_imp(dt)
        g.draw()
        pg.display.flip()


if __name__ == "__main__":
    main()

