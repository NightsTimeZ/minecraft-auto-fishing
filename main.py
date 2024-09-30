from pynput import keyboard, mouse
from PIL import ImageGrab
import time

# Edit Ur Position Here
position = (1358, 812)
basecolor = (180, 162, 180) # 180, 162, 180 for Enchant | 160,160,160 for normal bet
running = True

def get_pixel_color(position):
    image = ImageGrab.grab(bbox=(position[0], position[1], position[0] + 1, position[1] + 1))
    return image.getpixel((0, 0))

def is_color_in_range(color, target=basecolor, tolerance=30):
    return all(target[i] - tolerance <= color[i] <= target[i] + tolerance for i in range(3))

def right_click():
    mouse_controller = mouse.Controller()
    mouse_controller.click(mouse.Button.right)

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        running = False
        return False
print("WAIT 5 SEC!") 
time.sleep(5)
print("START!")

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while running:
        color = get_pixel_color(position)
        if is_color_in_range(color):
            right_click()
            time.sleep(0.5)
        time.sleep(0.1)
finally:
    listener.stop()