#!/usr/bin/env python3
from pprint import pprint

names = ["fluffy", "spot", "cujo"]
ages = [3, 7, 12]
animal = ["cat", "dog", "mean dog"]

# declaring variable as a dictionary
pets = {}

# loop thru names list
for i in names:
    # getting index value
    name_index = names.index(i)

    # Adding pet to the dictionary and creating age and animal entry
    pets[i] = {"age": ages[name_index], "animal": animal[name_index]}

pprint(pets)
