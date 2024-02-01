import json

from Service.Controller.DeviceController import PlayerController 


class GestureConfig:

    def get_action(self):
        return PlayerController.commandCollection[self.read_config()[self.name]]

    
    def get_action_name(self):
        return self.read_config()[self.name]


    def get_action_list(self):
        data = self.read_config()
        return list(data.values())


    def set_action(self, value):
        data = self.read_config()
        data[self.name] = value
        self.update_config(data)


    def read_config(self):
        with open('Service\Model\ConfigFiles\GestureConfig.json') as file:
            data = json.load(file)
        return data


    def update_config(self, data):
        with open('Service\Model\ConfigFiles\GestureConfig.json', 'w') as file:
            json.dump(data, file)



class Gesture(GestureConfig):

    def __init__(self, index, name):
        self.gestureId = index
        self.name = name



fiveGesture  = Gesture(0, "FIVE")
twoGesture   = Gesture(1, "TWO")
okayGesture  = Gesture(2, "OKAY")
fistGesture  = Gesture(3, "FIST")
rightGesture = Gesture(4, "RIGHT")
leftGesture  = Gesture(5, "LEFT")
upGesture    = Gesture(6, "UP")
downGesture  = Gesture(7, "DOWN")


gestureCollection = {
    "FIVE": fiveGesture,
    "TWO": twoGesture,
    "OKAY": okayGesture,
    "FIST": fistGesture,
    "RIGHT": rightGesture,
    "LEFT": leftGesture,
    "UP": upGesture,
    "DOWN": downGesture
}
