import cv2
from matplotlib import pyplot as plt
import argparse


def equalise(img_in):
    img = cv2.imread(img_in)

    img_in = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(img)

    equ_out = cv2.cvtColor(equ, cv2.COLOR_GRAY2RGB)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 7))

    axes[0][0].set_axis_off()
    axes[0, 0].imshow(img_in)
    axes[0, 0].set_title('Baixo contraste')
    axes[0][1].set_axis_off()

    axes[0, 1].imshow(equ_out)
    axes[0, 1].set_title('Equalizada')

    axes[1, 0].hist(img.flatten(), 256, [0, 256], color = 'r')
    axes[1, 0].set_ylabel('Frequência')
    axes[1, 0].set_xlabel('Intensidade do pixel')

    axes[1, 1].hist(equ.flatten(), 256, [0, 256], color = 'r')
    axes[1, 1].set_ylabel('Frequência')
    axes[1, 1].set_xlabel('Intensidade do pixel')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Exemplo:
    # $python histogram_equalization.py -i ../images/salt_low.jpg
    parser = argparse.ArgumentParser(description="Select image to read")
    parser.add_argument("-i", "--img", help="Input image file.", required=True)
    args = parser.parse_args()
    equalise(args.img)