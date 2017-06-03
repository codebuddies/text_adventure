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

    def __init__(self, name):
        self.name = name
        self.tiredness = 0
        self.thirst = 0
        self.current_status = 'Drinking a nice beer.'
        pass

    def update(self):
        self.tiredness += 1#
        if not self.current_status == "Zzzz":
            self.thirst += 1 # Should only be called when not sleeping...
        self.check_status()

    def check_status(self):
        #printint out current status
        print(self.current_status)
        if self.current_status == "Drinking a nice beer.":
            self.thirst = 0
            if self.tiredness == self.TOO_TIRED:
                print("I'll go back home get some sleep.")
                self.current_status = "Zzzz"
            elif self.thirst == 0:
                print("I'll go to work.")
                self.current_status = "Working my ass off"
        elif self.current_status == "Zzzz":
            self.tiredness -= 3 
            self.tiredness = max(self.tiredness, 0) 
            if self.tiredness == 0:
                print("I'll go to work.")
                self.current_status = "Working my ass off"
        elif self.current_status == "Working my ass off":
            if self.tiredness == self.TOO_TIRED:
                print("I'll go back home get some sleep.")
                self.current_status = "Zzzz"
            elif self.thirst == self.TOO_THIRSTY:
                print("Heading off to the bar!")
                self.current_status = 'Drinking a nice beer.'






