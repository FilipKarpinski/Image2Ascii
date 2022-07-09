import numpy as np
import pandas as pd
import cv2 as cv
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

IMAGE_NAME = '1.jpg'
SLICING_SIZE = {
    'low': (10, 30),
    'medium': (5, 15),
    'high': (2, 6),
}
FILENAME = f"{dir_path}/output/{IMAGE_NAME.split('.')[0]}.txt"
IMAGE_SIZE = {
    'low': (1000, 100),
    'medium': (1500, 150),
    'high': (2000, 200),
}
ASCII_MAP = {
    ' ': [255, 220],
    '.': [219, 200],    
    ',': [199, 160],                
    ';': [159, 130],
    'o': [129, 100], 
    'x': [99, 70],
    '%': [69, 40],
    '#': [39, 20],
    '@': [19, 0],
}
INVERT = False

def convert(file_bytes, quality, invert):
    quality_width = SLICING_SIZE[quality][0]
    quality_height = SLICING_SIZE[quality][1]
    nparr = np.fromstring(file_bytes, np.uint8)
    image = cv.imdecode(nparr, cv.IMREAD_GRAYSCALE)
    if invert:
        image = cv.bitwise_not(image)

    images_mean = []
    character = ''
    for i in range(0, image.shape[0], quality_height):
        for j in range(0, image.shape[1], quality_width):
            img_part = image[i: i+quality_height, j: j+quality_width]
            intesity_mean = cv.mean(img_part)[0]
            for key, value in ASCII_MAP.items():
                if intesity_mean >= value[1] and intesity_mean <= value[0]:
                    character = key
                    break
            images_mean.append(character)
        images_mean.append('\n')

    text = ''.join(map(str, images_mean))
    
    # with open(FILENAME, 'w+') as file:
    #     file.write(text)

    return text


if __name__ == '__main__':
    convert()    