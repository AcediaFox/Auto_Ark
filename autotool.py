import pyautogui
import time

IMAGE_PIC = [
    'pic/start_pic.png',
    'pic/MsStart_pic.png',
    'pic/end_pic.png',
    'pic/restorePotions_pic.png',
    'pic/restoreOriginite_pic.png'
]
MESSAGE_PROCESS = 'IN PROCESS!'


def click_pic(img):
    x, y = pyautogui.center(img)
    pyautogui.moveTo(x, y, 0.75)
    pyautogui.click()


def auto_arknight():
    print('Press Ctrl-C to quit.')
    check = True
    while check:
        try:
            print(MESSAGE_PROCESS, end='')
            print('\b' * len(MESSAGE_PROCESS), end='', flush=True)
            for idx, val in enumerate(IMAGE_PIC):
                img = pyautogui.locateOnScreen(val, confidence=0.7)
                if img:
                    if idx == 3 or idx == 4:
                        check = False
                        img = pyautogui.locateOnScreen(
                            'pic/cancel_pic.png', confidence=0.8)
                        click_pic(img)
                        break
                    print('Move in step {} !'.format(idx+1))
                    click_pic(img)
                    time.sleep(3)
                    break
        except Exception as e:
            print(e)


# auto_arknight()
# img = pyautogui.locateOnScreen('pic/MsStart_pic.png', confidence=0.7)
# print(img)