import time
from selecting_images import get_set,set_image
from resizing import *
from vars import position_offsets,start_time


running    = True
tick       = 0



#main
def counter():
    global tick

    seconds_passed = time.time() - start_time
    second  = int(seconds_passed % 60)
    hour    = int(seconds_passed // 3600)
    minutes = int((seconds_passed % 3600) // 60)

    if running:
        imgs, _     = get_set("h1",tick, position_offsets)
        set_image(hour_label1,   imgs[hour // 10],    "h1")

        imgs, _     = get_set("h2",tick, position_offsets)
        set_image(hour_label2,   imgs[hour % 10],     "h2")

        imgs, colon = get_set("c1",tick, position_offsets)
        set_image(isto_label,    colon,               "c1")

        imgs, _     = get_set("m1",tick, position_offsets)
        set_image(minute_label1, imgs[minutes // 10], "m1")

        imgs, _     = get_set("m2",tick, position_offsets)
        set_image(minute_label2, imgs[minutes % 10],  "m2")

        imgs, colon = get_set("c2",tick, position_offsets)
        set_image(isto2_label,   colon,               "c2")

        imgs, _     = get_set("s1",tick, position_offsets)
        set_image(second_label2, imgs[second // 10],  "s1")

        imgs, _     = get_set("s2",tick, position_offsets)
        set_image(second_label1, imgs[second % 10],   "s2")

        tick = (tick + 1) % 3
        root.after(100, counter)

#stop function
def press_stop(event=None):
    global running
    running = False

root.bind_all('s', press_stop)
counter()
root.mainloop()