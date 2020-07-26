
from PIL import Image
import matplotlib.pyplot as plt


def get_image_info(image):
    
    mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32,
                   "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24,
                   "I": 32, "F": 32, "I;16": 16, "I;16B": 16, "I;16L": 16,
                   "I;16S": 16, "I;16BS": 16, "I;16LS": 16, "I;32": 32,
                   "I;32B": 32, "I;32L": 32, "I;32S": 32, "I;32BS": 32, "I;32LS": 32}
    bpp = mode_to_bpp[image.mode]
    w, h = image.size
    print('Resolution: ',w,'x',h )
    print('Width: ', w)
    print('Height: ', h)
    print('Bit Depth: ', bpp)
    


def main():
    img = Image.open('image_1.png')
    get_image_info(img)
    plt.imshow(img)


main()