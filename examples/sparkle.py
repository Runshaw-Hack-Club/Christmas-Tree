"""
This snippet demonstrates how to create a simple sparkle effect on the tree. Sparkles are randomly
added to the tree and fade in and out gently. The effect is achieved by blending between the
background color and the sparkle color over time.
"""

import math
from runshawtree import controller
import time
import random


def sparkle(
    tree,
    sparkle_color=(255, 50, 0),
    background_color=(0, 0, 0),
    sparkle_probability=0.1,
    fade_steps=50,
    fade_duration=1.0,
):
    """Gently fade sparkles in and out on the tree."""
    led_states = [background_color] * tree.num_leds
    led_fade_progress = [0.0] * tree.num_leds  # Tracks fade progress (0.0 to 1.0)

    def blend(color1, color2, t):
        """Blend between two colors based on t (0.0 to 1.0)."""
        return tuple(int(c1 * (1 - t) + c2 * t) for c1, c2 in zip(color1, color2))

    while True:
        for y in range(tree.num_leds):
            if (
                random.random() < sparkle_probability
                and led_states[y] == background_color
            ):
                led_states[y] = sparkle_color
                led_fade_progress[y] = 0.0  # Start new sparkle

        for y in range(tree.num_leds):
            if led_states[y] == sparkle_color:
                led_fade_progress[y] += 1.0 / fade_steps
                if led_fade_progress[y] >= 1.0:  # Fully faded in, start fading out
                    led_states[y] = background_color
                    led_fade_progress[y] = 0.0
                t = min(led_fade_progress[y], 1.0)
                tree.set_pixel(y, blend(background_color, sparkle_color, t))
            else:
                tree.set_pixel(y, background_color)
        tree.show()
        time.sleep(fade_duration / fade_steps)


if __name__ == "__main__":
    tree = controller.Tree(debug=False, num_leds=200, brightness=30)
    sparkle(tree)
