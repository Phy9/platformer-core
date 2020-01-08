import pygame

class SceneGroup(pygame.sprite.Group):
    def __init__(self, *sprites, **kwargs):
        self.scene_sprites = {}
        super().__init__()
    def add(self, *sprites):
        super().add(*sprites)
        for s in sprites:
            if isinstance(s, Scene):
                self.scene_sprites[s] = 0
    def remove(self, *sprites):
        for s in sprites:
            if isinstance(s, Scene) and s in self.scene_sprites:
                del self.scene_sprites[s]
    def draw(self, surface):
        for s in self.scene_sprites:
            s.draw(surface)
        super().draw(surface)

class Scene(pygame.sprite.Sprite):
    def __init__(self, dimensions, subsprites=None):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.rect = self.image.get_rect()
        self.group = pygame.sprite.Group()
        if subsprites:
            self.group.add(*subsprites)
    def move(self, pos):
        self.rect.x, self.rect.y = pos
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.group.update(*args, **kwargs)
    def draw(self, surface):
        self.group.draw(self.image)

__all__ = [SceneGroup, Scene]
