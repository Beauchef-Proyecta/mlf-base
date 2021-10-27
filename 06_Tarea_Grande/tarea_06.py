import numpy as np
import cv2
import matplotlib.pyplot as plt
from shape_detector import ShapeDetector
from plotter import Plotter




def main():

    vid = cv2.VideoCapture(2)
    plotter = Plotter()

    while plotter.is_enabled:
    # Capturar imagen
        ret, frame = vid.read()

        # Procesar
        c = ShapeDetector(frame)
        c.process_image()
        c.draw_contours()
        fg = c.whichFigure()

        # Decidir
        #Condicionales para mover el robot
        if fg == 3:
            print('Mover robot derecha')
            
        if fg == 4:
            print('Mover robot izquierda')
            
        if fg == 6:
            print('Mover robot arriba')

        if fg == 5:
            print('Mover robot abajo')

        # Actuar

        # Mostrar resultado
        plotter.update([c.img, c.img_contoured])
    

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
