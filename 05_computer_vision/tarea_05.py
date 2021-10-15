import numpy as np
import cv2
import matplotlib.pyplot as plt
from color_detector import ColorDetector


def main():
    img_path = 'images/arcoiris.jpg'
    img_bgr = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    fig, ax = plt.subplots(3,3)

    # Imagen original
    c = ColorDetector(img_rgb)
    ax[0, 0].imshow(c.img)

    # Calculamos la mascara y la aplicamos
    # deben encontrar limites adecuados para el color que les interese
    lower_color = np.array([0, 0, 0])
    upper_color = np.array([360, 255, 255])

    c.mask_image(lower_color, upper_color)
    ax[0, 1].imshow(c.mask, cmap='gray')
    ax[0, 2].imshow(c.img_masked)

    # Se aplican operaciones morfológicas para reducir el ruido
    kernel = np.ones((20, 20), np.uint8)  # deben encontrar un tamañ de kernel adecuado

    c.filter_image(kernel=kernel)
    ax[1, 0].imshow(c.img_eroded)
    ax[1, 1].imshow(c.img_dilated)

    # Busqueda de contornos;
    umbral = 50     # deben encontrar un valor adecuado
    c.draw_contours(threshold=umbral)
    ax[2, 0].imshow(c.img_gray, cmap='gray')
    ax[2, 1].imshow(c.img_threshold, cmap='gray')
    ax[2, 2].imshow(c.img_contoured)

    """ OBS: Fsta función permite poder cerrar la venta apretando la tecla q """
    def close(event):
        if event.key == 'q':
            plt.close(event.canvas.figure)

    plt.gcf().canvas.mpl_connect("key_press_event", close)
    """ FIN OBS """

    # Dejamos en blanco el subplot [1, 2]
    ax[1, 2].axis('off')
    # Esta linea es muy importante: es la que "abre" la ventana de los graficos
    plt.show()


if __name__ == '__main__':
    main()
