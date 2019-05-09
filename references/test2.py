from imgpy import Img

squares = 7

with Img(fp='ninja.gif') as img:
    width = img.size[0]  # x
    height = img.size[1]  # y
    size = min(img.size)
    img.crop(box=(width//2 - size//2, height//2 - size//2, width//2 + size//2, height//2 + size//2))
    img.save(fp='crop.gif')

    #for i in range(squares):
     #   img.crop(box=(width // 2 - size // 2, height // 2 - size // 2, width // 2 + size // 2, height // 2 + size // 2))

    img.save(fp='baka.gif')