#/usr/bin/env python3
# An example script from the i3-py package available via pip3
# Requires the i3-py package to be installed
# Source found here: https://github.com/ziberna/i3-py/blob/master/examples/cycle.py

# A good starting point for an alt-tab like behavior?

import i3
import time

def cycle():
    # get currently focused windows
    current = i3.filter(nodes=[], focused=True)
    # get unfocused windows
    other = i3.filter(nodes=[], focused=False)
    # focus each previously unfocused window for 0.5 seconds
    for window in other:
        i3.focus(con_id=window['id'])
        time.sleep(0.5)
    # focus the original windows
    for window in current:
        i3.focus(con_id=window['id'])

if __name__ == '__main__':
    cycle()
