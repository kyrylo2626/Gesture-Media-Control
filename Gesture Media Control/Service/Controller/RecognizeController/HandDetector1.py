import cv2
import numpy as np
import mediapipe as mp
import time

class HandDetector():

    def __init__(self, show_image, show_bg_image):

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils

        self.show_image = show_image
        self.show_bg_image = show_bg_image


    def convert_image(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)


    def fill_background(self, img):
        self.img_filled = np.empty(img.shape)
        self.img_filled.fill(0)
        

    def find_hands(self, img):
        self.convert_image(img)

        if self.results.multi_hand_landmarks:
            return self.results.multi_hand_landmarks[0]

        return False


    def draw_hands(self, img):
        if (hand_landmarks := self.find_hands(img)) is not False:
            if self.show_bg_image:
                self.fill_background(img)
                self.mpDraw.draw_landmarks(self.img_filled, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
            if self.show_image:
                self.mpDraw.draw_landmarks(img, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
    

    def gesture_recognizer(self, hand_landmarks):
        data_list = []
        for hand_point in hand_landmarks.landmark:
            sub_data_list = [hand_point.x, hand_point.y]
            data_list.append(sub_data_list)
        
        return data_list

        
