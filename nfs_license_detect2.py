'''
This code detects the lisence plate in the image and zooms 
into the area of interest (lisense plate) and then adds the zoomed
image into the shared directory
'''

import cv2
import os 
import time
from os import path
from PIL import Image

time.sleep(6)
plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# obtaining list of all lisence plate images in 'plates' directory
plate_list = os.listdir('/home/vm5/Desktop/plate_photos')
print("TOTAL NUMBER OF PHOTOS: " + str(len(plate_list)) + "\n")

for plate in plate_list:

    img = cv2.imread('/home/vm5/Desktop/plate_photos/' + str(plate))
    cv2.imshow('original_image',img)


    # grascaling the image 
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img, 1.3, 5)

    # locating number plate in the image
    for (x,y,w,h) in plates:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
        break
            
    # zooming into the area of interest 
    plate_rect = plate_cascade.detectMultiScale(img,scaleFactor=1.05, minNeighbors=5)
    for (x,y,w,h) in plate_rect:
        # rescaling image
        img = img[y:y+h ,x-2:x+w-5]


    cv2.imshow('output_image.jpg',img)
    # display img for 4 sec
    cv2.waitKey(1000)

    # saving the output image into the shared directory
    new_name = str(plate).split('.')
    file_name = new_name[0] + "_output.jpg"
    file_path = os.path.join("/mnt/nfs_clientshare/share_vm5", file_name)
    cv2.imwrite(file_path, img)

    time.sleep(4)
    cv2.destroyAllWindows()
    time.sleep(16)
