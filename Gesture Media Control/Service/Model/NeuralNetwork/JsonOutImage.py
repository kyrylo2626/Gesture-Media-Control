import cv2
import json
from Service.Controller.RecognizeController.HandDetector import HandDetector

cap = cv2.VideoCapture(0)

image_out = True
bg_image_out = True

detector = HandDetector(image_out, bg_image_out)
counter = 0

while True:
    success, image = cap.read()

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
            detector.gesture_recognizer(hand_landmarks, True)
            counter += 1
            print(counter)

    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) & 0xFF == ord('q'):
        break

dataset = "1_Five_Sign"
with open(f"Data/{dataset}/{dataset}_Data.json", "w") as data_file:
    data_file.write(json.dumps(detector.data))

cap.release()
cv2.destroyAllWindows()



