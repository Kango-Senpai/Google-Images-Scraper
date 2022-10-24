import matplotlib.pyplot as plt
from cv2 import imread, cvtColor, COLOR_BGR2RGB
import os
from dir_helper import enter_cache, exit_cache
from resources import DefaultImage
def gallery_rgb(images):
    image_index = 0
    plt.figure()
    f, plots = plt.subplots(3,5,figsize=(20,20))
    enter_cache()
    for x in range(len(plots)):
        for y in range(len(plots[x])):
            image = imread(DefaultImage.path)
            try:
                image = imread(images[image_index])
            except:
                image = imread(DefaultImage.path)
            finally:
                processed_image = cvtColor(image,COLOR_BGR2RGB)
                plots[x][y].imshow(processed_image)
                image_index += 1
    exit_cache()
    plt.show()