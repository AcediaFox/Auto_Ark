from autotool import auto_arknight
import os
import time
MENU = """
+------------------------------------+
|           Auto Game Menu           |
+------------------------------------+
|List of game:                       |
|1. Arknight                         |
|2. AzurLane                         |
|0. Exit                             |
+------------------------------------+
"""

while True:
    os.system('cls')
    print(MENU)
    Choice = input('Enter your Choice: ')
    if Choice == '0':
        os.system('cls')
        break
    elif Choice == '1':
        auto_arknight()
    elif Choice == '2':
        pass
    else:
        print('Please choice in [0-2]')
        time.sleep(2)
