import startup
import utils2
from dir_helper import cache_size

from cleanup import clear_screen as wipe
from menu_functions import search_and_display as SAD
from menu_functions import show_history as SH
from cleanup import clear_cache as CC
white = "\033[37m"

def readme():
    wipe()
    print("\033[33mSearch: Enter a search to pull from Google images.")
    print("History: Pulls images from cache to get an idea of search history.")
    print("Clear: Deletes all images in the cache.")
    print(f"Readme: Displays this screen.{white}")
    utils2.safe_string("","\nENTER")


menu_items = [SAD,SH,CC,readme,exit]
def main_menu():
    utils2.start_log()
    while True:
        wipe()
        print("\033[33mCache size: ",cache_size())
        print("\033[32m1. Search")
        print("\033[36m2. History")
        print("\033[31m3. Clear history")
        print(f"\033[35m4. Readme{white}")
        print("5. Quit")
        user_input = utils2.safe_int(3,-1,len(menu_items))
        menu_items[user_input]()
        
        

main_menu()

