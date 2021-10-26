import cv2
import numpy as np
import matplotlib.pyplot as plt

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

class figureDetector:
    def __init__(self, img):
        self.img = img
        self.img_eroded = np.zeros(img.shape)
        self.img_dilated = np.zeros(img.shape)
        self.img_gray = np.zeros(img.shape)
        self.img_gaus = np.zeros(img.shape)
        self.img_contoured = np.zeros(img.shape)
        

    def process_image(self, kernel, threshold):
        self.img_gray= cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.filter_image(kernel)
        self.draw_contours()

    def filter_image(self, kernel=5):
        self.img_gaus = cv2.GaussianBlur(self.img_gray, (kernel, kernel), 0)

        self.img_canny = cv2.Canny(self.img_gaus, 10, 150)
        self.img_dilated = cv2.dilate(self.img_canny, None, iterations=1)
        self.img_eroded = cv2.erode(self.img_dilated, None, iterations=1)
    
    def draw_contours(self):
        cnts, _ = cv2.findContours(self.img_eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.img_contoured = cv2.drawContours(img, cnts, -1, (0,255,0), 2)

        print("Se detectan ", len(cont), " contornos")

    def whichFigure(self):
        for c in cnts:
            float porc = 0.02 #a prueba y error
            epsilon = porc * cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            print(len(approx))

            if len(approx)==3:
                cv2.putText(img,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
                var = 3
            if len(approx)==4:
                cv2.putText(img,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
                var = 4
            if len(approx)==5:
                cv2.putText(img,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
                var = 5
            if len(approx)==6:
                cv2.putText(img,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
                var = 6

        #dependiendo de var se arma la funcion de decision

var = 0
#img = cv2.imread(r"C:/Users/lesli/Documents/GitHub/venv/figurasColores.png")
img = np.copy(frame)
gray = np.zeros(img.shape)
canny = np.zeros(img.shape)
dilate = np.zeros(img.shape)
erode = np.zeros(img.shape)
cont = np.zeros(img.shape)
erode = np.zeros(img.shape)
guas =  np.zeros(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

i = 5
guas = cv2.GaussianBlur(gray, (i, i), 0)

canny = cv2.Canny(guas, 10, 150)
dilate = cv2.dilate(canny, None, iterations=1)
erode = cv2.erode(dilate, None, iterations=1)
cnts, _ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cont = cv2.drawContours(img, cnts, -1, (0,255,0), 2)
print(len(cont))

for c in cnts:
    porc = 0.02 #a prueba y error
    epsilon = porc * cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    print(len(approx))

    if len(approx)==3:
        cv2.putText(img,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
        var = 3
    if len(approx)==4:
        cv2.putText(img,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        var = 4
    if len(approx)==5:
        cv2.putText(img,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
        var = 5
    if len(approx)==6:
        cv2.putText(img,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
        var = 6

cv2.imshow('Que figuras hay', cont)
cv2.waitKey(0)


