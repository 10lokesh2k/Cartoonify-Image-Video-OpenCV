import cv2
import numpy as np

def pencilSketch():
        import easygui
        ImagePath=easygui.fileopenbox()

        img = cv2.imread(ImagePath)
        rs1 = cv2.resize(img, (550, 450))
        cv2.imshow("Original Photo", rs1)

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Gray Photo", gray_img)
        
        inverted_img = 255 - gray_img
        # cv2.imshow("Inverted", inverted_img)

        blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)
        inverted_blurred = 255 - blurred_img
        pencil_sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)
        rs2 = cv2.resize(pencil_sketch, (550, 450))
        cv2.imshow("Pencil Sketch", rs2)
