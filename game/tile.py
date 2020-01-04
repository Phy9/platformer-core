import pathlib

import pygame

from myutils import colors, consts, options

'''
 * The most general class to represent a terrain tile
 * @extends pygame.sprite.Sprite
 * @field image [inherited] the image used on the tile
 * @field mask [inherited] the mask of the sprite, typically generated from the image
 * @field rect [inherited] the rectangle describing the position and size of the tile, used in collision calculations and renderng
 * @field pos list of x (pos[0]) and y (pos[1]) coordinates, in tile units (NOT pixels)
'''
class Tile(pygame.sprite.Sprite):
    class TileException(Exception):
        'Handle unwanted situations, such as image table not initialized, with TileException.'
    _image_table = {}
    _rect_table = {}
    '''
     * A self-called static method in attempt to initialize all tile images in order to save resource and improve game fluency
     * @throws TileException when there are no files qualifying for tile images in the designated directory (./resources/images/tiles/)
     * @returns None
     * @related pathlib, pygame.image, Tile.TileException
    '''
    @staticmethod
    def init_image():
        # Reads images from the resources/images/tiles folder
        path_to_image_dir = pathlib.Path('resources', 'images', 'tiles')
        # The paths to the images to be loaded are those in the designated directory which are files and end with a PNG extension.
        path_to_images = [p for p in path_to_image_dir.iterdir() if p.is_file() and p.suffix.lower() is 'png']
        if not path_to_images:
            raise TileException('Tile images not found.')
        for p in path_to_images:
            # For every image
            _image_table[p.name] = pygame.image.load(str(p))
            _rect_table[p.name] = _image_table[p.name].get_rect()
    init_image()  # Self-call in class definition; auto-initialize
    '''
     * Initialize a Tile object. This tile object does not interact with the player.
     * @param self [ignored] a reference to the object self
     * @param pos list/tuple of xy-coordinates in tile units (Not pixels)
     * @param imageid an available key (image ID) in the class attribute `_image_table`
     * @throws TileException when at least one actual parameter is invalid
     * @return None
     * @related pygame.sprite Tile
    '''
    def __init__(self, pos, imageid):
        if not isinstance(pos, (list, tuple)) or pos.length != 2:
            raise TileException(f'Invalid initial tile position {pos}.')
        if imageid not in self.__class__._image_table:
            raise TileException(f'Tile image ID {imageid} not found. Check your Tile class initialization status.')
        pygame.sprite.Sprite.__init__(self)
        self.pos = list(pos)
        self.imageid = imageid
        self.image = self.__class__._image_table[self.imageid]
        self.rect = self.__class__._image_table[self.imageid].copy()  # Make sure it is a new rect object, so that I can do whatever I want to the coordinates
        # TODO: Mask
    # TODO: update_rect_xy
    # TODO: Masking
