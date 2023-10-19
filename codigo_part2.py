
import cv2
import numpy as np
from mss import mss
import pyautogui

template = cv2.imread('accept.png', cv2.IMREAD_GRAYSCALE)
banir = cv2.imread('banir.png', cv2.IMREAD_GRAYSCALE)
botaobanir = cv2.imread('botaobanir.png', cv2.IMREAD_GRAYSCALE)
urgot = cv2.imread('urgot.png', cv2.IMREAD_GRAYSCALE)

with mss() as sct:
  while True:
    template = np.array(sct.grab(sct.monitors[0]))
    sct_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(sct_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.70:
      top_left = max_loc
      bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
      click_x = top_left[0] + template.shape[1] // 2
      click_y = top_left[1] + template.shape[0] // 2
      pyautogui.moveTo(click_x, click_y)
      pyautogui.click()
      break

with mss() as sct:
    while True:
      banir = np.array(sct.grab(sct.monitors[0]))
      sct_gray = cv2.cvtColor(banir, cv2.COLOR_RGB2GRAY)
      result = cv2.matchTemplate(sct_gray, banir, cv2.TM_CCOEFF_NORMED)
      _, max_val, _, max_loc = cv2.minMaxLoc(result)

      if max_val > 0.70:
        top_left = max_loc
        bottom_right = (top_left[0] + banir.shape[1], top_left[1] + banir.shape[0])
        click_x = top_left[0] + banir.shape[1] // 2
        click_y = top_left[1] + banir.shape[0] // 2
        pyautogui.moveTo(click_x, click_y)
        pyautogui.click()
        break


      botaobanir = np.array(sct.grab(sct.monitors[0]))
      sct_gray = cv2.cvtColor(botaobanir, cv2.COLOR_RGB2GRAY)
      result = cv2.matchTemplate(sct_gray, botaobanir, cv2.TM_CCOEFF_NORMED)
      _, max_val, _, max_loc = cv2.minMaxLoc(result)

      if max_val > 0.70:
        top_left = max_loc
        bottom_right = (top_left[0] + botaobanir.shape[1], top_left[1] + botaobanir.shape[0])
        click_x = top_left[0] + botaobanir.shape[1] // 2
        click_y = top_left[1] + botaobanir.shape[0] // 2
        pyautogui.moveTo(click_x, click_y)
        pyautogui.click()
        break
    with mss() as sct:
        while True:
          urgot = np.array(sct.grab(sct.monitors[0]))
          sct_gray = cv2.cvtColor(urgot, cv2.COLOR_RGB2GRAY)
          result = cv2.matchTemplate(sct_gray, urgot, cv2.TM_CCOEFF_NORMED)
          _, max_val, _, max_loc = cv2.minMaxLoc(result)

          if max_val > 0.70:
            top_left = max_loc
            bottom_right = (top_left[0] + urgot.shape[1], top_left[1] + urgot.shape[0])
            click_x = top_left[0] + urgot.shape[1] // 2
            click_y = top_left[1] + urgot.shape[0] // 2
            pyautogui.scroll(-100)#TEM QUE ACHAR O NUMERO DO SCROLL PRA BAIXO
            pyautogui.moveTo(click_x, click_y)
            pyautogui.click()
            break






    # cv2.imshow('Screen', sct_gray) # Apenas para depuração
    if cv2.waitKey(1) & 0xFF== ord('q'):
      break

cv2.destroyAllWindows()
