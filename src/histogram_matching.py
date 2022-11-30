# import packages
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms
import cv2
import argparse


def match_histogram(img_in, img_ref):
    # reading main image
    img1 = cv2.imread(img_in)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    # checking the number of channels
    print('No of Channel is: ' + str(img1.ndim))

    # reading reference image
    img2 = cv2.imread(img_ref)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    # checking the number of channels
    print('No of Channel is: ' + str(img2.ndim))

    image = img1
    reference = img2

    matched = match_histograms(image, reference, multichannel=True)
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 5))

    axes[0][0].set_axis_off()
    axes[0, 0].imshow(image)
    axes[0, 0].set_title('Original')
    axes[0][1].set_axis_off()
    axes[0, 1].imshow(reference)
    axes[0, 1].set_title('Referência')
    axes[0][2].set_axis_off()
    axes[0, 2].imshow(matched)
    axes[0, 2].set_title('Resultado')

    top = 85000
    axes[1, 0].hist(image.flatten(), 256, [0, 256], color = 'r')
    axes[1, 0].set_ylabel('Frequência')
    axes[1, 0].set_xlabel('Intensidade do pixel')
    axes[1, 0].set_ylim(bottom=0, top=top)

    axes[1, 1].hist(reference.flatten(), 256, [0, 256], color = 'r')
    axes[1, 1].set_ylabel('Frequência')
    axes[1, 1].set_xlabel('Intensidade do pixel')
    axes[1, 1].set_ylim(bottom=0, top=top)

    axes[1, 2].hist(matched.flatten(), 256, [0, 256], color = 'r')
    axes[1, 2].set_ylabel('Frequência')
    axes[1, 2].set_xlabel('Intensidade do pixel')
    axes[1, 2].set_ylim(bottom=0, top=top)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Exemplo:
    # $python histogram_matching.py -i ../images/cascais_over.jpg -r ../images/cascais_ref.png
    parser = argparse.ArgumentParser(description="Select image to read")
    parser.add_argument("-i", "--img", help="Input image file.", required=True)
    parser.add_argument("-r", "--ref", help="Reference image file.", required=True)
    args = parser.parse_args()
    match_histogram(args.img, args.ref)