# ICantPlayThis / Weeb Trash
# Python 3.6
# V1.0: Program to crop gifs into 5x5 squares - 01/04/2018

from PIL import Image
import glob
import os
import shutil
from imgpy import Img

# initialise variables
squares = 5
line = 1
extension = ".gif"

def crop_line(line, squares, name, square_length): # crop the image
    for i in range(squares):  # loop for every square in the line

        # algorithm that calculates x and y positions and saves each image in usable format
        cropped_square = square_length * i, square_length * line, square_length * i + square_length, square_length * line + square_length

        cropped_image.crop(cropped_square).save("./{}/{}_{}_{}{}".format(name, name, line + 1, i + 1, extension))
        text_file.write(":{}_{}_{}:".format(name, line + 1, i + 1))


# Get list of files
files = glob.glob('./gifs/*.gif')

#Display each line in list
for i, file in enumerate(files):
    print("{}: {}".format(i, file))


number = int(input("which file would you like? please select the number: "))
name = input("What would you like the image to be called?: ")

file = files[number]
#name = ''.join(file.split())[:-4]
#extension = '.' + file.rsplit('.', 1)[1]
print(name)
print(extension)

# create path
directory = os.getcwd()
new_folder = os.path.join(directory, r'{}'.format(name))

# delete folder if it exists
if os.path.exists(new_folder):
    shutil.rmtree(new_folder)

os.makedirs(new_folder)

# make text file
text_file = open(os.path.join(new_folder, name + ".txt"), "a")

# Read image
img = Image.open(file)
size = min(img.size) # shortest side of the image
square_length = size // squares # length of the side of the square

width = img.size[0] # x
height = img.size[1] # y

# crop image to square and center
cropped_image = img.crop((width//2 - size//2, height//2 - size//2, width//2 + size//2, height//2 + size//2))

# run function for number of squares (default 5)
for i in range(squares):
    crop_line(i, squares, name, square_length)
    text_file.write("\n")
text_file.close()
