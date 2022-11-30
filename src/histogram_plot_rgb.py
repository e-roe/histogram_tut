import cv2
from skimage import io
import matplotlib.pyplot as plt
import argparse
import numpy as np


def plot_histogram(file):
    image = io.imread(file)
    fig = plt.figure()
    plt.hist(image.ravel(), bins = 256, color = 'grey')
    plt.hist(image[:, :, 0].ravel(), bins=256, color='Red', alpha=0.5)
    plt.hist(image[:, :, 1].ravel(), bins=256, color='Green', alpha=0.5)
    plt.hist(image[:, :, 2].ravel(), bins=256, color='Blue', alpha=0.5)
    plt.xlabel('Intensidade')
    plt.ylabel('Frequência')
    plt.legend(['Total (3 canais somados)', 'Canal Vermelho', 'Canal Verde', 'Canal Azul'])

    fig.canvas.draw()
    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    factor = image.shape[0] / 480
    if image.shape[0] > 480:
        factor = 1 / factor

    image = cv2.resize(image, (int(image.shape[1] * factor), 480))
    concat = np.concatenate((image, data), axis=1)
    cv2.imshow('Image Histogram', cv2.cvtColor(concat, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)


if __name__ == '__main__':
    # Exemplo:
    # $python histogram_plot_rgb.py -i ../images/cascais_ref.png
    parser = argparse.ArgumentParser(description="Select image to read")
    parser.add_argument("-i", "--img", help="Input image file.", required=True)
    args = parser.parse_args()
    plot_histogram(args.img)