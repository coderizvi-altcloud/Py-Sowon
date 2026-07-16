import vars
from labels import hour_label1, hour_label2, isto_label, minute_label1, minute_label2, isto2_label, second_label1, second_label2
from frames import hour_frame1, hour_frame2, isto, minute_frame1, minute_frame2, isto2, second_frame1, second_frame2
from images import build_image_sets
from root import root
import window_vars


def on_resize(event):
    if event.widget != root:
        return
    if vars.resize_job:
        root.after_cancel(vars.resize_job)
    vars.resize_job = root.after(150, do_resize)


def do_resize():
    new_w = root.winfo_width()
    new_h = root.winfo_height()

    window_vars.FRAME_H = new_h - 300
    window_vars.FRAME_W = (new_w - 2 * window_vars.COLON_W - 8 * 8) // 6

    if window_vars.FRAME_W <= 0 or window_vars.FRAME_H <= 0:
        return

    for f in [hour_frame1, hour_frame2, minute_frame1, minute_frame2, second_frame1, second_frame2]:
        f.config(width=window_vars.FRAME_W, height=window_vars.FRAME_H)
    for f in [isto, isto2]:
        f.config(width=window_vars.COLON_W, height=window_vars.FRAME_H)

    hour_label1.place(  x=0, y=0, width=window_vars.FRAME_W, height=window_vars.FRAME_H)
    hour_label2.place(  x=0, y=0, width=window_vars.FRAME_W, height=window_vars.FRAME_H)
    isto_label.place(   x=0, y=0, width=window_vars.COLON_W, height=window_vars.FRAME_H)
    minute_label1.place(x=0, y=0, width=window_vars.FRAME_W, height=window_vars.FRAME_H)
    minute_label2.place(x=0, y=0, width=window_vars.FRAME_W, height=window_vars.FRAME_H)
    isto2_label.place(  x=0, y=0, width=window_vars.COLON_W, height=window_vars.FRAME_H)
    second_label1.place(x=0, y=0, width=window_vars.FRAME_W, height=window_vars.FRAME_H)
    second_label2.place(x=0, y=0, width=window_vars.FRAME_W, height=window_vars.FRAME_H)

    vars.image_sets = build_image_sets(window_vars.FRAME_W, window_vars.FRAME_H)


root.bind("<Configure>", on_resize)