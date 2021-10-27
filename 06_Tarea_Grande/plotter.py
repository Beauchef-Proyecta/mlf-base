import matplotlib.pyplot as plt
import numpy as np
import datetime

class Plotter():

    def __init__(self):

        self.display = True
        self.fig, self.ax = plt.subplots(nrows = 1, ncols = 2)
        self.ax[1].remove()
        self.ax[1] = self.fig.add_subplot(111,projection='3d')
        plt.gcf().canvas.mpl_connect("key_press_event", self.close)
        
        self.image_plot = self.ax[0].imshow(np.zeros((9,16)))
        self.ax[0].axis("off")
        self.ax[1].axis("off")


        plt.ion()
        plt.show()

    def is_enabled(self):
        return self.display

    def close(self, event):
        if event.key == 'q':
            self.display = False
            plt.close(event.canvas.figure)

    def update(self, img, robot):
        ti = datetime.datetime.now()
        self.image_plot.set_array(img)
        [X_pos,Y_pos, Z_pos] = robot
        self.plot_robot(X_pos,Y_pos, Z_pos)
        
        
        
        plt.draw()
        plt.pause(0.05)
        dt = datetime.datetime.now() - ti
        #print(dt)
    
    def plot_robot(self, X_pos, Y_pos, Z_pos):
        # Clear figure
        self.ax[1].clear()

        # Plot the data
        self.ax[1].scatter(0, 0, 0, zdir='z', s=30)  # Origin
        self.ax[1].plot([0, X_pos[0]], [0, Y_pos[0]], [0, Z_pos[0]])  # L0
        self.ax[1].plot([X_pos[0], X_pos[1]], [Y_pos[0], Y_pos[1]], [Z_pos[0], Z_pos[1]])  # L1
        self.ax[1].plot([X_pos[1], X_pos[2]], [Y_pos[1], Y_pos[2]], [Z_pos[1], Z_pos[2]])  # L2
        self.ax[1].plot([X_pos[2], X_pos[3]], [Y_pos[2], Y_pos[3]], [Z_pos[2], Z_pos[3]])  # L3
        self.ax[1].scatter(X_pos, Y_pos, Z_pos, zdir='z', s=20)  # Joints

        # Make it prettier
        self.ax[1].set_ylabel('Y [mm]')
        self.ax[1].set_xlabel('X [mm]')
        self.ax[1].set_zlabel('Z [mm]')

        # Set axis limits
        self.ax[1].set_xlim(-300, 300)
        self.ax[1].set_ylim(-300, 300)
        self.ax[1].set_zlim(0, 300)