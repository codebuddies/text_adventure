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



    # def get_a_drink(self):
    #     print("Heading off to the bar!")
    #     if self.thirst > 1:
    #         self.thirst -= 1

    # def go_to_work(self):
    #     print("I had enough sleep. I'll go to work.")
    #     self.tiredness += 1
    #     self.thirst += 1


    # def sleep(self):
    #     print("Drinking made me tired. I'll go back home get some sleep.")
    #     self.thirst = 0
    #     self.tiredness = 0



        # print("Show what your character is currently doing.")
        # print("If they get thirsty, they should leave and go get a drink.")
        # print("Only once they get to the bar, they have the opportunity "
        #       " to drink, which happens with the next update call.")
        # print("Once they're done drinking, their thirst should go back to 0.")
        # print("When characters are tired, they should head off back home.")
        # print("Once home, they don't get thirsty anymore. They lose 3"
        #       " tiredness at every update call.")
        # print("Once rested, they can go back to work.")


