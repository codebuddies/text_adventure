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

    def change_state(self, new_state):
        self.exit()
        self.__class__ = new_state
        self.enter()

    def update(self):
        raise NotImplementedError


class MyCharacter(Entity):

    def __init__(self, name):
        super().__init__(name)
        self.__class__ = Working

    def update(self):
        self.update()


class Working(MyCharacter):

    def enter(self):
        print("Let's get some work done!")

    def exit(self):
        print("Leaving the office.")

    def update(self):
        self.tiredness += 1
        self.thirst += 1

        print("Working my ass off.")

        if self.thirst > self.TOO_THIRSTY:
            print("I'm too thirsty. Heading off to the bar!")
            self.change_state(Drinking)
        elif self.tiredness > self.TOO_TIRED:
            print("I'm too tired to keep on working. I'll go back home get"
                  " some sleep.")
            self.change_state(Sleeping)

class Drinking(MyCharacter):
    def enter(self):
        print("Let's checkout this bar. They seem to have tap beers.")

    def exit(self):
        print("Let's leave a tip before leaving the bar.")

    def update(self):
        self.tiredness += 1

        print("Drinking a nice beer")
        self.thirst = 0

        if self.tiredness > self.TOO_TIRED:
            print("Drinking made me tired. I'll go back home get"
                  " some sleep.")
            self.change_state(Sleeping)
        else:
            print("Now I can go back to work.")
            self.change_state(Working)

class Sleeping(MyCharacter):
    def enter(self):
        print("Home, sweet home.")

    def exit(self):
        print("Let's lock the front door before leaving home.")

    def update(self):
        self.tiredness += 1
        
        print("Zzzz")
        self.tiredness -= 3
        if self.tiredness <= 0:
            self.tiredness = 0
            print("I had enough sleep. I'll go to work.")
            self.change_state(Working)
