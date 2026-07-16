from frames import hour_frame1,hour_frame2,isto,minute_frame1,minute_frame2,isto2,second_frame1,second_frame2
import ttkbootstrap as tb
from window_vars import COLON_W,FRAME_W,FRAME_H

#labels
hour_label1   = tb.Label(hour_frame1,   background="black")
hour_label2   = tb.Label(hour_frame2,   background="black")
isto_label    = tb.Label(isto,          background="black")
minute_label1 = tb.Label(minute_frame1, background="black")
minute_label2 = tb.Label(minute_frame2, background="black")
isto2_label   = tb.Label(isto2,         background="black")
second_label1 = tb.Label(second_frame1, background="black")
second_label2 = tb.Label(second_frame2, background="black")
#labels setting
hour_label1.place(  x=0, y=0, width=FRAME_W, height=FRAME_H)
hour_label2.place(  x=0, y=0, width=FRAME_W, height=FRAME_H)
isto_label.place(   x=0, y=0, width=COLON_W, height=FRAME_H)
minute_label1.place(x=0, y=0, width=FRAME_W, height=FRAME_H)
minute_label2.place(x=0, y=0, width=FRAME_W, height=FRAME_H)
isto2_label.place(  x=0, y=0, width=COLON_W, height=FRAME_H)
second_label1.place(x=0, y=0, width=FRAME_W, height=FRAME_H)
second_label2.place(x=0, y=0, width=FRAME_W, height=FRAME_H)
