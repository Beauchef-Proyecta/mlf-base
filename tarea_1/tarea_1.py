import numpy as np
import matplotlib.pyplot as plt


class CartesianRobot:

    def __init__(self):
        self.current_position = [0, 0]

    def move_to(self, x, y):
        self.current_position[0] = x
        self.current_position[1] = y

    def draw_line_to(self, x1, y1):
        #
        plt.plot(self.current_position, [x1, y1])
        self.current_position[0] = x1
        self.current_position[1] = y1

    def draw_square(self, side=1):
        """ Dibuja un cuadrado de lado 'side' con una esquina en la posición actual del robot """
        # ------ Tu código va acá abajo ------



        # ----- Fin de tu código -----

    def draw_circle(self, radius=1):
        """Dibuja una circunferencia de radio 'radius' centrado en la posición actual del robot"""
        # ------ Tu código va acá abajo ------



        # ----- Fin de tu código -----


def main():
    robot = CartesianRobot()
    robot.draw_square()
    robot.draw_circle()
    plt.show()


if __name__ == '__main__':
    main()
