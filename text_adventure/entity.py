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
        self.currentStatus=0
    def update(self):
        locationText = ["Working my ass off.","Drinking a nice beer","Zzzz"]
        transitionText = ["I'm too thirsty. Heading off to the bar!","Now I can go back to work.","I'm too tired to keep on working. I'll go back home get some sleep.","Drinking made me tired. I'll go back home get some sleep.","I had enough sleep. I'll go to work."]

        print(locationText[self.currentStatus])
        
        if self.currentStatus == 0:
            self.tiredness+=1
            self.thirst+=1
            if self.tiredness>=self.TOO_TIRED:
                self.currentStatus = 2
                print(transitionText[2])
            elif self.thirst>=self.TOO_THIRSTY:
                self.currentStatus=1
                print(transitionText[0])
        elif self.currentStatus == 1:
            self.tiredness+=1
            self.thirst=0
            if self.tiredness>=self.TOO_TIRED:
                self.currentStatus = 2
                print(transitionText[2])
            else:
                self.currentStatus=0
                print(transitionText[1])
        elif self.currentStatus == 2:
            self.tiredness-=3
            if self.tiredness<0:
                self.tiredness = 0
                print(transitionText[4])
                self.currentStatus = 0
       # self.tiredness += 1
        
      #  self.thirst += 1 # Should only be called when not sleeping...
'''
        print("If they get thirsty, they should leave and go get a drink.")
        print("Only once they get to the bar, they have the opportunity "
              " to drink, which happens with the next update call.")
        print("Once they're done drinking, their thirst should go back to 0.")
        print("When characters are tired, they should head off back home.")
        print("Once home, they don't get thirsty anymore. They loose 3"
              " tiredness at every update call.")
        print("Once rested, they can go back to work.")
'''
