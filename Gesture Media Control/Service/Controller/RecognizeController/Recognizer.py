import time
import cv2
import numpy as np
import tensorflow as tf

from Service.Controller.RecognizeController.HandDetector import HandDetector
from Service.Controller.RecognizeController.CommandManager import GestureConf
from Service.Controller.ConfigController.AppConfig import config


class Recognizer:

    def __init__(self, slider):
        self.active = False

        self.show_image = config.IMAGE_OUTPUT
        self.show_bg_image = config.BG_IMAGE_OUTPUT

        self.cap = cv2.VideoCapture(config.CAMERA_INDEX)
        self.detector = HandDetector(self.show_image, self.show_bg_image)

        self.model_loaded = tf.keras.models.load_model(config.KERAS_MODEL)

        self.commandManager = GestureConf()
        self.timePause = time.time()
        self.timeDelay = 0
        self.gestureMemory = None

        self.windowSlider = slider


    def recognize(self):

        while True:
            success, img = self.cap.read()

            if not success:
                self.cap = cv2.VideoCapture(0)
                continue

            self.detector.draw_hands(img)

            if time.time() - self.timePause > 1:
                if (hand_landmarks := self.detector.find_hands(img)) is not False:

                    points_data = tf.expand_dims(self.detector.gesture_recognizer(hand_landmarks), axis=0)
                    result = self.model_loaded.predict(points_data, verbose=0)
                    
                    if np.max(result) > 0.99:
                        if self.gestureMemory is None or self.gestureMemory != np.argmax(result):
                            self.gestureMemory = np.argmax(result)
                            self.timeDelay = time.time()
                        elif self.gestureMemory == np.argmax(result) and time.time() - self.timeDelay > 1:
                            self.commandManager(np.argmax(result))
                            self.timePause = time.time()
                            self.gestureMemory = None

            if self.show_image and self.show_bg_image:
                allImages = np.concatenate((img, self.detector.img_filled), axis=1)
                cv2.imshow('Image', allImages / 255)
            elif self.show_image: cv2.imshow('Image', img)
            elif self.show_bg_image: cv2.imshow('Image', self.detector.img_filled)
            
            if not self.active:
                break
            
            # keyCode = cv2.waitKey(1000)
            # if cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) < 1:
            #     break

            if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        
        self.active = False
        self.windowSlider.setValue(100)
        self.cap.release()
        cv2.destroyAllWindows()
