#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Entity:
    """Base Entity to live in the World.

    Need to implement the `update` method which will be called by the World
    at every timestep.
    """

    TOO_THIRSTY = 2
    TOO_TIRED = 5

    def __init__(self, name):
        self.tiredness = 0
        self.thirst = 0
        self.name = name

    def update(self):
        raise NotImplementedError

class MyCharacter(Entity):

    TOO_THIRSTY = 2
    TOO_TIRED = 5

    def __init__(self, name):
        Entity.__init__(self, name)
        self.status = "working"
        self.thirst_counter = 1
        self.sleep_counter = 1

    def update(self):
        self.check_status()
        self.check_thirst()
        self.check_tiredness()
        self.thirst += self.thirst_counter
        self.tiredness += self.sleep_counter
        print(f"{self.name} is {self.status}")
        print(f"Tiredness: {self.tiredness}")
        print(f"Thirst: {self.thirst}")

    def check_status(self):
        if self.status == "working":
            self.working()
        if self.status == "sleeping":
            self.sleeping()
        if self.status == "at the bar":
            self.at_the_bar()

    def check_thirst(self):
        if self.thirst >= self.TOO_THIRSTY:
            self.status = "at the bar"
            print("I'm thirsty! Time for a drink!")

    def check_tiredness(self):
        if self.tiredness >= self.TOO_TIRED:
            self.status = "sleeping"
            print("YAWN! I'm going home!")

    def working(self):
        self.thirst_counter = 1
        self.sleep_counter = 1

    def sleeping(self):
        self.thirst_counter = 0
        self.sleep_counter = -3
        if self.tiredness <= 0:
            self.sleep_counter = 1
            self.thirst_counter = 1
            self.status = "working"

    def at_the_bar(self):
        self.thirst_counter = -3
        self.sleep_counter = 1
        if self.thirst <= 0:
            self.thirst_counter = 1
            self.status = "working"
