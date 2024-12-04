import math
from runshawtree import controller
import time


class ColorUtils:
    # This looks complicated, but it's just a direct translation of the HSV to RGB algorithm
    # See https://en.wikipedia.org/wiki/HSL_and_HSV#From_HSV for more details
    # HSV stands for Hue, Saturation, Value (or Brightness), and is a common way to represent colors
    @staticmethod
    def hsv_to_rgb(h, s, v):
        h = float(h)
        s = float(s)
        v = float(v)
        h60 = h / 60.0
        h60f = math.floor(h60)
        hi = int(h60f) % 6
        f = h60 - h60f
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        r, g, b = 0, 0, 0
        if hi == 0:
            r, g, b = v, t, p
        elif hi == 1:
            r, g, b = q, v, p
        elif hi == 2:
            r, g, b = p, v, t
        elif hi == 3:
            r, g, b = p, q, v
        elif hi == 4:
            r, g, b = t, p, v
        elif hi == 5:
            r, g, b = v, p, q
        return int(r * 255), int(g * 255), int(b * 255)


tree = controller.Tree(debug=False, brightness=30)
num_leds = 200
t = 0

while True:
    for i in range(num_leds):
        # Create a wave pattern using a sine function
        wave = math.sin((i / num_leds * 4 * math.pi) - (t * 0.1))
        brightness = (wave + 1) / 2  # Normalize to range [0, 1]
        # Generate a color using HSV (hue varies, saturation and value are fixed)
        hue = (t + i * 360 / num_leds) % 360  # Circular hue
        color = ColorUtils.hsv_to_rgb(hue, 1.0, brightness)
        # Set the pixel color
        tree.set_pixel(i, color)
    tree.show()
    # Increment time for animation
    t += 1
    # Delay for that ⭐smooth⭐ frame rate!
    time.sleep(0.02)
