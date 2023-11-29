#!/usr/bin/env python3

from PIL import Image
import os
import filetype

def modify_images():
    """Resize (128, 128), rotate (-90 degrees) and save (as jpg) on directory of images"""
    read_directory = "/home/donsacafq/Module_26_project/images"
    write_directory = "/home/donsacafq/Module_26_project/converted_images"
    for filename in os.listdir(read_directory): # Iterate through list of files in appropriate directory
        path_and_filename = read_directory + "/" + filename # Concatenate path and file name
        if filetype.is_image(path_and_filename): # if file is an image, convert
            im = Image.open(path_and_filename)
            rgb_im = im.convert('RGB')
            rgb_im.rotate(270).resize((128,128)).save(write_directory + "/" + filename + ".jpg")

def main():
    modify_images()

if __name__ == "__main__":
    main()