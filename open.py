#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deejay
#
# Created:     12/05/2014
# Copyright:   (c) Deejay 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *

import os

import tkFileDialog

from PIL import Image

def imageopen():
    poop = Tk()
    poop.withdraw()

    img = tkFileDialog.askopenfilename()
    #oimage = Image.open(img)
    return img


def imageopen_forPIL():
    poop = Tk()
    poop.withdraw()

    img = tkFileDialog.askopenfilename()
    oimage = Image.open(img)
    return oimage

#imageopen test
#picture = imageopen()
#print picture
#width, height = picture.size
#print "The Height is: ", height, "The width: ", width
