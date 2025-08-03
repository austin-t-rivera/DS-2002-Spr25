#!/usr/bin/python3

import os

Fav_animal = input('What is your favorite animal?')
Num_siblings = input('How many siblings do you have?')
Fav_class = input('What is your favorite class at UVA?')

os.environ['Fav_animal'] = 'dog'
os.environ['Num_siblings'] = 'five'
os.environ['Fav_class'] = 'Spiritual but not Religious'


os.environ['Plant'] = 'African Violet'
plant_env = os.getenv('Plant')
print(plant_env)
