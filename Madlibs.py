"""
This program generates passages that are generated in mad-lib format
Author: your-name
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs is starting"

name = raw_input("Enter a name:")

First_Adjective = raw_input("Enter an adjective:")

Second_Adjective = raw_input("Enter an adjective:")

Third_adjective = raw_input("Enter an adjective:")

First_verb = raw_input("Enter a verb:")

First_noun = raw_input("Enter a noun:")

Second_noun = raw_input("Enter a noun:")

Animal = raw_input("Enter an animal:")

Food = raw_input("Enter a food:")

Fruit = raw_input("Enter a fruit:")

Superhero = raw_input("Enter a superhero:")

Country = raw_input("Enter a country:")

Dessert = raw_input("Enter a dessert:")

Year = raw_input("Enter a year:")

Second_noun = raw_input("Enter a noun:")

print STORY % (name, First_Adjective, Second_Adjective, Animal, Food, First_verb, First_noun, Fruit, Third_adjective, name, Superhero, name, Country, name, Dessert, name, Year, Second_noun)









