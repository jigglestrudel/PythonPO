import pygame


class Button:
    def __init__(self, owner, x, y, width, height, onclick_function, hover_function=None, drag_button=False):
        self.owner = owner
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclick_function = onclick_function
        self.hover_function = hover_function

        self.fill_colors = {
            'normal': '#000000',
            'hover': '#333333',
            'pressed': '#666666',
        }

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.alreadyPressed = False
        self.alreadyHovered = False
        self.drag_button = drag_button

    def draw(self, screen):
        screen.blit(self.button_surface, self.button_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        self.button_surface.fill(self.fill_colors['normal'])
        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.fill_colors['hover'])
            if self.hover_function is not None and not self.alreadyHovered:
                self.hover_function()
                self.alreadyHovered = True

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.button_surface.fill(self.fill_colors['pressed'])

                if not self.alreadyPressed:
                    self.onclick_function()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False
        elif self.drag_button:
            self.alreadyPressed = False


