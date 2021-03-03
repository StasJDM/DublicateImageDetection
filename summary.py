import os
import time
import imagehash
from PIL import Image

start_time = time.time()

IMAGE_PATH = "img/"

def get_image(image_name):
    return Image.open(IMAGE_PATH + image_name)

def get_ahash(image):
    return imagehash.average_hash(image)

def get_phash(image):
    return imagehash.phash(image)

def get_dhash(image):
    return imagehash.dhash(image)

def get_difference(hash_x, hash_y):
    return abs(hash_x - hash_y)

def print_difference_info(hash_x_number, hash_y_number):
    print("Image " + str(hash_x_number) + " - - - Image " + str(hash_y_number))
    print("Image " + str(hash_x_number) + ":")
    print(" - aHash: " + str(a_hashes[hash_x_number - 1]))
    print(" - dHash: " + str(d_hashes[hash_x_number - 1]))
    print(" - pHash: " + str(p_hashes[hash_x_number - 1]))
    print("Image " + str(hash_y_number) + ":")
    print(" - aHash: " + str(a_hashes[hash_y_number - 1]))
    print(" - dHash: " + str(d_hashes[hash_y_number - 1]))
    print(" - pHash: " + str(p_hashes[hash_y_number - 1]))
    print("Hash difference:")
    a_diff = get_difference(a_hashes[hash_x_number - 1], a_hashes[hash_y_number - 1]);
    d_diff = get_difference(d_hashes[hash_x_number - 1], d_hashes[hash_y_number - 1]);
    p_diff = get_difference(p_hashes[hash_x_number - 1], p_hashes[hash_y_number - 1]);
    print(" - Difference aHash : " +  str(a_diff))
    print(" - Difference dHash : " +  str(d_diff))
    print(" - Difference pHash : " +  str(p_diff))
    print()

images = [get_image("kvar_" + str(i) + ".jpg") for i in range(1, 13)]
a_hashes = [get_ahash(image) for image in images]
d_hashes = [get_dhash(image) for image in images]
p_hashes = [get_phash(image) for image in images]

while(True):
    x = int(input("First image number: "))
    y = int(input("Second image number: "))
    print_difference_info(x, y)

program_time = time.time() - start_time

print("Time: " + str(program_time))
