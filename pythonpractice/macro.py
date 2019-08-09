import os, time, subprocess
import pyautogui
from mss import mss
import numpy as np

start_x = 10
start_y = 550

bbox = (start_x, start_y, start_x + 500, start_y + 1)

cords_x = [10, 140, 270, 400]

def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(bbox)
            pyautogui.click(20, 400)
        t2 = time.time()
        print(t2 - t1)

def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)

def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            for cord in cords_x:
                # print(img.pixel(cord, 0))
                if img.pixel(cord, 0)[0] < 100 and img.pixel(cord, 0)[0] <= 230:
                    pyautogui.click(start_x + cord, start_y)
                    break

# test_time()
# print_mouse_pos()
time.sleep(1)
start()


# 10 520 , 140 520, 270 520, 400 520


# while True:
    # x, y = pyautogui.position()
    # position_str = 'x: ' + str(x) + 'Y: ' + str(y)
    # print(position_str)

# pyautogui.PAUSE = 0.08
#
# # position
# Line_1_button = [60, 620]
# Line_2_button = [182, 620]
# Line_3_button = [305, 620]
# Line_4_button = [430, 620]
#
# # 1387, 79 // 1880, 959 블루스택 왼쪽상단 부터 오른쪽 하단
# # 120(x)(가로) , 225(y)(높이)
# # 10, 500 // 10, 725  (1라인)
# # 132, 500 // 250, 725 (2라인)
# # 255, 500 // 380, 725 (3라인)
# # 380, 500 // 505, 725 (4라인)
# Line_1 = {'left': 10, 'top': 500, 'width': 115, 'height': 225}
# Line_2 = {'left': 132, 'top': 500, 'width': 115, 'height': 225}
# Line_3 = {'left': 255, 'top': 500, 'width': 115, 'height': 225}
# Line_4 = {'left': 380, 'top': 500, 'width': 115, 'height': 225}
#
# def click(coords):
#     pyautogui.moveTo(x=coords[0], y=coords[1], duration=0.01)
#     pyautogui.mouseDown()
#     pyautogui.mouseUp()
#
#
# def compute_icon_type(img):
#     mean = np.mean(img, axis=(0,1))
#     result = None
#
#     if mean[0] > 200 and mean[0] < 205 and mean[1] > 150 and mean[1] < 155 and mean[2] > 50 and mean[2] < 55:
#         result = 'START'
#
#     elif mean[0] > 0 and mean[0] < 0 and mean[1] > 0 and mean[1] < 0 and mean[2] > 0 and mean[2] < 0:
#         result = 'BLACKTILE'
#
#     elif mean[0] > 250 and mean[0] < 255 and mean[1] > 220 and mean[1] < 225 and mean[2] > 185 and mean[2] < 190:
#         result = 'BACKGROUND'
#
#     return result
#
#
# while True:
#     with mss.mss() as sct:
#         line_1_img = np.array(sct.grab(Line_1))[:, :, :3]
#         line_2_img = np.array(sct.grab(Line_2))[:, :, :3]
#         line_3_img = np.array(sct.grab(Line_3))[:, :, :3]
#         line_4_img = np.array(sct.grab(Line_4))[:, :, :3]
#
#         line_1_icon = compute_icon_type(line_1_img)
#         line_2_icon = compute_icon_type(line_2_img)
#         line_3_icon = compute_icon_type(line_3_img)
#         line_4_icon = compute_icon_type(line_4_img)
#
#         if line_1_icon == 'START' and (line_2_icon == 'START' and line_3_icon == 'START' and line_4_icon == 'START'):
#             print('TAP start!!!')
#             pyautogui.mouseDown()
#             pyautogui.mouseUp()
#
#         elif line_1_icon == 'BLACKTILE' and (line_2_icon == 'BLACKTILE' and line_3_icon == 'BLACKTILE' and line_4_icon == 'BLACKTILE'):
#             print('TAP blacktile!!!')
#             pyautogui.mouseDown()
#             pyautogui.mouseUp()
#
#         elif line_1_icon == 'BACKGROUND' and (
#                 line_2_icon == 'BACKGROUND' and line_3_icon == 'BACKGROUND' and line_4_icon == 'BACKGROUND'):
#             print('TAP background!!!')
#             pyautogui.mouseDown()
#             pyautogui.mouseUp()
#
#
# # start button
# # img_shape = 94, 125, 3
# # img BGR = 203, 158, 53
#
# # black_tile
# # img shape = 278, 157, 3
# # img BGR - 0, 0, 0
#
# # back_ground
# # img shape = 216, 127, 3
# # img BGR = 255, 223, 189
#
#
# # 이미지 BGR 값 구하기
# # img = cv2.imread('back_ground.png')
# # print(img.shape)
# # B = img.item(30, 30, 0)
# # G = img.item(30, 30, 1)
# # R = img.item(30, 30, 2)
# #
# # BGR = [B, G, R]
# # print(BGR)