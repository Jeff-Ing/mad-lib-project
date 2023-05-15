"""
This program ask the user a series of questions, mad lib style
"""

import time
import sys

animal_one = input("Name an Animal: ")
food_one = input("Name a food: ")
noun_one = input("Noun: ")
verb_one = input("Verb: ")
verb_two = input("Verb: ")
verb_three = input("Verb: ")
verb_four = input("Verb: ")
noun_two = input("Noun: ")
location_one = input("Location: ")
noun_three = input("Noun: ")
noun_four = input("Noun: ")
location_two = input("Location: ")
verb_five = input("Verb: ")
food_two = input("Food: ")
game_one = input("Game: ")
verb_six = input("Verb: ")
noun_five = input("Noun: ")
noun_six = input("Noun: ")
noun_seven = input("Plural Noun: ")
verb_seven = input("Verb ending in -ing: ")
verb_eight = input("Verb: ")
noun_eight = input("Plural Noun: ")
verb_nine = input("Verb: ")


story = "If you give a " + str(animal_one) + " a " + str(food_one) + ", he/she is going to ask for a " + str(noun_one) + ". When you give him/her the " + str(noun_one) + ", he/she will want to " + str(verb_one) + ". When he/she is finished, he/she will " + str(verb_two) + " and " + str(verb_three) + " to the " + str(noun_two) + ". Since that doesn't work out, he/she will want to go to " + str(location_one) + ". On the way, he/she will see a " + str(noun_three) + " and will want " + str(noun_four) + ". The you will have to take him/her to the " + str(location_two) + ". He/she will " + str(verb_four) + ". When he/she is done, he/she will ask you for some " + str(food_two) + ". On the way home he/she will start a game of " + str(game_one) + ". When you finally get home, you'll have to " + str(verb_five) + ". Then he/she will want a " + str(noun_five) + ". You'll have to find a " + str(noun_six) + " and " + str(noun_seven) + ". When he/she sees the " + str(noun_seven) + ", he/she will start " + str(verb_six) + ". Then he/she will " + str(verb_seven) + " out of " + str(noun_eight) + ". Of course, when he/she is finished, he/she will want to " + str(verb_eight) + ", So, he/she will ask for a " + str(noun_one) + ". And chances are if you give him/her a " + str(noun_one) + ", he/she is going to want a " + str(food_one) + "."

for char in story:
    print(char, end='')
    sys.stdout.flush()
    time.sleep(.05)