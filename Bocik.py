import pyautogui
import time

msg = input("Wpisz wiadomosc: ")
n = input("ile razy ?: ")

print("t minus")

count = 3
while(count != 0):
   print(count)
   time.sleep(1)
   count -= 1

print ()

for i in range(0,int(n)):
   pyautogui.typewrite(msg + '\n')
