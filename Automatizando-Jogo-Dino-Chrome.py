import pyautogui
from PIL import ImageGrab
import time

##https://chrome://dino
aux = 0
#pyautogui.press()

while True:
    tela = ImageGrab.grab()

    for x in range(300+int(aux), 400+int(aux)):
        
        area = tela.getpixel((x, 510))
#172
        if area[0] == 83:
            pyautogui.press("up")
            break

        area = tela.getpixel((x, 510))
#172
        if area[0] == 172:
            pyautogui.press("up")
            break
### pular






        area = tela.getpixel((x, 412))
        if area[0] == 83:
            x = 0.5
            pyautogui.keyDown("down")
            time.sleep(x)
            pyautogui.keyUp("down")
            #pyautogui.press("down")
            break



        area = tela.getpixel((x, 412))
#172
        if area[0] == 172:
            x = 0.5
            pyautogui.keyDown("down")
            time.sleep(x)
            pyautogui.keyUp("down")
            #pyautogui.press("down")
            #pyautogui.press("down")
            break



#### pula ave


        area = tela.getpixel((x, 503))
#172
        if area[0] == 83:
            pyautogui.press("up")
            #print("teste")
            break

        area = tela.getpixel((x, 503))
#172
        if area[0] == 172:
            pyautogui.press("up")
            #print("teste")
            break

    aux += 0.1