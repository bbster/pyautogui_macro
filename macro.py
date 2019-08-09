import os

import pyautogui
import mss, cv2
import numpy as np


# start = pyautogui.locateAllOnScreen('start.jpg', grayscale=True)
# pyautogui.click(start)
#
# tile = pyautogui.locateAllOnScreen('black_tile.jpg', grayscale=True)
# pyautogui.click(tile)


# print(pyautogui.position())

# while True:
#     point = pyautogui.position()
#     print(point)

    # 1575, 637 시작버튼 좌표
    # 1387, 79 // 1880, 959 블루스택 왼쪽상단 부터 오른쪽 하단

# def icon_type(img):
#     mean = np.mean(img, axis=(0,1))

# _img = np.array(pyautogui.screenshot())
# img = cv2.cvtColor(_img, cv2.COLOR_RGB2GRAY)



start = cv2.imread(("start.jpg", cv2.IMREAD_GRAYSCALE))

cv2.imshow("start", start)
cv2.waitKey(0)
cv2.destroyAllWindows()