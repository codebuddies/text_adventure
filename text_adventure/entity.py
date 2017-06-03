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
        super().__init__(name)
        self.current_status = Working()

    def change_status(self, new_status):
        self.current_status = new_status
        self.current_status.enter(self)

    def update(self):
        self.current_status.update(self)

class Working:
    def enter(self, entity):
        print("Let's get some work done!")

    def update(self, entity):
        entity.tiredness += 1
        entity.thirst += 1 
        print("Working my ass off")
        if entity.tiredness == entity.TOO_TIRED:
            print("I'll go back home get some sleep.")
            entity.change_status(Sleeping())
        elif entity.thirst == entity.TOO_THIRSTY:
            print("Heading off to the bar!")
            entity.change_status(Drinking())

class Drinking:
    def enter(self, entity):
        print("Heading off to the bar!")

    def update(self, entity):
        entity.tiredness += 1
        entity.thirst = 0
        print("Drinking a nice beer.")
        if entity.tiredness == entity.TOO_TIRED:
            print("I'll go back home get some sleep.")
            entity.change_status(Sleeping())
        elif entity.thirst == 0:
            print("I'll go to work.")
            entity.change_status(Working())

class Sleeping:
    def enter(self, entity):
        print("I'll go back home get some sleep.")
    def update(self, entity):
        print("Zzzz")
        entity.tiredness -= 3 
        entity.tiredness = max(entity.tiredness, 0) 
        if entity.tiredness == 0:
            entity.change_status(Working())

    # def check_status(self):
    #     print(self.current_status)
    #     if self.current_status == "Drinking a nice beer.":
    #         self.thirst = 0
    #         if self.tiredness == self.TOO_TIRED:
    #             print("I'll go back home get some sleep.")
    #             self.current_status = "Zzzz"
    #         elif self.thirst == 0:
    #             print("I'll go to work.")
    #             self.current_status = "Working my ass off"
    #     elif self.current_status == "Zzzz":
    #         self.tiredness -= 3 
    #         self.tiredness = max(self.tiredness, 0) 
    #         if self.tiredness == 0:
    #             print("I'll go to work.")
    #             self.current_status = "Working my ass off"
    #     elif self.current_status == "Working my ass off":
    #         if self.tiredness == self.TOO_TIRED:
    #             print("I'll go back home get some sleep.")
    #             self.current_status = "Zzzz"
    #         elif self.thirst == self.TOO_THIRSTY:
    #             print("Heading off to the bar!")
    #             self.current_status = 'Drinking a nice beer.'


#each user input will map to a transition, in the real text adventure game



