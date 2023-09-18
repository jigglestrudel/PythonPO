import pygame
from pygame.font import Font


class TextField:
    font: Font

    def __init__(self, x, y, w, h, font, text, pink=False):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.font = font
        self.pink = pink
        self._text = text
        self._updated = True
        self.field_surface = pygame.Surface((self.width, self.height))
        self.field_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, t):
        self._text = t
        self._updated = True

    def update(self):
        if self._updated:
            self.field_surface.fill("pink" if self.pink else "white")
            for index, line in enumerate(self._text):
                render = self.font.render(line, True, "#CC00DD" if self.pink else "black")
                self.field_surface.blit(render, [0, self.font.size(line)[1]*index,
                                                 self.font.size(line)[0], self.font.size(line)[1] ])
            self._updated = False

    def draw(self, screen):
        screen.blit(self.field_surface, self.field_rect)


