import os
import dir_helper
from utils2 import log
def clear_screen():
    os.system("cls" if os.path.exists("C:\\Windows\\System32\\cmd.exe") else "clear")

def clear_cache():
    dir_helper.enter_cache()
    current_dir_listing = os.scandir(os.getcwd())
    for entry in current_dir_listing:
        if str(entry.name).endswith(".png"):
            os.remove(entry.name)
    dir_helper.exit_cache()
    message = "Image cache cleared."
    input(f"\033[31m{message}\033[37m")
    log(message)
    return
