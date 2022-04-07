import cv2
from cv2 import EVENT_LBUTTONDOWN
from cv2 import FILLED
import numpy as np

img = cv2.imread('D:\workspace\Jupyter\PythonImageWorkSpace\OpenCV\poker.jpg')
RADIUS = 15
COLOR = (255, 0, 255)
Point_list = []
THICKNESS = 3
drawing = False

def Mouse_Handler(event, x, y, flags, param):
    global drawing
    dst_img = img.copy()

    if event == EVENT_LBUTTONDOWN:
        drawing = True
        Point_list.append((x, y))
        
    if drawing:
        prev_point = None
        for point in Point_list:
            cv2.circle(dst_img, point, RADIUS, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point

        next_point = (x, y)
        if len(Point_list) == 4:
            show_result()
            next_point = Point_list[0]
        cv2.line(dst_img, next_point, point, COLOR, THICKNESS, cv2.LINE_AA)
       
    
    cv2.imshow('img', dst_img)

def show_result():
    width, height = 530, 710

    src = np.float32(Point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow('result', result)

cv2.namedWindow('img')
cv2.setMouseCallback('img', Mouse_Handler)
cv2.waitKey(0)
cv2.destroyAllWindows()