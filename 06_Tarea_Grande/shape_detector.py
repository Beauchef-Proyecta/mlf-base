import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime

class ShapeDetector:
    def __init__(self):
        self.img = None

    def update_image(self, img):
        # Se actualiza la imagen para procesar; se reduce su dimensión, se pasa al espacio RGB y se refleja verticalmente
        self.img = cv2.resize(img, (360, 640))
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.img = cv2.flip(self.img, 2)

        # Se reinician las matrices auxiliares
        self.img_filtered = np.zeros(img.shape)
        self.img_gray = np.zeros(img.shape)
        self.img_gaus = np.zeros(img.shape)
        self.img_contoured = np.zeros(img.shape)
        self.img_text = np.zeros(img.shape)
        self.contours = 0 #guarda los datos de los contornos

    def process_image(self):
        if self.img is None:
            raise AttributeError("ShapeDetector: 'No tengo una imagen para trabajar:c'" )

        # Convertir a escala de grises
        self.img_gray= cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)

        # Filtrar con un Blur Gaussiano
        kernel = (15,15)
        self.img_gaus = cv2.GaussianBlur(self.img_gray, kernel, 0)

        # Aplicar filtro Canny para detección de bordes
        self.img_canny = cv2.Canny(self.img_gaus, 50, 150)
        
        # Suavizar la imagen con erode y dilate
        self.img_filtered = cv2.dilate(self.img_canny, None, iterations=1)
        self.img_filtered = cv2.erode(self.img_filtered, None, iterations=1)

        # Encontrar contornos
        contours, _ = cv2.findContours(self.img_filtered, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filtrar los contornos obtenidos para quedarse sólo con aquellos cuya área sea suficientemente grande (>10.000px)
        relevant_contours = []
        for c in contours:
            if cv2.contourArea(c) > 10000:
                relevant_contours.append(c)
        self.contours = relevant_contours
    
        self.img_contoured = cv2.drawContours(self.img, self.contours, -1, (0,255,0), 2)

        print("Se ha(n) detectado ", len(self.contours), " contorno(s)")

    def whichShape(self):
        if not self.contours:
            # Si no se detectaron contornos relevantes, no se hace nada (sólo se retorna)
            return
        
        for c in self.contours:
            shape_size = 0

            # Calcular la cantidad de lados de la forma
            """ En esta sección se recomienda consultar el sitio https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/ """
            porc = 0.05
            epsilon = porc * cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            shape_size = len(approx)

            # Dibujar bounding box del contorno y agregar texto que lo describe
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(self.img, (x,y), (x+w,y+h), color=(0,255,0), thickness=5)
            cv2.putText(self.img,'Contorno - '+str(shape_size), (x,y-5),5,2,(0,0,0),thickness = 5)

        return shape_size
