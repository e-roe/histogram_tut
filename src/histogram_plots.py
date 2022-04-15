import cv2
from matplotlib import pyplot as plt
import os

if __name__ == '__main__':
    examples = ['cascais_under.jpg', 'cascais.jpg', 'cascais_over.jpg']
    labels = ['Subexposição', 'Exposição normal', 'Superexposição']
    images = []
    for im in examples:
        read = cv2.imread(os.path.join('..', 'images', im))
        read = cv2.cvtColor(read, cv2.COLOR_BGR2RGB)
        images.append(read)

    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 5))

    for index in range(3):
        axes[0][index].set_axis_off()
        axes[0][index].imshow(images[index])
        axes[0][index].set_title(labels[index])
    for index in range(3):
        axes[1, index].hist(images[index].flatten(), 256, [0, 256], color ='r')
        axes[1, index].set_ylabel('Frequência')
        axes[1, index].set_xlabel('Intensidade do pixel')
        axes[1, index].set_ylim(bottom=0, top=170000)

    plt.tight_layout()
    plt.show()

