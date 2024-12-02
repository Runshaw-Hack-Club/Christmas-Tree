"""
A very simple example that lights up each LED in turn with a red colour.
"""

from runshawtree import controller
import time

tree = controller.Tree(debug=False, brightness=30)


while True:
    for i in range(tree.num_leds):
        tree.set_pixel(i, (255, 0, 0))
        tree.show()
        time.sleep(0.1)

    tree.clear()
    tree.show()
