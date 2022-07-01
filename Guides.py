import pyautogui
import time

#Best Shortcut keys:
#shift tab: will untab any area you want
#Middle mouse button/end button: will cancel program
#ctrl + enter: run program
#closest side mouse click: will duplicate line
#foreward most side mouse click/delete: will delete line
#alt a: move caret to front of line
#alt ;: move caret to back of line







# Give the python file some time before continuing (3 seconds)
time.sleep(3)

# Mouse Functions
print(pyautogui.size()) #Prints the resolution of your screen
# Prints the current position of the mouse
print(pyautogui.position())
# Moves the mouse over time (x location, y location, seconds (3))
pyautogui.moveTo(100, 100, 3)
# Move the mouse relative to its current position
pyautogui.moveRel(100, 100, 3)
# Click (x coordinate, y coordinate, amount of clicks, seconds of click holding)
pyautogui.click(500, 500, 3, 3, button="left")
# Alternative methods for above
#pyautogui.tripleClick()
#pyautogui.doubleClick()
#pyautogui.leftClick()
#pyautogui.rightClick()

# How to scroll (positive numbers will scroll up, negative numbers will scroll down)
for i in range(50):
    pyautogui.scroll(500)

# How to click your mouse and drag somewhere (mouse down=click, mouse up=release)
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
time.sleep(3)
pyautogui.mouseUp()

# Spiral drawing using pyautogui in painter (not finished)
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    pyautogui.dragRel(0, distance, 1, button-"left")
    pyauto.dragRel(-distance, 0, 1, button="left")

pyautogui.displayMousePosition()
# Below will loop things 10 times
for i in range(10): #for loops are used to replay a loop a specified amount of times

# Below will print mouse coordinates continually, and you can use the keyboard shortcut "alt + tab" to switch back and forth to record data
while True:
    print(pyautogui.position())

#Getting RGB values AND coordinates!
import pyautogui
import time

while 1:
    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    print(r,g,b,x,y)

    time.sleep(0.5)

#How to use loops and if statements + breaks
x = 11
print('opening')
while True: #how to make the loop go on an unspecified amount of times
    if x == 10: #must be == instead of just = for some reason
        print('x=10')
    else:
        print('worked')
        break #a break will stop any while, for, or nested loops once reached.

#How to get RGB values + coordinates using mouse:
import pillow
import pyautogui
pyautogui.displayMousePosition()
Press Ctrl-C to quit.
X:  739 Y:  205 RGB: (238, 237, 178)
X:  739 Y:  205 RGB: (238, 237, 178)
X: 1397 Y:  463 RGB: (120, 108,  56)
X: 1395 Y:  463 RGB: (125, 111,  59)
X: 1395 Y:  463 RGB: (125, 111,  59)
X: 1249 Y:  473 RGB: (173, 127,  29)
X:  470 Y:  378 RGB: (255, 255, 255)
X:  469 Y:  378 RGB: (255, 255, 255)
#Dofus bot fighting mechanism:
while True:
    if keyboard.is_pressed('down'): #canceling loop
        break
    if pyautogui.pixel(642, 946)[0] != 90:
        print('its working')
        pyautogui.click(900, 952, 1, 1) #magic arrow
        pyautogui.click(1841, 806, 1, 0.5) #enemy

    else:
        print('pass/not working')


#How to screenshot a region and save it to a specific folder
time.sleep(4)
iml = pyautogui.screenshot(region=(1400,780,700,50))
iml.save(r'C:\Users\micha\Coding\Dofus Bot Project\Region_Enemy_Screenshot.png')
print('it worked')

#How to fight hands free on Dofus
while True:
    pic = pyautogui.screenshot(region=(1400, 780, 700, 50))
    width, height = pic.size
    for x in range(0,width,20):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))
            if (b in range(147,157)):
                pyautogui.click(898, 942, 1, 1)
                time.sleep(0.6)
                pyautogui.click(x+1400,y+780)
                pyautogui.moveTo(1750,730,0.1)
                time.sleep(1)

                break

#How to see if a certain image is on the screen:
    if pyautogui.locateOnScreen('Dofus_Ready_Button.png'):
        print('found it')
    else:
        print('couldnt find)