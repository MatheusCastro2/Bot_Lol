import cv2
import numpy as np
from mss import mss
import pyautogui
import time


def selecao(botoes):  # Função para apertar botao
    with mss() as sct:
        while True:
            #Nessa parte ele vai tirar um screenshot da tela e converter para escala de cinza
            screenshot = np.array(sct.grab(sct.monitors[0]))
            sct_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
            result = cv2.matchTemplate(
                sct_gray, botoes, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result) #Aqui ele vai pegar o valor do match e a posição
            
            if max_val > 0.70: #Se o valor for maior que 0.70 ele vai clicar no botao
                top_left = max_loc #Aqui ele vai pegar a posição do botao
                click_x = top_left[0] + botoes.shape[1] // 2 #Aqui ele vai pegar o centro do botao
                click_y = top_left[1] + botoes.shape[0] // 2 #Aqui ele vai pegar o centro do botao
                pyautogui.moveTo(click_x, click_y)
                pyautogui.click()
                time.sleep(5)
                break


botao = cv2.imread('accept.png', cv2.IMREAD_GRAYSCALE)
banir_img = cv2.imread('banir.png', cv2.IMREAD_GRAYSCALE)
botaobanir_img = cv2.imread('botaobanir.png', cv2.IMREAD_GRAYSCALE)
urgot_img = cv2.imread('urgot.png', cv2.IMREAD_GRAYSCALE)
pick_img = cv2.imread('pick.png', cv2.IMREAD_GRAYSCALE)



selecao(botao)
selecao(banir_img)
selecao(botaobanir_img)
selecao(urgot_img)
selecao(pick_img)

cv2.destroyAllWindows() #Fecha todas as janelas
