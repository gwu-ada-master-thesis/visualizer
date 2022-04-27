import os
import cv2

for image_path in os.listdir("../../pictures"):
    
    try:
        image = cv2.imread(f"../../pictures/{image_path}", 0)

        ret, inverted_thresholded_image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)

        cv2.imwrite(f"../../pictures/inverted/{image_path.split('.')[0]}_inverted.{image_path.split('.')[1]}", inverted_thresholded_image)

        print(image_path)
    except:
        continue