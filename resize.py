# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:09:44 2019

@author: Iraklis Kalamas
"""
# Resize an image using python

import os, re
from PIL import Image

def main():

    #Asking the resize factor from the user and check if its correct.
    n = input("Resize factor (between 1 and 5): ")
    while(True):
        if (n not in ["1", "2", "3", "4", "5"]):
            n = input("Resize factor (between 1 and 5): ")
        else:
            n = int(n)
            break
        
    #Asking the original image name from the user and check if its correct.        
    infile = input("Original image name: ")
    while not (os.path.isfile(infile)):
        print("This file doesn't exist")
        infile = input("Original image name: ")
    
    #Asking the resized image name from the user and check if its correct. 
    outfile = input("Resized image name: ")
    while (True):
        if len(outfile) == 0:
            print("Input a new file name.")
            outfile = input("Resized image name: ")
        else:
            imageName = re.compile(r".+\.jpg")
            img = imageName.search(outfile)
            if (img == None):
                print("Input a new file name.")
                outfile = input("Resized image name: ")
            else:
                break
    
    #Import - Resize - Export
    inimage = Image.open(infile)
    width, height = inimage.size
    outimage = inimage.resize((width * n, height * n))
    outimage.save(outfile)


if __name__ == "__main__":
    main()
