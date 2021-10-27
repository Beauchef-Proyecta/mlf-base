import numpy as np
import cv2
import matplotlib.pyplot as plt
from shape_detector import ShapeDetector
from plotter import Plotter
from decision import Manager
from mk2robot import MK2Robot




def main():

    vid = cv2.VideoCapture(2)
    sd = ShapeDetector()
    plotter = Plotter()
    manager = Manager()
    robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])

    while plotter.is_enabled():
        
        # Capturar imagen
        _, frame = vid.read()

        # Procesar
        sd.update_image(frame)
        sd.process_image()
        shape = sd.whichFigure()
        # Decidir
        command = manager.decide_what_to_do(shape)
        # Actuar
        robot.execute(command)

        # Mostrar resultado
        processed_image = sd.img_contoured
        robot_pose = robot.current_joint_positions()
        plotter.update(img=processed_image, robot=robot_pose)
    

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
