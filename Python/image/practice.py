import cv2
import numpy as np

img = cv2.imread('D:\workspace\Jupyter\PythonImageWorkSpace\OpenCV\cat.jpg')

def Mouse_Handler(event, x, y, flags, param):
    pass

cv2.namedWindow('img')
cv2.setMouseCallback('img', Mouse_Handler)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()