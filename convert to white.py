# James Fletcher / Tempered-Kirin
# Python 3.7.2 /32
# V1.0 Covert all image files in a folder to white

from PIL import Image
import glob
import os
import shutil

# initialise variables
pixels = 16
folder = "./textures/"
extension = "*.png"
files = []

def convert_image():
    return


# find images
for dir,_,_ in os.walk(folder):
    files.extend(glob.glob(os.path.join(dir, extension)))

for file in files:
    print(file)
#im = Image.open()
