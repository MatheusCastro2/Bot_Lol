import pyautogui
import time


while True:
    butao = pyautogui.position(x=911, y=785)
    pyautogui.click(pyautogui.position(x=911, y=785))
    time.sleep(10)


    if(butao is None):
        continue
    else:
        print(butao)
        pyautogui.click(pyautogui.position(x=911, y=785))
        pyautogui.click(interval=10)
