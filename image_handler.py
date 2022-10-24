import requests
import shutil #Module for saving files to disk.
import utils2
from bs4 import BeautifulSoup #HTML Parser
import dir_helper

def download_images(image_links):
    dir_helper.enter_cache()
    file_names = []
    for image_link in image_links:
        file_name = utils2.generate_name(image_link) + ".png"
        try:
            res = requests.get(image_link,stream = True)
            with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw,f)
            file_names.append(file_name)
        except Exception as ex:
            utils2.log(f"Error! ({ex})")
    dir_helper.exit_cache()
    return file_names

def get_html(url):
    try:
        data = requests.get(url)
        if data.status_code == 200:
            return data.text
        else:
            return "Download failed"
    except:
        return "Invalid URL"
        
def get_links(page_url):
    image_links = []
    html = get_html(page_url)
    soup = BeautifulSoup(html,"html.parser")
    for img in soup.find_all("img"):
        #print(img["src"])
        image_links.append(img["src"])
    return image_links
    