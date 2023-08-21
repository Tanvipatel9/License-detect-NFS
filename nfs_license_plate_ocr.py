'''
This file contains code to process the image given
to the run function for more clarity and then 
performs OCR on it to output the license plate number.
'''

import cv2
import pytesseract as pyt

# run ocr on 'plate' that is a path to a specific image 
def run(plate):

  path = str(plate)
  print("IMAGE PATH IS: " + path)

  img = cv2.imread(path)

  print("TYPE " + str(type(img)))
          
  print("IMAGE SHAPE IS: " + str(img.shape))
    
  height = img.shape[0]
  width = img.shape[1]

  print ("WIDTH: " + str(width))
  print ("HEIGHT: " + str(height))

  dimensions = (width*2, height*2)
  img = cv2.resize(img, dimensions, interpolation = cv2.INTER_AREA)

  # gray scaling image
  cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

  # smoothing image
  cv2.medianBlur(img,3)

  # contrast image
  img = cv2.convertScaleAbs(img, alpha=1.2, beta=10)

  # removing noise
  img = cv2.fastNlMeansDenoising(img, None, 20, 7, 21) 

  # performing OCR
  plate_number = (pyt.image_to_string(img, config = f'--psm 8 --oem 3 -c tessedit_char_whitelist=012456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'))
  # outputting number plate
  print("THE PLATE NUMBER IS: " + plate_number)
  img = cv2.resize(img, (400,200))

  # image with plate number - OUTPUT
  out_img = cv2.imread('/home/vm3/OpenCV/black_screen.jpg')
  out_img = cv2.resize(out_img, (400,200))
  text = str(plate_number)
  size = len(text)
  coordinates = (100,100)
  font = cv2.FONT_HERSHEY_DUPLEX
  out_img = cv2.putText(out_img, text[:size-2], coordinates, font, 1, (255,255,255), 2, cv2.LINE_AA)
  out_window_name = "Output_img"
  cv2.namedWindow(out_window_name)       
  cv2.imshow(out_window_name, out_img)
  cv2.moveWindow(out_window_name, 800,200) 

  # orig image of lisence plate - INPUT
  dimensions = (width, height)
  img = cv2.resize(img, dimensions, interpolation = cv2.INTER_AREA)
  in_window_name = "Input_img"
  cv2.namedWindow(in_window_name)       
  cv2.imshow(in_window_name, img)
  cv2.moveWindow(in_window_name, 100,200) 
  cv2.waitKey(3000)
  cv2.destroyAllWindows()


