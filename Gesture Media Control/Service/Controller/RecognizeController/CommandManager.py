from Service.Controller.ConfigController import GestureConfig

class GestureConf:

    def __call__(self, index):
            if   index == 0: GestureConfig.fiveGesture.get_action()()
            elif index == 1: GestureConfig.twoGesture.get_action()()
            elif index == 2: GestureConfig.okayGesture.get_action()()
            elif index == 3: GestureConfig.fistGesture.get_action()()
            elif index == 4: GestureConfig.rightGesture.get_action()()
            elif index == 5: GestureConfig.leftGesture.get_action()()
            elif index == 6: GestureConfig.upGesture.get_action()()
            elif index == 7: GestureConfig.downGesture.get_action()()