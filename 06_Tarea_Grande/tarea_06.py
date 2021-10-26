import numpy as np
import cv2
import matplotlib.pyplot as plt
from figureDetector import FigureDetector

def captureFrame():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while (True):
        # Capture the video frame by frame
        ret, frame = vid.read()
        # Display the resulting frame
        cv2.imshow('Captura tu figurita', frame)
        # the 'q' button is set as the quitting button you may use any desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return frame

def main():
    frame = captureFrame()
    fig, ax = plt.subplots(2,3)

    # Imagen original
    c = FigureDetector(frame)
    c.process_image()
    c.draw_contours()
    fg = c.whichFigure()

   
    ax[0, 0].imshow(c.img)
    ax[0, 1].imshow(c.img_gray, cmap='gray')
    ax[0, 2].imshow(c.img_eroded)
    ax[1, 0].imshow(c.img_contoured)
    ax[1, 1].imshow(c.img_text)
    ax[1, 2].imshow(c.img_text) #no se que otra figura mostrar:$

    """ OBS: Fsta función permite poder cerrar la venta apretando la tecla q """
    def close(event):
        if event.key == 'q':
            plt.close(event.canvas.figure)

    plt.gcf().canvas.mpl_connect("key_press_event", close)
    """ FIN OBS """

    # Esta linea es muy importante: es la que "abre" la ventana de los graficos
    plt.show()

    #Condicionales para mover el robot
    if fg == 3:
        print('Mover robot derecha')
        
    if fg == 4:
        print('Mover robot izquierda')
        
    if fg == 6:
        print('Mover robot arriba')

    if fg == 5:
        print('Mover robot abajo')

if __name__ == '__main__':
    main()
