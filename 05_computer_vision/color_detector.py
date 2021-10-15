import cv2
import numpy as np


class ColorDetector:

    def __init__(self, img):
        self.img = img

        # Inicializamos en cero todas las imagenes que guardaremos
        self.mask = np.zeros(img.shape)
        self.img_masked = np.zeros(img.shape)
        self.img_eroded = np.zeros(img.shape)
        self.img_dilated = np.zeros(img.shape)
        self.img_gray = np.zeros(img.shape)
        self.img_threshold = np.zeros(img.shape)
        self.img_contoured = np.zeros(img.shape)

    def process_image(self, lower_color, upper_color, kernel, threshold):
        self.mask_image(lower_color, upper_color)
        self.filter_image(kernel)
        self.draw_contours(threshold)

    def mask_image(self, lower_color, upper_color):
        img = np.copy(self.img)
        self.mask = cv2.inRange(img, lower_color, upper_color)
        self.img_masked = cv2.bitwise_and(img, img, mask=self.mask)

    def filter_image(self, kernel):
        # https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html
        img = self.img_masked
        self.img_eroded = cv2.erode(img, kernel)
        self.img_dilated = cv2.dilate(img, kernel)

    def draw_contours(self, threshold):
        """
        Para hacer esta función se deben seguir los siguientes pasos:
        1. convertir una imagen filtrada a escala de grises
        2. aplicar un umbral (threshhold). Se sugiere truncado: type=cv2.THRESH_TRUNC
        3. usar la funcion cv2.findContours:
            contours, hierarchy = cv2.finContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        4. copiar la imagen original
        5. usar cv2.drawContours(img, contours, -1, color=(0, 255,0), thickness=4)

        Para mas info, consultar
        https://learnopencv.com/contour-detection-using-opencv-python-c/
        """

        self.img_gray = cv2.cvtColor(self.img_eroded, cv2.COLOR_RGB2GRAY)

        ret, self.img_threshold = cv2.threshold(self.img_eroded, threshold, 255, cv2.THRESH_TRUNC)

        contours, hierarchy = cv2.findContours(self.img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        self.img_contoured = self.img.copy()
        cv2.drawContours(self.img_contoured, contours, -1, color=(0, 255, 0), thickness=4)

    def draw_bounding_boxes(self):
        """
        [Propuesto]
        1. Con el resultado de los contornos del metodo anterior,
        encontrar aquellos contornos cuya area encerrada sea superior a un
        numero arbitrario (por ej: 900 pixeles).

        2. Luego, iterar sobre cada grupo de contornos y usar las
        funciones cv2.boundingRect y cv2.rectangle:

         Mas o menos así
            for contour in contours:
                  x, y, w, h = cv2.boundingRect(contour)
                  cv2.rectangle(img, (x1, y1), (x2, y2), COLOR, line_width)

        Ojo que cv2.boundingRect entrega un origen (x, y) y el alto y ancho
        del rectangulo, pero cv2.rectangle toma dos esquinas opuestas como
        argumentos.

        """
