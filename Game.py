import pygame
from pygame import Surface, SurfaceType
from pygame.time import Clock
import pickle

from GameLogic import World
from GameLogic.Coordinate import Coordinate
from Drawing.OrganismButton import OrganismButton
from Drawing.PaintButton import PaintButton
from Drawing.TextButton import TextButton
from Drawing.TextField import TextField


class Game:
    py_clock: Clock
    py_screen: Surface | SurfaceType

    def __init__(self):
        pygame.init()
        self.py_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.py_clock = pygame.time.Clock()
        self.running = True
        self.py_objects = []
        self.world = World.World(20, 20)
        self.world.fill_with_wolves()

        self.py_font = pygame.font.SysFont('Comic Sans', 40)
        self.py_font_text = pygame.font.SysFont('Comic Sans', 15)
        self.py_font_signature = pygame.font.SysFont('Comic Sans', 25)
        self.tile_size = 48

        self.texture_dictionary = {
            "Wolf": pygame.image.load("Textures/wolf.png"),
            "Sheep": pygame.image.load("Textures/sheep.png"),
            "Fox": pygame.image.load("Textures/fox.png"),
            "Tortoise": pygame.image.load("Textures/tortoise.png"),
            "Antelope": pygame.image.load("Textures/antelope.png"),
            "Cybersheep": pygame.image.load("Textures/cybersheep.png"),
            "Grass": pygame.image.load("Textures/grass.png"),
            "Dandelion": pygame.image.load("Textures/dandelion.png"),
            "Guarana": pygame.image.load("Textures/guarana.png"),
            "Nightshade": pygame.image.load("Textures/nightshade.png"),
            "Hogweed": pygame.image.load("Textures/hogweed.png"),
            "Human": pygame.image.load("Textures/human.png"),
            "Fire": pygame.image.load("Textures/fire.png"),
            "Water": pygame.image.load("Textures/water.png"),
        }

        self.paint = "Fox"

        for x in range(self.world.width):
            for y in range(self.world.height):
                organism = self.world.find_organism_at_position(Coordinate(x, y))
                self.py_objects.append(OrganismButton(self, self.tile_size * x, self.tile_size * y,
                                                      self.tile_size, self.tile_size, self.texture_dictionary,
                                                      organism, self.world, Coordinate(x, y)))

        self.py_objects.append(TextButton(self, self.world.width * self.tile_size + 130, 5, 200, 100, self.update_world,
                                          self.py_font, "next turn"))
        self.py_objects.append(TextButton(self, self.world.width * self.tile_size + 130, 105, 200, 100, self.clear_world,
                                          self.py_font, "clear"))
        self.py_objects.append(TextButton(self, self.world.width * self.tile_size + 130, 205, 200, 100,
                                          self.randomize_world, self.py_font, "randomize"))
        self.py_objects.append(TextButton(self, self.world.width * self.tile_size + 130, 305, 200, 100, self.load_game,
                                          self.py_font, "load"))
        self.py_objects.append(TextButton(self, self.world.width * self.tile_size + 130, 405, 200, 100, self.save_game,
                                          self.py_font, "save"))

        self.py_objects.append(TextField(self.world.width * self.tile_size + 330, 5, 200, 100, self.py_font_signature,
                                         ["Tomasz Krępa", "193047"], pink=True))
        self.activate_button = TextButton(self, self.world.width * self.tile_size + 330, 305, 200, 100,
                                          self.activate_human,
                                          self.py_font, "activate")
        self.py_objects.append(self.activate_button)
        self.py_objects.append(TextButton(self, self.world.width * self.tile_size + 330, 405, 200, 100, self.quit_game,
                                          self.py_font, "quit"))

        self.history_field = TextField(self.world.width * self.tile_size + 10, 550, 550, 400, self.py_font_text,
                                       ["History will appear here"])
        self.py_objects.append(self.history_field)

        for index, value in enumerate(self.texture_dictionary.keys()):
            if value == "Human":
                continue
            self.py_objects.append(
                PaintButton(self, self.world.width * self.tile_size + 10 + self.tile_size*(index//12), self.tile_size * (index%12) + 5,
                            self.tile_size, self.tile_size, self.texture_dictionary, value))

    def update_world(self):
        self.world.manage_organisms()
        self.update_dynamic_fields()

    def clear_world(self):
        self.world.clear()
        self.update_dynamic_fields()

    def update_dynamic_fields(self):
        self.history_field.text = self.world.get_events() if len(self.world.get_events()) > 0 else ["History will appear here"]
        turns_left = self.world.human_get_turns_left()
        if turns_left is None:
            self.activate_button.text = "respawn"
        else:
            self.activate_button.text = str(turns_left) if turns_left != 0 else "activate"

    def randomize_world(self):
        self.clear_world()
        self.world.fill_with_wolves()
        self.update_dynamic_fields()

    def quit_game(self):
        self.running = False

    def activate_human(self):
        if self.activate_button.text == "respawn":
            self.world.spawn_human()
        else:
            self.world.human_activate()
        self.update_dynamic_fields()
    def game_loop(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        self.world.human_set_direction("DOWN")
                    elif pygame.key.get_pressed()[pygame.K_UP]:
                        self.world.human_set_direction("UP")
                    elif pygame.key.get_pressed()[pygame.K_LEFT]:
                        self.world.human_set_direction("LEFT")
                    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                        self.world.human_set_direction("RIGHT")
                    self.update_world()



            for obj in self.py_objects:
                obj.update()

            self.py_screen.fill("#FF00FF")

            for obj in self.py_objects:
                obj.draw(self.py_screen)

            pygame.display.flip()

            self.py_clock.tick(60)

    def save_game(self):
        try:
            with open('save.sav', 'wb') as file:
                pickle.dump(self.world, file)
        except IOError as e:
            print("Error saving game:", e)

    def load_game(self):
        try:
            with open('save.sav', 'rb') as file:
                game_state = pickle.load(file)
                self.world = game_state

        except IOError as e:
            print("Error loading game:", e)

        self.world.make_organisms_yours()
        self.update_dynamic_fields()
        for obj in self.py_objects:
            if isinstance(obj, OrganismButton):
                obj.world_pointer = self.world
                obj.organism = self.world.find_organism_at_position(obj.position)
