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
        if self.show_bg_image: self.fill_background(img)
        if (hand_landmarks := self.find_hands(img)) is not False:
            if self.show_bg_image:
                self.mpDraw.draw_landmarks(self.img_filled, hand_landmarks)
                for idx, landmark in enumerate(hand_landmarks.landmark):
                    cx, cy = int(landmark.x * self.img_filled.shape[1]) + 5, int(landmark.y * self.img_filled.shape[0]) - 5
                    cv2.putText(self.img_filled, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

                cv2.line(self.img_filled, (0, self.img_filled.shape[0]-5), (self.img_filled.shape[1], self.img_filled.shape[0] - 5), (255, 255, 255), 1)
                cv2.line(self.img_filled, (5, 0), (5, self.img_filled.shape[0]), (255, 255, 255), 1)

                for x in range(0, self.img_filled.shape[1] + 1, int(self.img_filled.shape[1] / 10)):
                    if x in [0, self.img_filled.shape[1]]: continue
                    cv2.line(self.img_filled, (x+5, self.img_filled.shape[0]), (x+5, self.img_filled.shape[0]-10), (255, 255, 255), 1)
                    cv2.putText(self.img_filled, f'{x / self.img_filled.shape[1]:.1f}', (x+5, self.img_filled.shape[0]-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

                for y in range(0, self.img_filled.shape[0] + 1, int(self.img_filled.shape[0] / 10)):
                    cv2.line(self.img_filled, (0, y+5), (10, y+5), (255, 255, 255), 1)
                    if y in [0, self.img_filled.shape[0]]: continue
                    cv2.putText(self.img_filled, f'{1 - y / self.img_filled.shape[0]:.1f}', (15, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


            if self.show_image:
                self.mpDraw.draw_landmarks(img, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
            
    

    def gesture_recognizer(self, hand_landmarks):
        data_list = []
        for hand_point in hand_landmarks.landmark:
            sub_data_list = [hand_point.x, hand_point.y]
            data_list.append(sub_data_list)
        
        return data_list

        
