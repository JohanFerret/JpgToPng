import os
from PIL import Image

def JpgToPng(dirIn, dirOut):
    if not os.path.exists(dirOut):
        os.mkdir(dirOut)

    li = os.listdir(dirIn)
    for name in li:
        img = Image.open(f"{dirIn}/{name}")
        name = os.path.splitext(name)[0]
        #print(name)
        img.save(f"{dirOut}/{name}.png")
