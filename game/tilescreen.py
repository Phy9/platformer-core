import pathlib, os, sys

import pygame

from game.scene import *
# from game.tile import *
from myutils import colors, consts, options

'''
NAME ID
rock RR
empty ,.
16 9
ID,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.
RR,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.
RR,.,.RR,.,.,.,.,.,.,.,.,.,.,.,.
RR,.,.,.,.,.,.,.,.,.RRRR,.,.,.RR
RR,.,.,.,.,.,.,.,.RR,.,.,.,.,.RR
,.,.,.,.,.,.,.RRRR,.,.,.,.,.,.RR
,.,.,.,.RRRR,.RR,.RR,.,.,.,.,.RR
,.,.,.,.RRRR,.,.,.,.RR,.,.,.,.RR
RRRRRRRRRRRR,.,.,.,.RRRRRRRRRRRR

'''

image_table = {}

def init_image():
    path_to_image_dir = pathlib.Path("resources", "images", "tiles")
    # print([p.is_file() for p in path_to_image_dir.iterdir()])
    # print([p.suffix.lower() == ".png" for p in path_to_image_dir.iterdir()])
    path_to_images = [p for p in path_to_image_dir.iterdir() if p.is_file() and p.suffix.lower() == ".png"]
    if not path_to_images:
        print("No tile images found!", file=sys.stderr)
    for p in path_to_images:
        image_table[p.name] = pygame.transform.scale(pygame.image.load(str(p)), (consts.TILE_W, consts.TILE_H))

init_image()

class TileMap:
    def __init__(self, fp):
        self.tile = {}
        mode = 0
        with open(fp, 'r') as fin:
            for lines in fin:
                if mode == 0:
                    l = lines.strip().split(' ')
                    self.tile[l[1]] = l[0]
                    if l[0] == "empty":
                        mode = 1
                elif mode == 1:
                    self.width, self.height = tuple(map(int, lines.split(' ')))
                    self.map = []
                    mode = 2
                elif mode == 2:
                    rear = len(self.map)
                    self.map.append([])
                    for i in range(len(lines) // 2):
                        self.map[rear].append(lines[i * 2: i * 2 + 2])
    def substitute(self, src, dest):
        for i in self.tile:
            if self.tile[i] == src:
                self.tile[i] = dest


class TileScreen(pygame.sprite.Sprite):
    def __init__(self, level):
        self.level = level
        self.tilemapname = level["tilemap"]["name"]
        self.tilemap = TileMap("resources/tilemaps/" + self.tilemapname)
        self.sub = level["tilemap"]["substitute"]
        self.dimensions = (self.tilemap.width * consts.TILE_W, self.tilemap.height * consts.TILE_H)
        for i, v in self.sub.items():
            self.tilemap.substitute(i, v)
        super().__init__()
        self.image = pygame.Surface(self.dimensions, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        # TODO: process self.rect
        self.need_redraw = True
    def draw(self):
        if not self.need_redraw:
            return
        print("Called and run!")
        for x in range(self.tilemap.width):
            for y in range(self.tilemap.height):
                tilename = self.tilemap.tile[self.tilemap.map[y][x]]
                if tilename == "empty":
                    continue
                tileimage = image_table[tilename+'.png']
                self.image.blit(tileimage, (x*consts.TILE_W, y*consts.TILE_H))
        self.need_redraw = False
