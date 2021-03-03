import os
import time
import imagehash
from PIL import Image

IMAGE_PATH = "img/"
image_name = "kvar_1.jpg"

def get_image(image_name):
    return Image.open(IMAGE_PATH + image_name)

def get_ahash(image):
    return imagehash.average_hash(image)

def get_phash(image):
    return imagehash.phash(image)

def get_dhash(image):
    return imagehash.dhash(image)

def get_ahash_by_image_path(image_name):
    image = get_image(image_name)
    return get_ahash(image)

def get_phash_by_image_path(image_name):
    image = get_image(image_name)
    return get_phash(image)

def get_dhash_by_image_path(image_name):
    image = get_image(image_name)
    return get_dhash(image)

#image = get_image(image_name)

start_time = time.time()

for i in range(1000):
    img_h = get_phash_by_image_path(image_name)

program_time = time.time() - start_time

print("Time: " + str(program_time))
