from Drawing.Button import Button


class PaintButton(Button):

    def __init__(self, owner,  x, y, w, h, texture_dict, organism):
        super().__init__(owner, x, y, w, h, self.function)
        self.texture_dictionary = texture_dict
        self.organism = organism
        self.fill_colors = {
            'normal': '#000000',
            'hover': '#222222',
            'pressed': '#00CC22',
        }

    def function(self):
        self.owner.paint = self.organism

    def draw(self, screen):
        texture = self.texture_dictionary[self.organism]
        self.button_surface.blit(texture, [
            self.button_rect.width / 2 - texture.get_rect().width / 2,
            self.button_rect.height / 2 - texture.get_rect().height / 2
        ])
        screen.blit(self.button_surface, self.button_rect)

    def update(self):
        super().update()
        if self.owner.paint == self.organism:
            self.button_surface.fill(self.fill_colors['pressed'])

