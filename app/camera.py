import cv2
from pathlib import Path
import numpy as np

class Camera:
    def __init__(self):
        self.camera = None

    def initialize(self):
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise RuntimeError("Could not initialize camera")

    def capture_image(self, save_path):
        if self.camera is None:
            self.initialize()

        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Failed to capture image")

        # Save the image
        cv2.imwrite(save_path, frame)
        return save_path

    def release(self):
        if self.camera:
            self.camera.release()
            self.camera = None