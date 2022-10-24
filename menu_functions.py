import image_handler
import window
import utils2
import os
import random
import dir_helper
from cleanup import clear_screen as wipe
max_results = 18

def search_and_display():
    wipe()
    search_query = utils2.safe_string("Keanu Reeves","Search for images: ").strip().replace(' ','+')
    search_url = f"https://www.google.com/search?q={search_query}&tbm=isch&biw=1920&bih=941"
    image_links = image_handler.get_links(search_url)
    print(f"Search returned {len(image_links)} results.")
    image_links = utils2.slim_list(image_links,max_results)
    images = image_handler.download_images(image_links)
    utils2.log(f"Downloaded {len(image_links)} images.")
    print("Close all windows to continue...")
    window.gallery_rgb(images)

def show_history():
    images = []
    dir_helper.enter_cache()
    current_dir_listing = os.scandir(os.getcwd())
    for entry in current_dir_listing:
        if entry.name.endswith(".png"):
            images.append(entry.name)
    images = utils2.slim_list(images,15)
    print("Close all windows to continue...")
    utils2.log("History was accessed.")
    dir_helper.exit_cache()
    window.gallery_rgb(images)
