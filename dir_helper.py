import os

def enter_cache():
    if not "icache" in os.getcwd():
        if os.path.exists("icache/"):
            os.chdir("icache")
        else:
            os.mkdir("icache")
            os.chdir("icache")
    

def exit_cache():
    if "icache" in os.getcwd():
        os.chdir("..")

def cache_size():
    enter_cache()
    count = 0
    for entry in os.scandir(os.getcwd()):
        count += 1
    exit_cache()
    return count