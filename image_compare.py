import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--new_image", type=str, default="new_image.jpg", help="path to new image")
ap.add_argument("-o", "--old_image", type=str, default="old_image.jpg", help="path to old image")
ap.add_argument("-t", "--threshold", type=int, default=10, help="threshold for pixel difference")
ap.add_argument("-s", "--kernel_size", type=int, default=3, help="kernel size for median filter")

args = vars(ap.parse_args())
 
grayscale_opened_new_img = cv2.imread(args["new_image"],0)
grayscale_opened_old_img = cv2.imread(args["old_image"],0)

bgr_opened_new_img = cv2.imread(args["new_image"])
bgr_opened_old_img = cv2.imread(args["old_image"])

height, width = np.size(grayscale_opened_new_img, 0), np.size(grayscale_opened_new_img, 1)

intermediate_array = grayscale_opened_new_img - grayscale_opened_old_img

for x in range(0, height):
    for y in range(0, width):
        if abs(intermediate_array[x][y]) < args["threshold"]:
            intermediate_array[x][y] = 255
        
intermediate_array = cv2.medianBlur(intermediate_array, args["kernel_size"])

for x in range(0, height):
    for y in range(0, width):
        if abs(intermediate_array[x][y]) == 255:
            bgr_opened_new_img[x][y] = [grayscale_opened_new_img[x][y], grayscale_opened_new_img[x][y], grayscale_opened_new_img[x][y]]
        else:
            bgr_opened_new_img[x][y] = [0,0,255]                    

cv2.imwrite("Compared_image.jpg", bgr_opened_new_img)


