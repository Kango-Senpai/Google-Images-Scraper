import os

def enter_cache():
    if os.path.exists("cache/"):
        os.chdir("cache")

def exit_cache():
    if "cache" in os.getcwd():
        os.chdir("..")

def cache_size():
    if "cache" not in os.getcwd():
        enter_cache()
    count = 0
    for entry in os.scandir(os.getcwd()):
        count += 1
    if "cache" in os.getcwd():
        exit_cache()
    return count