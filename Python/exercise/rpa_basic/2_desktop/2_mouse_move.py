import pyautogui

# 절대좌표로 마우스 이동
# pyautogui.moveTo(200, 100) # 지정한 위치로 마우스를 이동
# pyautogui.moveTo(100, 200, duration=5) # 0.25초 동안 지정 위치로 이동

# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 100, duration=0.25)
# pyautogui.moveTo(300, 100, duration=0.25)

# 상대좌표로 이동
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)
