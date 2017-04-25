"""
This code will read file given as parameter and list what mana symbols it contains. 

created   Apr 2017
by CheapskateProjects

---------------------------
The MIT License (MIT)
Copyright (c) 2017 CheapskateProjects
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import cv2
import numpy as np
from os import listdir
import sys

if ( len(sys.argv) <= 1 ):
    print "Usage: <file to check>"
    sys.exit()

# Config
matchingThreshold = 0.7

# Read templates at the begining. Only once
green = cv2.imread('mana_icons/green_mana.jpg',0)
blue = cv2.imread('mana_icons/blue_mana.jpg',0)
red = cv2.imread('mana_icons/red_mana.jpg',0)
white = cv2.imread('mana_icons/white_mana.jpg',0)
black = cv2.imread('mana_icons/black_mana.jpg',0)
# All the mana logos are about the same size
w, h = green.shape[::-1]

def colorcheck( color_template, draw_color, img_gray ):
    results = cv2.matchTemplate(img_gray,color_template,cv2.TM_CCOEFF_NORMED)
    locations = np.where( results >= matchingThreshold)
    if len(zip(*locations[::-1])) > 0:
        return "Yes"
    else:
        return "No"

filename=sys.argv[1]
img_to_check = cv2.imread(filename)
img_gray = cv2.cvtColor(img_to_check, cv2.COLOR_BGR2GRAY)
print "Green: " + colorcheck(green, (0,255,0), img_gray)
print "Red: " + colorcheck(red, (0,0,255), img_gray)
print "Black: " + colorcheck(black, (0,0,0), img_gray)
print "Blue: " + colorcheck(blue, (255,0,0), img_gray)
print "White: " + colorcheck(white, (255,255,255), img_gray)


