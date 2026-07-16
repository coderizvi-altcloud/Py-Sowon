import time
import ttkbootstrap as tb
from PIL import Image, ImageTk

root = tb.Window(themename="darkly")
root.title("Tk Example")
root.state('zoomed')
root.update()

root.configure(background="black")
style = tb.Style()
style.configure("Black.TFrame", background="black")

screen_w = root.winfo_width()
screen_h = root.winfo_height()

COLON_W = 85
FRAME_H = screen_h - 300
FRAME_W = (screen_w - 2 * COLON_W - 8 * 8) // 6

# frames
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

# packing
second_frame1.pack(side="right", padx=4, pady=150, fill="both", expand=True)
second_frame2.pack(side="right", padx=4, pady=150, fill="both", expand=True)
isto2.pack(        side="right", padx=4, pady=150, fill="both", expand=True)
minute_frame1.pack(side="right", padx=4, pady=150, fill="both", expand=True)
minute_frame2.pack(side="right", padx=4, pady=150, fill="both", expand=True)
isto.pack(         side="right", padx=4, pady=150, fill="both", expand=True)
hour_frame1.pack(  side="right", padx=4, pady=150, fill="both", expand=True)
hour_frame2.pack(  side="right", padx=4, pady=150, fill="both", expand=True)

# labels
hour_label1   = tb.Label(hour_frame1,   background="black")
hour_label2   = tb.Label(hour_frame2,   background="black")
isto_label    = tb.Label(isto,          background="black")
minute_label1 = tb.Label(minute_frame1, background="black")
minute_label2 = tb.Label(minute_frame2, background="black")
isto2_label   = tb.Label(isto2,         background="black")
second_label1 = tb.Label(second_frame1, background="black")
second_label2 = tb.Label(second_frame2, background="black")

hour_label1.place(  x=0, y=0, width=FRAME_W, height=FRAME_H)
hour_label2.place(  x=0, y=0, width=FRAME_W, height=FRAME_H)
isto_label.place(   x=0, y=0, width=COLON_W, height=FRAME_H)
minute_label1.place(x=0, y=0, width=FRAME_W, height=FRAME_H)
minute_label2.place(x=0, y=0, width=FRAME_W, height=FRAME_H)
isto2_label.place(  x=0, y=0, width=COLON_W, height=FRAME_H)
second_label1.place(x=0, y=0, width=FRAME_W, height=FRAME_H)
second_label2.place(x=0, y=0, width=FRAME_W, height=FRAME_H)

# images
Images_1 = [
    Image.open(rf"E:\timer project\assests\first\{i}.png").resize((FRAME_W, FRAME_H), Image.LANCZOS)
    for i in range(10)
]
colon_1 = Image.open(r"E:\timer project\assests\first\colon0.png").resize((COLON_W, FRAME_H), Image.LANCZOS)

Images_2 = [
    Image.open(rf"E:\timer project\assests\second\{i}.2.png").resize((FRAME_W, FRAME_H), Image.LANCZOS)
    for i in range(10)
]
colon_2 = Image.open(r"E:\timer project\assests\second\colon.2.png").resize((COLON_W, FRAME_H), Image.LANCZOS)

Images_3 = [
    Image.open(rf"E:\timer project\assests\third\{i}.3.png").resize((FRAME_W, FRAME_H), Image.LANCZOS)
    for i in range(10)
]
colon_3 = Image.open(r"E:\timer project\assests\third\colon.3.png").resize((COLON_W, FRAME_H), Image.LANCZOS)

image_sets = [
    (Images_1, colon_1),
    (Images_2, colon_2),
    (Images_3, colon_3),
]

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

second    = 0
hour      = 0
minutes   = 0
tick      = 0
start_time = time.time()
running   = True

refs = {}

def set_image(label, img, key):
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    refs[key] = photo

def counter():
    global second, hour, minutes, tick

    seconds_passed = time.time() - start_time
    second  = int(seconds_passed % 60)
    hour    = int(seconds_passed // 3600)
    minutes = int((seconds_passed % 3600) // 60)

    if running:
        def get_set(key):
            idx = (tick + position_offsets[key]) % 3
            return image_sets[idx]

        imgs, _     = get_set("h1")
        set_image(hour_label1,   imgs[hour // 10],    "h1")

        imgs, _     = get_set("h2")
        set_image(hour_label2,   imgs[hour % 10],     "h2")

        imgs, colon = get_set("c1")
        set_image(isto_label,    colon,               "c1")

        imgs, _     = get_set("m1")
        set_image(minute_label1, imgs[minutes // 10], "m1")

        imgs, _     = get_set("m2")
        set_image(minute_label2, imgs[minutes % 10],  "m2")

        imgs, colon = get_set("c2")
        set_image(isto2_label,   colon,               "c2")

        imgs, _     = get_set("s1")
        set_image(second_label2, imgs[second // 10],  "s1")

        imgs, _     = get_set("s2")
        set_image(second_label1, imgs[second % 10],   "s2")

        tick = (tick + 1) % 3      #
        root.after(350, counter)


def press_stop(event=None):
    global running
    running = False

root.bind_all('s', press_stop)
counter()
root.mainloop()