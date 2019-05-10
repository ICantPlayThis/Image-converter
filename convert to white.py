# James Fletcher / Tempered-Kirin
# Python 3.7.2 /32
# V1.0 Covert all image files in a folder to white

from PIL import Image
import glob
import os
import shutil

# initialise variables
pixels = 16, 16
folder = "./textures/"
extension = "*.png"
files = []
white = Image.open("./white 16x16.png")

def convert_image(image):
    global folder
    global extension
   #img = Image.open(file)



# find images
for dir,_,_ in os.walk(folder):
    files.extend(glob.glob(os.path.join(dir, extension)))

#for file in files:
    #convert_image(file)

