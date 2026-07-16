from PIL import Image
from window_vars import FRAME_H,FRAME_W,COLON_W
#images
Images_1_raw = [Image.open(rf"E:\timer project\assests\first\{i}.png")    for i in range(10)]
colon_1_raw  =  Image.open(r"E:\timer project\assests\first\colon0.png")

Images_2_raw = [Image.open(rf"E:\timer project\assests\second\{i}.2.png") for i in range(10)]
colon_2_raw  =  Image.open(r"E:\timer project\assests\second\colon.2.png")

Images_3_raw = [Image.open(rf"E:\timer project\assests\third\{i}.3.png")  for i in range(10)]
colon_3_raw  =  Image.open(r"E:\timer project\assests\third\colon.3.png")

#images row and col
image_sets_raw = [
    (Images_1_raw, colon_1_raw),
    (Images_2_raw, colon_2_raw),
    (Images_3_raw, colon_3_raw),
]

#done by claude
def build_image_sets(fw, fh):
    return [
        (
            [img.resize((fw, fh), Image.LANCZOS) for img in raw_list],
            colon_raw.resize((COLON_W, fh), Image.LANCZOS)
        )
        for raw_list, colon_raw in image_sets_raw
    ]

image_sets = build_image_sets(FRAME_W, FRAME_H)