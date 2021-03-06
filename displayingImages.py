"""
    OpenCV python; Displaying images with OpenCV
    author:Grimmcrow

    In this script i'll use cv2.imshow(), cv2.imread(), cv2.write()

"""
import numpy as np
import cv2

"""
Use the function cv2.imread() to read an image.
The image should be in the working directory or a full path of image should be given.

Second argument is a flag which specifies the way image should be read.

    cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
    cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

Note
    Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

"""

#Default, show in color
img_default = cv2.imread("pic.jpg")

#Load image in gray scale
img_gray = cv2.imread("pic.jpg", 0)

#Load image unchaged
img_unchanged = cv2.imread("pic.jpg", -1)

"""
Display an image

Use the function cv2.imshow() to display an image in a window.
The window automatically fits to the image size.

First argument is a window name which is a string. second argument is our image.
You can create as many windows as you wish, but with different window names.

"""

cv2.imshow("default", img_default)

cv2.imshow("Gray Scale", img_gray)

#Create a window that is re-sizeable
cv2.namedWindow("unchanged", cv2.WINDOW_NORMAL)

cv2.imshow("Unchanged", img_unchanged)

#Wait infinitly for a keyboard input
cv2.waitKey(0)
#destroy all windows or an alternative can be used cv2.destroyWindow(window_name)
cv2.destroyAllWindows()

"""
Write an image

Use the function cv2.imwrite() to save an image.

First argument is the file name, second argument is the image you want to save.
"""

cv2.imwrite("pic_gray.jpg", img_gray)
