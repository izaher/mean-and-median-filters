from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def mean_filter(image, filter_size):
    # create an empty array with same size as input image
    output = np.zeros(image.shape, np.uint8)

    # creat an empty variable
    result = 0

    for j in range(2, image.shape[0]-2):
        for i in range(2, image.shape[1]-2):
            for y in range(-2, 3):
                for x in range(-2, 3):
                    result = result + image[j+y, i+x]
            output[j][i] = int(result / filter_size**2)
            result = 0
    return output

def main():
    img = Image.open('image_1.png').convert('L')
    arr = np.array(img)
    mean_5 = mean_filter(arr, 5) 
    img = Image.fromarray(mean_5)
    plt.imshow(img, cmap='gray')

main()