# James Fletcher / Tempered-Kirin / ICantPlayThis
# Python 3.7.2 /32
# V1.0 Covert all image files in a folder to white
# V1.1 14/05/19
from PIL import Image
import glob
import os
import shutil

# initialise variables
folder = "./textures/"
newfolder = "./converted/"
new_folder = "/white/"
extension = "*.png"
files = []
images = []


def convert_image(im):
    alpha = im.split()[-1]
    white = Image.new(im.mode, im.size, (255, 255, 255, 0))
    white.putalpha(alpha)
    return white

# find images
for dir, _, _ in os.walk(folder):
    images.extend(glob.glob(os.path.join(dir, extension)))

# remove root directory filepath from images
for image in images:
    files.append(image[(len(folder)):])
    print(image[(len(folder)):])

# open image
for file in files:
    print(file)
    im = Image.open(folder + file).convert("RGBA") # open image as rgba (tuple)
    pixels = im.load()

    im = convert_image(im)

    # make directory and save
    os.makedirs(os.path.dirname(newfolder + file),exist_ok=True)
    im.save(newfolder + file)

print("done!")
