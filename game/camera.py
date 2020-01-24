"""

 ###
 #  #                             #          #
 #  # #### #### ### #### ###  ### ## #### ####
 #  # # #  #  # #   # #  #   #  # #  # #  #  #
 ###   ### #### #    ### ### #### ##  ### ####
           #

"""

import pygame

from game.scene import *
from game.level import *
from myutils import colors, consts, options

class Camera(Scene):
    def __init__(self, Lvl):


        super().__init__(consts.WN_RES)
        self.group.add(Lvl)

    def draw(self, )
