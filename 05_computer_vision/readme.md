# Tarea 5.1 - ¿Dónde están los ponies?

En esta tarea debes usar OpenCV para detectar *unicornios y/o ponies* en base a su color. Para ello debes:
1. Crear una máscara que filtre un rango de colores (en el espacio HSV)
2. Aplicar la máscara a la imagen ponies.jpg para dejar solo los colores deseados
3. Filtrar la imagen para reducir el ruido
4. Encontrar los contornos de las zonas de interés
5. Calcular las bounding boxes (rectángulos) y dibujarlos sobre la imagen


**Entregables:** los códigos color_detector.py y tarea_05.py completos 🙂

## Material Extra

Puedes encontrar un *jupyter notebook* interactivo en el siguiente enlace, donde puedes jugar con las distintas herramientas que tiene OpenCV:

[![Material Extra - Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/felipesanmartin/TutorialCV/blob/master/TutorialCV.ipynb)

## Funciones útiles
Estas funciones de OpenCV serán de utilidad para resolver el desafío:

`img_out = cv2.cvtColor(img_in, COLOR_CODE)`: permite transformar imágenes de un espacio de color a otro.

`mask = cv2.inRange(img_in, lower, upper)`: Genera una máscara con los valores que cumplen la condición, es decir, se encuentran entre los límites establecidos.

`img_out = cv2.bitwise_and(img_in, img_in, mask = mask)`: Genera una imagen "enmascarada".

`mask_out = cv2.erode(mask_in, kernel, iterations = 1)`: Operación morfológicas de erosión.

`mask_out = cv2.dilate(mask_in, kernel, iterations = 1)`: Operación morfológicas de dilatación.

`contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)`: Retorna contornos de los blobs en una imagen binaria.

`x, y, w, h = cv2.boundingRect(contour)`: Entrega coordenadas del rectángulo más pequeño que contiene al contorno.

`cv2.rectangle(img_in, (x1, y1), (x2, y2), COLOR, line_width)`: Dibuja el rectángulo de coordenadas `(x1, y1)`, `(x2, y2)` en la imagen de entrada `img_in`.

`cv2.imshow('nombre', img_bgr)`: Muestra la imagen `img_bgr` en una ventana `nombre`. La imagen debe estar en el espacio de colog BGR para que se visualice correctamente.


