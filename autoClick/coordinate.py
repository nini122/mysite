import os

import numpy as np
from pynput import mouse

npPath = "C:/Users/mhyon/PycharmProjects/myweb/venv/mysite/autoClick"
npName = os.path.join(npPath, "coord1.npy")

# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    c = np.array([x, y])
    np.save(npName, arr=c)

    if not pressed:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


# Collect events until released
with mouse.Listener(
        # on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    # on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
