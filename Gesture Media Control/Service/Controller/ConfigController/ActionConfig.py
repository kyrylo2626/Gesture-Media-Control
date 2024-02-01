import json
from Service.Controller.ConfigController import GestureConfig

class ActionConfig:

    @staticmethod
    def get_action():
        gestureData = GestureConfig.GestureConfig()
        actionOrder = gestureData.get_action_list()
        with open('Service\Model\ConfigFiles\ActionConfig.json', encoding='utf-8') as file:
            actionText = json.load(file)
        data = {key: actionText[key] for key in actionOrder}
        return data

    @staticmethod
    def set_action(listActions):
        for i in GestureConfig.gestureCollection:
            if GestureConfig.gestureCollection[i].get_action_name() == listActions[0].keyCommand:
                GestureConfig.gestureCollection[i].set_action(listActions[1].keyCommand)
            elif GestureConfig.gestureCollection[i].get_action_name() == listActions[1].keyCommand:
                GestureConfig.gestureCollection[i].set_action(listActions[0].keyCommand)