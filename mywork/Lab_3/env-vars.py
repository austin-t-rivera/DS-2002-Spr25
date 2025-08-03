#!/usr/bin/python3

import os

fav_food = input("What is your favorite food? ")
fav_show = input("What is your favorite show? ")
fav_subject = input("What is your favorite subject? ")

os.environ["FAV_FOOD"] = fav_food
os.environ["FAV_SHOW"] = fav_show
os.environ["FAV_SUBJECT"] = fav_subject

print("\nStored Environment Variables:")
print("Favorite Food:", os.getenv("FAV_FOOD"))
print("Favorite Show:", os.getenv("FAV_SHOW"))
print("Favorite Subject:", os.getenv("FAV_SUBJECT"))
