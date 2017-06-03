Practice Design Patterns through implementing a text based adventure game
-------------------------------------------------------------------------

This collaborative project aims at getting a feel for design patterns and what 
problems they try to solve.

If you're interested in joining us on this adventure, you can find us at
https://codebuddies.org/ (we're in the #python and #text-adventure channels in Slack).

### Instructions 

#### First assignment

1. Fork the code. (Or, if you've requested collaboration access in the #text-adventures channel on the [CodeBuddies](http://codebuddies.org) Slack, you can `git clone` the repo directly.)
2. Checkout the `original_prints` branch. 
3. Create a new branch based on the `original_prints` branch. Make your changes in your own repo.
4. Commit your changes. Once you're happy with your code, create a pull request -- or, if you've been added as a collaborator, simply push up the branch.

Your task is to implement the `MyCharacter` class found in 
text_adventure/entity.py. The `update` method contains print statements
explaining how the character should behave, and Workflow.png will give you
some hints on what order things should be happening in.

**WARNING:**  This code is going to throw an exception initially -  there are some things missing.  
Your mission is to find and fix those items! 

You can find an example of what the output might be like in 
`expected_output.txt`.

##### Our FIrst Design Pattern: **Finite State Machine**
After you've implemented your solution, check out the `state_machine` branch and try to see if you can rework your code following that pattern.


### Hangout reportback notes
24/7 hangout link: [https://codebuddies.org/hangout/9rasmyL5rp9igiDyZ](https://codebuddies.org/hangout/9rasmyL5rp9igiDyZ)

#### June 3rd, 2017
@dangillet:
```
We reviewed together the _naive_ way of implementing the problem and then we went through the _Finite State Machine_ pattern. It allows us to remove a level of `if` statements, and keep all the logic about one state in a single place.

I've pushed 2 branches. One is https://github.com/codebuddiesdotorg/text_adventure/tree/state_machine and shows the _basic_ implementation of the State machine for Python. It could be made more _formal_ by using an _Interface Class_ from which all the states derive. But as Python is a dynamic language, it's not really worth the effort.

I've pushed in another branch https://github.com/codebuddiesdotorg/text_adventure/tree/alt_implementation an alternate implementation using the fact that Python being dynamic, you can change the class of the `Entity` dynamically to have the desired implementation depending on the current state. I would not necessarily recommend doing it this way. I've discovered it while reading the Python Cookbook, 3rd edition. http://chimera.labs.oreilly.com/books/1230000000393

What I'm going now to do is merge the `state_machine` branch into master. From there we decided for practice to implement one or two more states. As we will do it all differently, we will rename our class whatever we want. Currently it was `MyCharacter`. I would suggest you take a name describing the kind of character you're going to implement. It could be a `Dog`, a `Vampire` or whatever floats your boat. As a fun experiment we will then merge all these classes and their states together and instantiate one of each character type to see them *living* in the world.

After that I think we will move on to *really* work on the foundation of the text based adventure game.
```




