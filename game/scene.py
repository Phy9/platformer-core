import pygame

def __some_random_bullshit():
    pass  # does nothing

function_class = __some_random_bullshit.__class__

class SceneGroup(pygame.sprite.Group):
    def __init__(self, *sprites, **kwargs):
        self.drawable_sprites = {}
        super().__init__(*sprites, **kwargs)
        self.add_d_sprites(*sprites)
    def add_d_sprites(self, *sprites):
        for s in sprites:
            if "draw" in dir(s) and "__call__" in dir(s.draw):
                print(f"Add drawable sprite {s}")
                self.drawable_sprites[s] = 0
    def add(self, *sprites):
        super().add(*sprites)
        self.add_d_sprites(*sprites)
    def remove(self, *sprites):
        for s in sprites:
            if isinstance(s, Scene) and s in self.drawable_sprites:
                del self.drawable_sprites[s]
    def draw(self, surface):
        for s in self.drawable_sprites:
            s.draw()
        super().draw(surface)

class Scene(pygame.sprite.Sprite):
    def __init__(self, dimensions, subsprites=None):
        super().__init__()
        self.dimensions = dimensions
        self.image = pygame.Surface(dimensions)
        self.rect = self.image.get_rect()
        self.group = SceneGroup()
        if subsprites:
            self.group.add(*subsprites)
    def move(self, pos):
        self.rect.x, self.rect.y = pos
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.group.update(*args, **kwargs)
    def draw(self):
        self.group.draw(self.image)
