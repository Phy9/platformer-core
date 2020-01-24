import json, os, sys

import pygame

from game.scene import *
from game.tilescreen import *
from myutils import colors, consts, options

class Level(Scene):
    def __init__(self, levelname):
        with open(os.path.join("resources/levels", f"{levelname}.json"), "r") as f:
            self.level = json.loads(f.read())
        # self.begin = self.level["begin"]
        # self.end = self.level["end"]
        # self.camera = self.level["camera"]
        # self.background = self.level["background"]
        self.tilescreen = TileScreen(self.level)
        super().__init__(self.tilescreen.dimensions)
        self.group.add(self.tilescreen)
    def init_camera(self, camargs):
        if camargs["type"]=="fixed":
            x = camargs["offset"][0] * consts.TILE_W - consts.WN_RES[0] / 2
            y = camargs["offset"][1] * consts.TILE_H - consts.WN_RES[1] / 2
            self.camera_area = lambda: pygame.Rect((x, y), consts.WN_RES)
