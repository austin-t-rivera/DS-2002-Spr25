#!/c/Users/justi/AppData/Local/Microsoft/WindowsApps/python3

import os

os.environ["FAV_SUBJECT"] = input('What is your favorite subject? ')
os.environ["PETS"] = input('Do you have any pets? ')
os.environ["BELIEF"] = input('Do you believe in a God? ')

FAV_SUBJECT_ENV = os.getenv("FAV_SUBJECT")
PETS_ENV = os.getenv("PETS")
BELIEF_ENV = os.getenv("BELIEF")

print(FAV_SUBJECT_ENV)
print(PETS_ENV)
print(BELIEF_ENV)
