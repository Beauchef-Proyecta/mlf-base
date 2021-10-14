import numpy as np
import matplotlib.pyplot as plt


class CartesianRobot:

    def __init__(self):
        self.current_position = [0, 0]

    def move_to(self, x, y):
        self.current_position[0] = x
        self.current_position[1] = y

    def draw_line_to(self, x1, y1):
        x_axes = [self.current_position[0], x1]
        y_axes = [self.current_position[1], y1]
        plt.plot(x_axes, y_axes)
        self.move_to(x1, y1)

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
    robot.move_to(0, 0)
    robot.draw_line_to(1, 1)
    robot.draw_line_to(2, 2)
    robot.draw_line_to(5, 2)
    robot.draw_square()
    robot.draw_circle()
    plt.show()


if __name__ == '__main__':
    main()
