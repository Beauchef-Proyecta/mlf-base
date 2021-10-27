import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime

class ShapeDetector:
    def __init__(self):
        self.img = None

    def update_image(self, img):
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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

        img = np.copy(self.img)
        self.img_gray= cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        self.filter_image()
        self.draw_contours()

    def filter_image(self, kernel=(15, 15)):
        img = np.copy(self.img_gray)
        self.img_gaus = cv2.GaussianBlur(img, kernel, 0)

        self.img_canny = cv2.Canny(self.img_gaus, 10, 150)
        self.img_dilated = cv2.dilate(self.img_canny, None, iterations=1)
        self.img_eroded = cv2.erode(self.img_dilated, None, iterations=1)
    
    def draw_contours(self):
        img = np.copy(self.img_eroded)
        img2 = np.copy(self.img)
        self.contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        el_mas_grande = max(self.contours, key=cv2.contourArea)
        self.img_contoured = cv2.drawContours(img2, el_mas_grande, 1, (0,255,0), 2)

        #print("Se detectan ", len(self.contours), " contornos")

    def whichFigure(self):
        #queria que sobre la figura con los contornos verdes pusiera los nombre pero no me resulta:(
        self.img_text = np.copy(self.img_contoured) 

        for c in self.contours:
            var = 0
            porc = 0.05 #a prueba y error
            epsilon = porc * cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            x,y,w,h = cv2.boundingRect(approx) #w y h son para diferenciar un rectangulo de un cuadrado

            # aqui hay que poner otro condicional por si detecta 2 figuras en la misma imagen, eso debe ser otra var
            if len(approx)==3:
                #cv2.putText(self.img_text,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
                var = 3
            if len(approx)==4:
                #cv2.putText(self.img_text,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
                var = 4
            if len(approx)==5:
                #cv2.putText(self.img_text,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
                var = 5
            if len(approx)==6:
                #cv2.putText(self.img_text,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
                var = 6
        #print(var)
        return var
