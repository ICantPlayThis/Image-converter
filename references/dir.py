import os
def crop_line(line):
    for i in range(5):
        print(100 * i, 100 * line, 100 * i + 100, 100 * line + 100)

        print(":{}_{}_{}:".format(name, line + 1, i + 1))

name = "test"
extension = ".png"

#directory = os.getcwd()
#new_folder = os.path.join(directory, r'{}'.format(name))
#if not os.path.exists(new_folder):
#    os.makedirs(new_folder)
#print(new_folder)

#text_file = open("./{}/{}.txt".format(name), "w")
#text_file = open(os.path.join(new_folder, name + ".txt"), "w")

#if new_folder.is_file():
#    print("yes")

for i in range(5):
    crop_line(i)




