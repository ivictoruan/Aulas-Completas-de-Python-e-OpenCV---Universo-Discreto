import numpy as np
import cv2


def showImage(img):
    from matplotlib import pyplot as plt
    obj_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    obj_img = cv2.imread("images\meme.png", 0)
    showImage(obj_img)

main()



