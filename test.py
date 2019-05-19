# James Fletcher / Tempered-Kirin / ICantPlayThis
# Python 3.7.2 /32

from PIL import Image
import glob
import os

# initialise variables
folder = ".\\textures\\"
new_folder = ".\\converted\\"
extension = "*.png"
files = []
images = []
blacklist = ['font', 'gui', 'map', 'effect', 'misc']

def convert_image(image):
    alpha = image.split()[-1] # split image into alpha only
    white = Image.new(image.mode, image.size, (255, 255, 255, 0)) # make a pure white image
    white.putalpha(alpha) # put the alpha from the image into the blank white image
    return white


# find images in folder
for dir, _, _ in os.walk(folder):
    images.extend(glob.glob(os.path.join(dir, extension)))

# remove root directory from string
for image in images:
    files.append(image[(len(folder)):])

# remove blacklisted folders
for i in files[:]:
    for image in blacklist:
        if image in i:
            files.remove(i)
print(files)
print("done!")
