import pyautogui
import time
from PIL import ImageGrab

time.sleep(15)

count = 1

for i in range(75):
    pyautogui.press('down')
    time.sleep(2)
    screenshot = ImageGrab.grab()
    screenshot.save(f'/home/vaibhav/Desktop/stock/image{str(count)}.jpg')
    count+=1
    pyautogui.click(x=1279, y=22)
    time.sleep(3)
    
# print(pyautogui.KEYBOARD_KEYS)