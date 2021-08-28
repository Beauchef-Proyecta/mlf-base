import numpy as np
import matplotlib.pyplot as plt
from utils import add_arrow

class CartesianRobot:

    def __init__(self):
        self.current_position = [0, 0]
        self.home = [0, 0]
        self._pen_state = False

    def enable_pen(self):
        self._pen_state = True

    def disable_pen(self):
        self._pen_state = False

    def move_to(self, x, y):
        if self._pen_state:
            self._draw_line_to(x, y)

        self.current_position = [x, y]

    def move_to_home(self):
        self.move_to(self.home[0], self.home[1])

    def _draw_line_to(self, x, y):
        x_data = [self.current_position[0], x]
        y_data = [self.current_position[1], y]
        line = plt.plot(x_data, y_data)
        add_arrow(line[-1])

        
def main():
    robot = CartesianRobot()

    robot.enable_pen()
    robot.move_to(10, 5)

    robot.disable_pen()
    robot.move_to(10, 10)

    robot.enable_pen()
    robot.move_to(0, 20)

    plt.show()


if __name__ == '__main__':
    main()