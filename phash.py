import os
import time
import imagehash
from PIL import Image

start_time = time.time()

IMAGE_PATH = "img/"
image_1_name = "kvar_1.jpg"
image_2_name = "kvar_2.jpg"

def get_image(image_name):
    return Image.open(IMAGE_PATH + image_name)

def get_hash(image_name):
    image = get_image(image_name)
    return imagehash.phash(image)

def get_difference(hash_x, hash_y):
    return abs(hash_x - hash_y)

img_1_h = get_hash(image_1_name)
img_2_h = get_hash("image_2_name)

print(img_1_h)
print(img_2_h)
print(get_difference(img_1_h, img_2_h))

program_time = time.time() - start_time
print(program_time)
