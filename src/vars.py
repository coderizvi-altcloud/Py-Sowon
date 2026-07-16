import time
from images import build_image_sets
import window_vars

position_offsets = {
    "h1": 0,
    "h2": 1,
    "c1": 2,
    "m1": 0,
    "m2": 1,
    "c2": 2,
    "s1": 0,
    "s2": 1,
}


#variables
start_time = time.time()
resize_job = None
refs       = {}
image_sets = build_image_sets(window_vars.FRAME_W, window_vars.FRAME_H)
