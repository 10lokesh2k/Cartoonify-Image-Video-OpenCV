import cv2
import numpy as np

def cartoonimg():
        import easygui
        ImagePath=easygui.fileopenbox()

        img = cv2.imread(ImagePath)
        rs1 = cv2.resize(img, (550, 450))
        # Display the resulting frame
        cv2.imshow('Original Photo', rs1)
        
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Grayscale', gray)

        imgBlur = cv2.medianBlur(gray, 5)
        # cv2.imshow('Blurred', imgBlur)

        imgEdge = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        # cv2.imshow('Edge mask detection', imgEdge)

        colored = cv2.bilateralFilter(img, 9, 250, 250)
        cartoon = cv2.bitwise_and(colored, colored, mask=imgEdge)
        rs2 = cv2.resize(cartoon, (550, 450))
        cv2.imshow('Cartoon effect', rs2)
