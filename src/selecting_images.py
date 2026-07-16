from PIL import ImageTk
import vars
from vars import refs, position_offsets


def set_image(label, img, key):
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    refs[key] = photo

def get_set(key, tick, position_offsets):
    idx = (tick + position_offsets[key]) % 3
    return vars.image_sets[idx]  # ← always live value