import os
from os.path import exists

if not exists("icache/"):
    os.mkdir("icache")

if not exists("Resources/"):
    print("\033[31mResources cannot be found! Reinstall!")
    exit()