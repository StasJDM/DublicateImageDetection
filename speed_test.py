import os
import time
import imagehash
from PIL import Image

IMAGE_PATH = "img/"
image_name_1 = "kvar_1.jpg"
image_name_2 = "kvar_5.jpg"

def get_image(image_name):
    return Image.open(IMAGE_PATH + image_name)

def get_ahash(image):
    return imagehash.average_hash(image)

def get_phash(image):
    return imagehash.phash(image)

def get_dhash(image):
    return imagehash.dhash(image)

def get_whash(image):
    return imagehash.whash(image)

def get_colorhash(image):
    return imagehash.colorhash(image)

def get_crop_resistant_hash(image):
    return imagehash.crop_resistant_hash(image)

def get_ahash_by_image_path(image_name):
    image = get_image(image_name)
    return get_ahash(image)

def get_phash_by_image_path(image_name):
    image = get_image(image_name)
    return get_phash(image)

def get_dhash_by_image_path(image_name):
    image = get_image(image_name)
    return get_dhash(image)

def get_whash_by_image_path(image_name):
    image = get_image(image_name)
    return get_whash(image)

def get_colorhash_by_image_path(image_name):
    image = get_image(image_name)
    return get_colorhash(image)

def get_crop_resistant_hash_by_image_path(image_name):
    image = get_image(image_name)
    return get_crop_resistant_hash(image)

def get_difference(hash_x, hash_y):
    return abs(hash_x-hash_y)

def get_crop_difference(hash_original, hash_cropped):
    return hash_original.hash_diff(hash_cropped)

image_1 = get_image(image_name_1)
image_2 = get_image(image_name_2)

image_1_hash = get_crop_resistant_hash(image_1)
image_2_hash = get_crop_resistant_hash(image_2)

start_time = time.time()

for i in range(10000):
    diff = get_crop_difference(image_1_hash, image_2_hash)

program_time = time.time() - start_time

print("Time: " + str(program_time))
