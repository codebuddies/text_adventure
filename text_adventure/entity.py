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
        self.state = Working()

    def change_state(self, new_state):
        self.state.exit(self)
        self.state = new_state
        self.state.enter(self)

    def update(self):
        self.state.update(self)


class Working:
    def enter(self, entity):
        print("Let's get some work done!")

    def exit(self, entity):
        print("Leaving the office.")

    def update(self, entity):
        entity.tiredness += 1
        entity.thirst += 1

        print("Working my ass off.")

        if entity.thirst > entity.TOO_THIRSTY:
            print("I'm too thirsty. Heading off to the bar!")
            entity.change_state(Drinking())
        elif entity.tiredness > entity.TOO_TIRED:
            print("I'm too tired to keep on working. I'll go back home get"
                  " some sleep.")
            entity.change_state(Sleeping())

class Drinking:
    def enter(self, entity):
        print("Let's checkout this bar. They seem to have tap beers.")

    def exit(self, entity):
        print("Let's leave a tip before leaving the bar.")

    def update(self, entity):
        entity.tiredness += 1

        print("Drinking a nice beer")
        entity.thirst = 0

        if entity.tiredness > entity.TOO_TIRED:
            print("Drinking made me tired. I'll go back home get"
                  " some sleep.")
            entity.change_state(Sleeping())
        else:
            print("Now I can go back to work.")
            entity.change_state(Working())

class Sleeping:
    def enter(self, entity):
        print("Home, sweet home.")

    def exit(self, entity):
        print("Let's lock the front door before leaving home.")

    def update(self, entity):
        entity.tiredness += 1
        
        print("Zzzz")
        entity.tiredness -= 3
        if entity.tiredness <= 0:
            entity.tiredness = 0
            print("I had enough sleep. I'll go to work.")
            entity.change_state(Working())
