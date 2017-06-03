#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main game entry point."""

from .world import World
from .entity import MyCharacter

def run():
    "Run the game."
    world = World()

    # Instantiate your character here and add it to the world:

    character = MyCharacter("Protagonist")
    world.add_entity(character)

    # We advance the world 20 timesteps
    for step in range(20):
        world.update()