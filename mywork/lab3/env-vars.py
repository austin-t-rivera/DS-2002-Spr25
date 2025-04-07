#!/usr/bin/python3

import os

os.environ["FAV_GENRE"] = "R&B"
os.environ ["YEAR"]= "Fourth Year"
os.environ ["CITIZEN"] = "Yes"

FAV_GENRE = input("What is your favorit genre of music?")
YEAR  = input("What year are you at UVA?")
CITIZEN = input("Are you a citizen of the United States?")

print(os.getenv("FAV_GENRE"))
print(os.getenv("YEAR"))
print(os.getenv("CITIZEN"))


