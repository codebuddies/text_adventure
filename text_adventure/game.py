#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main game entry point."""

from .world import World
from .spaghetti_entity import MyDemoCharacter

def run():
    "Run the game."
    world = World()

    # Instantiate your character here and add it to the world:
    dan = MyDemoCharacter("Dan")
    world.add_entity(dan)

    # We advance the world 20 timesteps
    for step in range(20):
        world.update()