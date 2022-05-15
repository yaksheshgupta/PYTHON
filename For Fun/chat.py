import keyboard as k
import pyautogui as p
import time as t
t.sleep(5)
for i in range(1,21):
    k.write("./adb shell input tap 130 1800")
    k.press_and_release("enter")
    t.sleep(1)
    k.write("./adb shell input tap 420 1800")
    k.press_and_release("enter")
    t.sleep(1)
    k.write("./adb shell input tap 920 1800")
    k.press_and_release("enter")
    t.sleep(1)
