#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class World:
    """World contains all the game `Entities`.

    The world advances one step for every `update` method call.
    """
    def __init__(self):
        self.entities = set()

    def add_entity(self, entity):
        "Add en entity to the world."
        self.entities.add(entity)

    def update(self):
        "Advance the world one step."
        for entity in self.entities:
            print("{}'s update:".format(entity.name))
            entity.update()
            print("-"*80)
