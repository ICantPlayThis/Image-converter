# James Fletcher / Tempered-Kirin / ICantPlayThis
# Python 3.7.2 /32
# V1.0 Covert all image files in a folder to white 13/05/19
# V1.1 Fixed filepath 14/05/19
# V1.2 Cleaned up code and added comments 19/05/19
# V1.3 Added blacklist filter 19/05/19
from PIL import Image
import glob
import os

# initialise variables
folder = "./textures/"
new_folder = "./converted/"
extension = "*.png"
files = []
images = []
blacklist = ['font', 'gui', 'effect', 'misc']

def convert_image(image):
    if image.size[0] == image.size[1]: # if the width equals the heigth
        alpha = image.split()[-1] # split image into alpha only
        white = Image.new(image.mode, image.size, (255, 255, 255, 0)) # make a pure white image
        white.putalpha(alpha) # put the alpha from the image into the blank white image
        return white
    else:
        pass


# find images in folder
for dir, _, _ in os.walk(folder):
    images.extend(glob.glob(os.path.join(dir, extension)))

# remove root directory from string
for image in images:
    files.append(image[(len(folder)):])

# remove blacklisted images
for i in files[:]: # : in square bracket makes a copy of the list
    for image in blacklist:
        if image in i:
            files.remove(i)


# open image
for file in files:
    print(file)
    im = Image.open(folder + file).convert("RGBA") # open image as rgba (tuple)

    # convert image to white
    im = convert_image(im)

    # make directory and save
    os.makedirs(os.path.dirname(new_folder + file), exist_ok=True)
    if im:
        im.save(new_folder + file)

print("done!")
