
import cv2
import numpy as np
from mss import mss
import pyautogui
import time

template_img = cv2.imread('accept.png', cv2.IMREAD_GRAYSCALE)
banir_img = cv2.imread('banir.png', cv2.IMREAD_GRAYSCALE)
botaobanir_img = cv2.imread('botaobanir.png', cv2.IMREAD_GRAYSCALE)
urgot_img = cv2.imread('urgot.png', cv2.IMREAD_GRAYSCALE)
pick_img = cv2.imread('pick.png', cv2.IMREAD_GRAYSCALE)

with mss() as sct:
    while True:
        screenshot = np.array(sct.grab(sct.monitors[0]))
        sct_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(
            sct_gray, template_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.70:
            top_left = max_loc
            bottom_right = (top_left[0] + template_img.shape[1],
                            top_left[1] + template_img.shape[0])
            click_x = top_left[0] + template_img.shape[1] // 2
            click_y = top_left[1] + template_img.shape[0] // 2
            pyautogui.moveTo(click_x, click_y)
            pyautogui.click()
            break

with mss() as sct:
    while True:
        screenshot1 = np.array(sct.grab(sct.monitors[0]))
        sct_gray = cv2.cvtColor(screenshot1, cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(sct_gray, banir_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.70:
            top_left = max_loc
            bottom_right = (top_left[0] + banir_img.shape[1],
                            top_left[1] + banir_img.shape[0])
            click_x = top_left[0] + banir_img.shape[1] // 2
            click_y = top_left[1] + banir_img.shape[0] // 2
            pyautogui.moveTo(click_x, click_y)
            pyautogui.click()
            time.sleep(5)
            break

with mss() as sct:
    while True:
        screenshot2 = np.array(sct.grab(sct.monitors[0]))
        sct_gray = cv2.cvtColor(screenshot2, cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(
            sct_gray, botaobanir_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.70:
            top_left = max_loc
            bottom_right = (
                top_left[0] + botaobanir_img.shape[1], top_left[1] + botaobanir_img.shape[0])
            click_x = top_left[0] + botaobanir_img.shape[1] // 2
            click_y = top_left[1] + botaobanir_img.shape[0] // 2
            pyautogui.moveTo(click_x, click_y)
            pyautogui.click()
            time.sleep(5)
            break

with mss() as sct:
    while True:
        screenshot3 = np.array(sct.grab(sct.monitors[0]))
        sct_gray = cv2.cvtColor(screenshot3, cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(sct_gray, urgot_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.70:
            top_left = max_loc
            bottom_right = (top_left[0] + urgot_img.shape[1],
                            top_left[1] + urgot_img.shape[0])
            click_x = top_left[0] + urgot_img.shape[1] // 2
            click_y = top_left[1] + urgot_img.shape[0] // 2
            pyautogui.moveTo(click_x, click_y)
            pyautogui.click()
            time.sleep(5)
            break

with mss() as sct:
    while True:
        screenshot4 = np.array(sct.grab(sct.monitors[0]))
        sct_gray = cv2.cvtColor(screenshot4, cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(sct_gray, pick_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.70:
            top_left = max_loc
            bottom_right = (top_left[0] + pick_img.shape[1],
                            top_left[1] + pick_img.shape[0])
            click_x = top_left[0] + pick_img.shape[1] // 2
            click_y = top_left[1] + pick_img.shape[0] // 2
            pyautogui.moveTo(click_x, click_y)
            pyautogui.click()
            time.sleep(5)
            break

    # cv2.imshow('Screen', sct_gray) # Apenas para depuração
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
