import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 23,13 64,170,242 #40AAF2

pixel = pyautogui.pixel(23, 13)
print(pixel)

# print(pyautogui.pixelMatchesColor(23, 13, (64,170,242)))
# print(pyautogui.pixelMatchesColor(23, 13, pixel))
print(pyautogui.pixelMatchesColor(23, 13, (64,170,243)))
