import time
from pyautogui import hotkey, moveTo, click, press, typewrite, screenshot

print("""\nMake sure the last windows you've selected before the one in which you run this python script, is the minecraft window!""")

RANGE = 2
MULTIPLIER = 200
HEIGHT = 120

# go and unlock minecraft window
hotkey('alt', 'tab')
moveTo(981, 336)
click()

def enter_cmd(cmd):
    press('/')
    typewrite(cmd)
    press('enter')

enter_cmd('gamemode 1')
# time.sleep(1)

enter_cmd('time set 0')

for x in range(-RANGE, RANGE):
    for y in range(-RANGE, RANGE):
        xCo, yCo = x*MULTIPLIER, y*MULTIPLIER
        enter_cmd('tp {} {} {}'.format(xCo, HEIGHT, yCo))
        
        time.sleep(3)
        screenshot('./snapshots/{},{}.png'.format(xCo, yCo))

enter_cmd('FINISHED!')

