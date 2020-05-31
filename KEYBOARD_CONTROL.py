import pyautogui

# make sure to have an editor on your left side before you ran application
print(pyautogui.size())

# simulates pressing hot keys
pyautogui.hotkey('alt', 'tab')  # navigate to your editor

pyautogui.click(200, 200)
pyautogui.typewrite("hello world")

# passing lists on typewrite lets you use keyboard commands
myList = ['space', 'x', 'y', 'z', 'left', 'left', 'left', 'A', 'B', 'C']
pyautogui.typewrite(myList)

# simulates pressing 1 key only
pyautogui.press('f1')

# location of current mouse cursor
print(pyautogui.position())
pyautogui.moveTo(100, 100, duration=1.5)

pyautogui.click()
pyautogui.typewrite('moved mouse')
