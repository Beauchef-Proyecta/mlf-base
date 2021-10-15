import cv2
import matplotlib.pyplot as plt
import numpy as np

class ColorDetector:

    def __init__(self, img):
        self.img = img
        self.mask = np.zeros(img.shape)
        self.masked_img = np.zeros(img.shape)
        self.eroded_img = np.zeros(img.shape)
        self.dilated_img = np.zeros(img.shape)
        self.grayscale_img = np.zeros(img.shape)
        self.thresh_img = np.zeros(img.shape)
        self.contoured_img = np.zeros(img.shape)

    def mask_image(self, lower_color, upper_color):
        img = np.copy(self.img)
        self.mask = cv2.inRange(img, lower_color, upper_color)
        self.masked_img = cv2.bitwise_and(img, img, mask=self.mask)

    def filter_image(self, kernel):
        img = self.masked_img
        self.eroded_img = cv2.erode(img, kernel)
        self.dilated_img = cv2.dilate(img, kernel)

    def find_contours(self):
        self.grayscale_img = cv2.cvtColor(self.eroded_img, cv2.COLOR_RGB2GRAY)
        ret, self.thresh_img = cv2.threshold(self.grayscale_img, 120, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(self.thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contoured_img = self.img.copy()
        cv2.drawContours(self.contoured_img, contours, -1, color=(0, 255,0), thickness=4)
