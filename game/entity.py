import json, os, sys, pathlib

import pygame

from game.scene import *
from game.tilescreen import *
from myutils import colors, consts, options

class entity(scene):
    def load_image(self,fp):
        ret={}
        for p in fp.iterdir():
            if p.is_file():
                try:
                    ret[os.path.basename(p)]=pygame.image.load(p)
                except Exception as err:
                    print(err)
            else:
                ret[]


    def init_image(self,fp):

        path_to_images = [p for p in fp.iterdir() if p.is_file() and p.suffix.lower() == ".png"]
        if not path_to_images:
            print("No tile images found!", file=sys.stderr)
        for p in path_to_images:
            image_table[p.name] = pygame.transform.scale(pygame.image.load(str(p)), (consts.TILE_W, consts.TILE_H))
    def __init__(self,dim):
        super().__init__(dim)

class static_entity(entity):

    def __init__(self,name):


        