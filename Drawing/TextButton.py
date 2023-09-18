import pygame
from Drawing.Button import Button


class TextButton(Button):
    def __init__(self, owner, x, y, width, height, onclick_function, font, button_text='Button'):
        super().__init__(owner, x, y, width, height, onclick_function)
        self._button_text = button_text
        self.font = font
        self.button_surf = font.render(button_text, True, (200, 0, 255))


    @property
    def text(self):
        return self._button_text

    @text.setter
    def text(self, t):
        self._button_text = t
        self.button_surf = self.font.render(self._button_text, True, (200, 0, 255))

    def draw(self, screen):
        self.button_surface.blit(self.button_surf, [
            self.button_rect.width / 2 - self.button_surf.get_rect().width / 2,
            self.button_rect.height / 2 - self.button_surf.get_rect().height / 2
        ])
        screen.blit(self.button_surface, self.button_rect)



