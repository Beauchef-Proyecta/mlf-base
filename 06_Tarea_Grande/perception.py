import cv2


# define a video capture object
vid = cv2.VideoCapture(2)

while (True):

    # Capture the video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    if frame is not None:
        cv2.imshow('Captura tu figurita', cv2.flip(frame, 1))

    # the 'q' button is set as the quitting button you may use any desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


class figureDetector:
    def __init__(self, img):
        self.img = img

        # Inicializamos en cero todas las imagenes que guardaremos
        self.mask = np.zeros(img.shape)
        self.img_masked = np.zeros(img.shape)
        self.img_eroded = np.zeros(img.shape)
        self.img_dilated = np.zeros(img.shape)
        self.img_gray = np.zeros(img.shape)
        self.img_threshold = np.zeros(img.shape)
        self.img_contoured = np.zeros(img.shape)


# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


class ColorDetector:

    def __init__(self, img):
        self.img = img

        # Inicializamos en cero todas las imagenes que guardaremos
        self.mask = np.zeros(img.shape)
        self.img_masked = np.zeros(img.shape)
        self.img_eroded = np.zeros(img.shape)
        self.img_dilated = np.zeros(img.shape)
        self.img_gray = np.zeros(img.shape)
        self.img_threshold = np.zeros(img.shape)
        self.img_contoured = np.zeros(img.shape)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


