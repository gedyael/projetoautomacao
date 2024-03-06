import time
import pyautogui

# definir o tempo
time.sleep(5) 

#pegar posição do mouse pra saber onde clicar
print(pyautogui.position())

#testar quanto de scrool

pyautogui.scroll(200)
