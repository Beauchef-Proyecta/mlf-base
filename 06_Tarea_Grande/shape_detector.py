import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime

class ShapeDetector:
    def __init__(self):
        self.img = None

    def update_image(self, img):
        self.img = cv2.resize(img, (480, 640))
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.img = cv2.flip(self.img, 2)
        self.img_eroded = np.zeros(img.shape)
        self.img_dilated = np.zeros(img.shape)
        self.img_gray = np.zeros(img.shape)
        self.img_gaus = np.zeros(img.shape)
        self.img_contoured = np.zeros(img.shape)
        self.img_text = np.zeros(img.shape)
        self.contours = 0 #guarda los datos de los contornos

    #puse muchos copy, tal vez alguno esta de mas
    def process_image(self):
        if self.img is None:
            raise AttributeError("ShapeDetector 'No tengo una imagen para trabajar:c'" )

        self.img_gray= cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        self.filter_image()
        self.find_relevant_contours()

    def filter_image(self, kernel=(15, 15)):
        img = np.copy(self.img_gray)
        self.img_gaus = cv2.GaussianBlur(img, kernel, 0)

        self.img_canny = cv2.Canny(self.img_gaus, 50, 150)
        self.img_dilated = cv2.dilate(self.img_canny, None, iterations=1)
        self.img_eroded = cv2.erode(self.img_dilated, None, iterations=1)
    
    def find_relevant_contours(self):
        img = np.copy(self.img_eroded)
        img2 = np.copy(self.img)
        self.contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # filter contours by area greater than 400
        filtered = []
        for c in self.contours:
            if cv2.contourArea(c) > 10000:
                filtered.append(c)
        self.contours = filtered
    
        self.img_contoured = cv2.drawContours(img2, self.contours, -1, (0,255,0), 2)

        print("Se detectan ", len(self.contours), " contornos")

    def whichFigure(self):
        if not self.contours:
            print("No pude detectar ningún contorno :c")
            return
        
        for c in self.contours:
            var = 0
            porc = 0.05 #a prueba y error
            epsilon = porc * cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            x,y,w,h = cv2.boundingRect(approx) #w y h son para diferenciar un rectangulo de un cuadrado
            cv2.rectangle(self.img, (x,y), (x+w,y+h), color=(0,255,0), thickness=5)

            # aqui hay que poner otro condicional por si detecta 2 figuras en la misma imagen, eso debe ser otra var
            var =  len(approx)
            cv2.putText(self.img,'Contorno - '+str(var), (x,y-5),5,2,(0,0,0),thickness = 5)
        print(var)
        return str(var)
