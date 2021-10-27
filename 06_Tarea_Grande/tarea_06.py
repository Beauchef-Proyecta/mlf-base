import numpy as np
import cv2
import matplotlib.pyplot as plt
from shape_detector import ShapeDetector
from plotter import Plotter
from decision import Manager
from mk2robot import MK2Robot




def main():

    """ [Inicialización]
    Todo sistema de robots tiene varios subsistemas, cada cual con una responsabilidad única
    y funcionan de manera coordinada.
    En este caso, tenemos 5 sub-sistemas:
    1. camera: responsable de operar la cámara
    2. detector: procesa la imagen obtenida por el subsitema camera y entrega información útil para saber qué hacer con el robot
    3. manager: implementa una "estrategia" según lo que se detecta y genera una instrucción (command) para que el robot la ejecute
    4. robot: recibe la instrucción y la ejecuta (por sus propios medios)
    5. plotter: muestra lo que está pasando. No es esencial para el funcionamiento, pero nos permite a les humanes cachar qué está pasando o.o

    """
    camera = cv2.VideoCapture(2)    # Usar la que tengan disponible en su pc; por defecto es 0
    detector = ShapeDetector()
    manager = Manager()
    robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
    plotter = Plotter()

    while plotter.is_enabled():
        
        # 1. Capturar imagen
        _, frame = camera.read()

        # 2. Procesar
        detector.update_image(frame)
        detector.process_image()
        shape = detector.whichFigure()
        
        # 3. Decidir
        command = manager.decide_what_to_do(shape)
        
        # 4. Actuar
        robot.execute(command)

        # 5. Mostrar resultado
        processed_image = detector.img_contoured
        robot_pose = robot.current_joint_positions()
        plotter.update(img=processed_image, robot=robot_pose)
    
    # Una vez que se cierra el plot, se destruye todo para tener una salida limpia :)
    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
