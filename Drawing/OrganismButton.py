from GameLogic.Coordinate import Coordinate
from Drawing.Button import Button
from GameLogic.Organism import Organism
from GameLogic.World import World
from GameLogic.Organisms.Animals.Wolf import Wolf
from GameLogic.Organisms.Animals.Sheep import Sheep
from GameLogic.Organisms.Animals.Cybersheep import Cybersheep
from GameLogic.Organisms.Animals.Antelope import Antelope
from GameLogic.Organisms.Animals.Fox import Fox
from GameLogic.Organisms.Animals.Tortoise import Tortoise
from GameLogic.Organisms.Plants.Hogweed import Hogweed
from GameLogic.Organisms.Plants.Grass import Grass
from GameLogic.Organisms.Plants.Guarana import Guarana
from GameLogic.Organisms.Plants.Dandelion import Dandelion
from GameLogic.Organisms.Plants.Nightshade import Nightshade
from GameLogic.Organisms.Elements.Fire import Fire
from GameLogic.Organisms.Elements.Water import Water


class OrganismButton(Button):
    organism: Organism

    def __init__(self, owner,  x, y, w, h, texture_dict, organism: Organism, world: World, position=Coordinate(0, 0)):
        super().__init__(owner, x, y, w, h, self.add_function, drag_button=True)
        self.texture_dictionary = texture_dict
        self.organism = organism
        self.position = organism.position if self.organism is not None else position
        self.world_pointer = world
        self.fill_colors = {
            'normal': '#111111',
            'hover': '#222222',
            'pressed': '#222222',
        }

    def add_function(self):
        if self.organism is None:
            self.world_pointer.add_organism(globals()[self.owner.paint](self.position))

    def draw(self, screen):
        if self.organism is not None:
            texture = self.texture_dictionary[self.organism.__class__.__name__]
            self.button_surface.blit(texture, [
                self.button_rect.width / 2 - texture.get_rect().width / 2,
                self.button_rect.height / 2 - texture.get_rect().height / 2
            ])
        screen.blit(self.button_surface, self.button_rect)

    def update(self):
        if self.organism is not None and (not self.organism.position == self.position or
                                          not self.world_pointer.is_organism_alive(self.organism)):
            self.organism = self.world_pointer.find_organism_at_position(self.position)
        elif self.organism is None:
            self.organism = self.world_pointer.find_organism_at_position(self.position)

        super().update()

