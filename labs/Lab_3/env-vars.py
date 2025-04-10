#!/usr/bin/python

import os

favorite_sport = input('What is your favorite sport? ')
favorite_color = input('What is your favorite color? ')
favorite_song = input('What is your favorite song? ')

os.environ["FAV_SPORT"] = favorite_sport
os.environ["FAV_COLOR"] = favorite_color
os.environ["FAV_SONG"] = favorite_song

print("Favorite sport:", os.environ["FAV_SPORT"])
print("Favorite color:", os.environ["FAV_COLOR"])
print("Favorite song:", os.environ["FAV_SONG"])