import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
from mpl_toolkits.mplot3d import Axes3D
from color_detector import ColorDetector
from plotter import Plotter

def main():
    img_path = 'images/arcoiris.jpg'
    img_bgr = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    fig, ax = plt.subplots(3,3)

    # Imagen original
    c = ColorDetector(img_rgb)
    ax[0, 0].imshow(c.img)

    # Calculamos la mascara y la aplicamos
    lower_color = np.array([100, 0, 0])
    upper_color = np.array([200, 255, 255])
    c.mask_image(lower_color, upper_color)
    ax[0, 1].imshow(c.mask, cmap='gray')
    ax[0, 2].imshow(c.masked_img)

    # Se aplican operaciones morfológicas para reducir el ruido
    kernel = np.ones((10, 10), np.uint8)
    c.filter_image(kernel)
    ax[1, 0].imshow(c.eroded_img)
    ax[1, 1].imshow(c.eroded_img)

    # Busqueda de contornos
    c.find_contours()
    ax[2, 0].imshow(c.grayscale_img, cmap='gray')
    ax[2, 1].imshow(c.thresh_img, cmap='gray')

    ax[2, 2].imshow(c.contoured_img)






    # Aplicar operaciones morfológicas para eliminar ruido
    # Esto corresponde a hacer un Opening
    # https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html
    # Operacion morfologica erode

    # Operacion morfologica dilate

    # Busca contornos de blobs
    # https://docs.opencv.org/trunk/d3/d05/tutorial_py_table_of_contents_contours.html
    """
    # Iterar sobre contornos y dibujar bounding box de los patos
    for cnt in contours:
        # Obtener rectangulo que bordea un contorno

        # Filtrar por area minima
        if AREA > min_area:  # DEFINIR AREA
    # Dibujar rectangulo en el frame original

    # Se muestra en una ventana llamada "patos" la observación del simulador
    # con los bounding boxes dibujados
    cv2.imshow('patos', cv2.cvtColor(obs, cv2.COLOR_RGB2BGR))
    # Se muestra en una ventana llamada "filtrado" la imagen filtrada
    cv2.imshow('filtrado', image)

    """
    def close(event):
        if event.key == 'q':
            plt.close(event.canvas.figure)

    cid = plt.gcf().canvas.mpl_connect("key_press_event", close)

    plt.show()


if __name__ == '__main__':
    main()