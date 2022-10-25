import os
from os.path import exists

if not exists("cache/"):
    os.mkdir("cache")

if not exists("Resources/"):
    print("\033[31mResources cannot be found! Reinstall!")
    exit()