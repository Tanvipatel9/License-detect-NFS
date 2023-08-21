'''
This code detects the license plate in the image and zooms 
into the area of interest (lisense plate) and then adds the zoomed
image into the shared directory 
'''


import cv2
import os 
import time
import numpy as np
from os import path

plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# obtaining list of all lisence plate images in 'plates' directory
plate_list = os.listdir('/home/vm4/Desktop/plate_photos')
print("TOTAL NUMBER OF PHOTOS: " + str(len(plate_list)) + "\n")

for plate in plate_list:

    img = cv2.imread('/home/vm4/Desktop/plate_photos/' + str(plate))
    orig_img = cv2.imread('/home/vm4/Desktop/plate_photos/' + str(plate))
   

    plates = plate_cascade.detectMultiScale(img, 1.3, 5)

    # locating the number plate in the image
    for (x,y,w,h) in plates:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
        cv2.putText(img, "No.Plate", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0,225,0), 1)
        break

    # zooming into the area of interest 
    plate_rect = plate_cascade.detectMultiScale(img,scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in plate_rect:
        # cropping image
        # img = img[y+10:y+h-8 ,x+6:x+w-10]
        img = img[y:y+h ,x-2:x+w-5]

    # resizing image (zoom in)
    height = img.shape[0]
    width = img.shape[1]
    dimensions = (width*2, height*2)
    img = cv2.resize(img, dimensions, interpolation = cv2.INTER_AREA)
    
    # creating windows for output images
    in_window_name = "Input_img"
    out_window_name = "Output_img"

    cv2.namedWindow(in_window_name) 
    cv2.namedWindow(out_window_name) 

    cv2.imshow(in_window_name, orig_img)
    cv2.imshow(out_window_name, img)
    
    cv2.moveWindow(in_window_name, 1000,0) 
    cv2.moveWindow(out_window_name, 0,0) 

    cv2.waitKey(1000)

    # saving the output image into the shared directory
    new_name = str(plate).split('.')
    file_name = new_name[0] + "_output.jpg"
    file_path = os.path.join("/mnt/nfs_clientshare/share_vm4", file_name)
    cv2.imwrite(file_path, img)

    time.sleep(4)
    cv2.destroyAllWindows()
    time.sleep(16)

