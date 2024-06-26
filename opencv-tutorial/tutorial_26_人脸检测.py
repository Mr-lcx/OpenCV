# cond
import cv2 as cv
import os
import numpy as np

'''
有点问题
,
还是跑不通

'''

def face_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(os.getcwd()+"\\haarcascade\\haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 5)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", image)


def main():
    # src = cv.imread("CrystalLiu1.jpg")
    # cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)

    # cv.imshow("input image", src)
    # face_detection(src)

    # 视频检测
    capture = cv.VideoCapture(0)
    cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
    while True:
        ret, frame = capture.read()
        # frame = cv.flip(frame, 0)
        face_detection(frame)
        c = cv.waitKey(10)
        if c == 27:
            break

    cv.waitKey(0)
    cv.destroyAllWindows()  # 关闭所有窗口


if __name__ == '__main__':
    main()