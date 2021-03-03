import os
import time
import imagehash
from PIL import Image

start_time = time.time()

IMAGE_PATH = "img/"
image_original_name = "kvar_11.jpg"
image_cropped_name = "kvar_13.jpg"

def get_image(image_name):
    return Image.open(IMAGE_PATH + image_name)

def get_hash(image_name):
    image = get_image(image_name)
    return imagehash.crop_resistant_hash(image)

def get_difference(hash_original, hash_cropped):
    return hash_original.hash_diff(hash_cropped)

image_original = get_hash(image_original_name)
image_cropped = get_hash(image_cropped_name)
diff = get_difference(image_original, image_cropped)

program_time = time.time() - start_time

print(image_original_name + " : " + str(image_original))
print(image_cropped_name + " : " + str(image_cropped))
print("Difference: " + str(diff))
print("Time: " + str(program_time))
