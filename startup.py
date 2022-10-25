import os
import os.path

if not path.exists("cache/"):
    os.mkdir("cache")

if not path.exists("Resources/"):
    print("\033[31mResources cannot be found! Reinstall!")
    exit()