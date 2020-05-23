import numpy as np
import pyautogui

co = np.load(file="Coord1.npy")
# print(co)
c = np.load(file="ci.npy")
pyautogui.click((co[0], co[1]), c)

# pyautogui.press('Windows_logo_key')