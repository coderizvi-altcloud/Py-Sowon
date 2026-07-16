from root import root

#frame calc
screen_w = root.winfo_width()
screen_h = root.winfo_height()

COLON_W = 85
FRAME_H = screen_h - 300
FRAME_W = (screen_w - 2 * COLON_W - 8 * 8) // 6