"""
This snippet demonstrates how to create a simple scanner effect on the tree. A scanner is a moving
light that sweeps across the tree. The effect is achieved by setting the brightness of each LED
based on its distance from the scanner position.
"""

import math
from runshawtree import controller
import time


def scanner(tree, speed=1.0, color=(255, 0, 0)):
    """Move a scanner across the tree."""
    while True:
        for i in range(tree.num_leds):
            # Calculate the brightness based on the distance from the scanner position
            distance = abs(i - int(time.time() * speed) % tree.num_leds)
            brightness = max(0, 1 - distance / tree.num_leds)
            tree.set_pixel(i, (int(c * brightness) for c in color))
            tree.show()
            time.sleep(0.02)

        time.sleep(2)
        tree.clear()
        tree.show()


if __name__ == "__main__":
    tree = controller.Tree(debug=False, brightness=30)
    scanner(tree)
