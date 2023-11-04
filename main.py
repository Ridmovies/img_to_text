import cv2
import pytesseract
import pyautogui
from pynput import mouse


x1, y1, x2, y2 = 0, 0, 0, 0
cnt = 0

# push mouse cursor
# def on_click(x, y, button, pressed):
#     global x1, y1, x2, y2
#     if pressed:
#         x1, y1 = pyautogui.position()
#     if not pressed:
#         x2, y2 = pyautogui.position()
#         return False


# Double click
def on_click(x, y, button, pressed):
    global x1, y1, x2, y2
    global cnt
    if pressed:
        cnt += 1
        if cnt == 1:
            x1, y1 = pyautogui.position()
        elif cnt == 2:
            x2, y2 = pyautogui.position()
            return False


# блок `with` слушает события до выхода
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# получаем скриншот экрана
screenshot = pyautogui.screenshot()

# # открываем скриншот в стандартном приложении для просмотра изображений
# screenshot.show()

# вырезаем нужную область из скриншота
cropped_image = screenshot.crop((x1, y1, x2, y2))

# сохраняем скриншот в файл
cropped_image.save('screenshot.png')

# path tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('screenshot.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, lang=('eng+rus'), config=config))

data = pytesseract.image_to_data(img, config=config)

cv2.imshow('Result', img)
cv2.waitKey(0)

