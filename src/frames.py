from root import root, style
import ttkbootstrap as tb
from window_vars import FRAME_H,FRAME_W,COLON_W

#frames
hour_frame1   = tb.Frame(root, width=FRAME_W, height=FRAME_H, style="Black.TFrame")
hour_frame2   = tb.Frame(root, width=FRAME_W, height=FRAME_H, style="Black.TFrame")
isto          = tb.Frame(root, width=COLON_W, height=FRAME_H, style="Black.TFrame")
minute_frame1 = tb.Frame(root, width=FRAME_W, height=FRAME_H, style="Black.TFrame")
minute_frame2 = tb.Frame(root, width=FRAME_W, height=FRAME_H, style="Black.TFrame")
isto2         = tb.Frame(root, width=COLON_W, height=FRAME_H, style="Black.TFrame")
second_frame1 = tb.Frame(root, width=FRAME_W, height=FRAME_H, style="Black.TFrame")
second_frame2 = tb.Frame(root, width=FRAME_W, height=FRAME_H, style="Black.TFrame")

for f in [hour_frame1, hour_frame2, isto, minute_frame1, minute_frame2, isto2, second_frame1, second_frame2]:
    f.pack_propagate(False)
#frame settings
second_frame1.pack(side="right", padx=4, pady=150, fill="both", expand=True)
second_frame2.pack(side="right", padx=4, pady=150, fill="both", expand=True)
isto2.pack(        side="right", padx=4, pady=150, fill="both", expand=True)
minute_frame1.pack(side="right", padx=4, pady=150, fill="both", expand=True)
minute_frame2.pack(side="right", padx=4, pady=150, fill="both", expand=True)
isto.pack(         side="right", padx=4, pady=150, fill="both", expand=True)
hour_frame1.pack(  side="right", padx=4, pady=150, fill="both", expand=True)
hour_frame2.pack(  side="right", padx=4, pady=150, fill="both", expand=True)