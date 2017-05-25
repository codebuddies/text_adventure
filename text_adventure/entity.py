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
        # Something needed??
        pass

    def update(self):
        self.tiredness += 1
        
        self.thirst += 1 # Should only be called when not sleeping...

        print("Show what your character is currently doing.")
        print("If they get thirsty, they should leave and go get a drink.")
        print("Only once they get to the bar, they have the opportunity "
              " to drink, which happens with the next update call.")
        print("Once they're done drinking, their thirst should go back to 0.")
        print("When characters are tired, they should head off back home.")
        print("Once home, they don't get thirsty anymore. They loose 3"
              " tiredness at every update call.")
        print("Once rested, they can go back to work.")


