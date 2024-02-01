import cv2
import json
import numpy as np

from HandDetector import HandDetector

from PIL import ImageGrab

image_out = True
bg_image_out = True

detector = HandDetector(image_out, bg_image_out)
counter = 0

while True:
    screen = np.array(ImageGrab.grab(bbox=(150,150,590,660)))
    image = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    detector.draw_hands(image)

    if image_out and bg_image_out:
        allImages = np.concatenate((image, detector.img_filled), axis=1)
        cv2.imshow('Image', allImages / 255)
    elif image_out:
        cv2.imshow('Image', image)
    elif bg_image_out:
        cv2.imshow('Image', detector.img_filled)

    if cv2.waitKey(1) == ord('s'):
        if (hand_landmarks := detector.find_hands(image)) is not False:
            cv2.imwrite(f'Service/Model/NeuralNetwork/GestureData/Left_Sign/Image_{counter}.jpg', image)
            counter += 1
            print(counter)

    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()



