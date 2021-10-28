import matplotlib.pyplot as plt
import numpy as np
import datetime

class Plotter():

    def __init__(self):

        self.display = True
        self.ax = [None, None]
        self.fig = plt.figure()
        self.fig.set_size_inches(8,4)

        self.ax[0] = self.fig.add_subplot(121)
        self.ax[1] = self.fig.add_subplot(122,projection='3d')

        self.ax[1].axis("off")
        plt.gcf().canvas.mpl_connect("key_press_event", self.close)
        
        self.image_plot = self.ax[0].imshow(np.zeros((480,640)))
        

        plt.ion()
        plt.show()

    def is_enabled(self):
        return self.display

    def close(self, event):
        if event.key == 'q':
            self.display = False
            plt.close(event.canvas.figure)

    def update(self, img, robot):
        self.image_plot.set_data(img)

        [X_pos,Y_pos, Z_pos] = robot
        self.plot_robot(X_pos,Y_pos, Z_pos)
        plt.draw()
        plt.pause(0.05)
    
    def plot_robot(self, X_pos, Y_pos, Z_pos):
        self.ax[1].clear()

        self.ax[1].scatter(0, 0, 0, zdir='z', s=30)  # Origin
        self.ax[1].plot([0, X_pos[0]], [0, Y_pos[0]], [0, Z_pos[0]])  # L0
        self.ax[1].plot([X_pos[0], X_pos[1]], [Y_pos[0], Y_pos[1]], [Z_pos[0], Z_pos[1]])  # L1
        self.ax[1].plot([X_pos[1], X_pos[2]], [Y_pos[1], Y_pos[2]], [Z_pos[1], Z_pos[2]])  # L2
        self.ax[1].plot([X_pos[2], X_pos[3]], [Y_pos[2], Y_pos[3]], [Z_pos[2], Z_pos[3]])  # L3
        self.ax[1].scatter(X_pos, Y_pos, Z_pos, zdir='z', s=20)  # Joints

        self.ax[1].set_ylabel('Y [mm]')
        self.ax[1].set_xlabel('X [mm]')
        self.ax[1].set_zlabel('Z [mm]')

        self.ax[1].set_xlim(-300, 300)
        self.ax[1].set_ylim(-300, 300)
        self.ax[1].set_zlim(0, 300)