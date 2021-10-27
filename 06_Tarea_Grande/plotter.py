import matplotlib.pyplot as plt

class Plotter():

    def __init__(self):

        self.display = True
        self.fig, self.ax = plt.subplots(1,2)
        plt.gcf().canvas.mpl_connect("key_press_event", self.close)
        # Esta linea es muy importante: es la que "abre" la ventana de los graficos
        plt.ion()
        plt.show()

    def is_enabled(self):
        return self.display

    def close(self, event):
        if event.key == 'q':
            self.display = False
            plt.close(event.canvas.figure)

    def update(self, img):
        self.ax[0].imshow(img[0])
        self.ax[0].axis("off")
        self.ax[1].imshow(img[1])
        self.ax[1].axis("off")
        plt.draw()
        plt.pause(0.01)
    