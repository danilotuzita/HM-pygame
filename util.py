import pygame as pg
import os


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
X = 0
Y = 1


def load_img(path):
    return pg.image.load(os.path.join(path))
