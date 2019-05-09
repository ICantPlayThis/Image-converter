# ICantPlayThis / Weeb Trash
# Python 3.6
# V1.0: Program to crop image into 5x5 squares each with a height and length of 100px - 30/03/2018
# V1.1: removed unused code
# V2.0: lists all images in folder that can be selected - 31/03/2018
# V2.1: fixed new folder
# V2.2: lists files by their index in the list
# V3.0: changeable folder and file name
# V4.0: makes text file with discord emote code
# V4.1: deletes name folder if exists to clear text file
# V4.2: crops image to center
# V4.3: opens images in image folder - 01/04/2018

# put script in folder with folder called "images"
# put images in images folder

from PIL import Image
import glob
import os
import shutil

# initialise variables
squares = 5
line = 1
extension = ".png"
files = []


def crop_line(line, squares, name, square_length):  # crop the image
    for i in range(squares):  # loop for every square in the line

        # algorithm that calculates x and y positions and saves each image in usable format
        cropped_square = square_length * i, square_length * line, square_length * i + square_length, square_length * line + square_length
        cropped_image.crop(cropped_square).save("./{}/{}_{}_{}{}".format(name, name, line + 1, i + 1, extension))
        text_file.write(":{}_{}_{}:".format(name, line + 1, i + 1))


# get list of files
images = glob.glob('./images/*.png') + glob.glob('./images/*.jpg')
for line in images:
    files.append(line[9:])

# display each line in list
for i, file in enumerate(files):
    print("{}: {}".format(i, file))

# ask user for file and name
number = int(input("which file would you like? please select the number: "))
name = input("What would you like the image to be called?: ")

file = files[number]
# name = ''.join(file.split())[:-4]
# extension = '.' + file.rsplit('.', 1)[1]

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
img = Image.open("./images/" + file)
#img.show()
size = min(img.size)  # shortest side of the image
square_length = size // squares  # length of the side of the square

width = img.size[0]  # x
height = img.size[1]  # y

# crop image to square and center
cropped_image = img.crop((width//2 - size//2, height//2 - size//2, width//2 + size//2, height//2 + size//2))

# run function for number of squares (default 5)
for i in range(squares):
    crop_line(i, squares, name, square_length)
    text_file.write("\n")
text_file.close()
