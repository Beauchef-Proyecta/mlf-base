import numpy as np
import matplotlib.pyplot as plt
from plot_utils import add_arrow


class JointedRobot:

    def __init__(self, l1=10, l2=10):
        self.q = [0, 0]
        self.l = [l1, l2]
        self.origin = [0,0]
        self.pose = []
        self.update_pose()

    def set_position_by_q(self, q1, q2):
        self.q = [q1, q2]
        self.update_pose()

    def update_pose(self):
        pose_1 = np.multiply([np.cos(self.q[0]), np.sin(self.q[0])], self.l[0])
        pose_2 = pose_1 + np.multiply([np.cos(self.q[1]+self.q[0]), np.sin(self.q[1]+self.q[0])], self.l[1])
        self.pose = [pose_1, pose_2]

    def plot_links(self):
        # L1
        x_data = [self.origin[0], self.pose[0][0]]
        y_data = [self.origin[1], self.pose[0][1]]
        plt.plot(x_data,y_data)
        # L2
        x_data = [self.pose[0][0], self.pose[1][0]]
        y_data = [self.pose[0][1], self.pose[1][1]]
        plt.plot(x_data,y_data)
        plt.show()


def main():
    robot = JointedRobot()
    robot.set_position(1, 0.5)
    print(robot.pose)
    robot.plot_links()


if __name__ == '__main__':
    main()