import json

class AppConfig:

    def __set_name__(self, owner, name):
        self.name = name


    def __get__(self, instance, owner):
        return self.read_config()[self.name]


    def __set__(self, instance=None, value=None):
        data = self.read_config()
        
        if value is None and isinstance(data[self.name], bool):
            data[self.name] = not data[self.name]
        else:
            data[self.name] = value
            
        self.update_config(data)


    def read_config(self):
        with open('Service/Model/ConfigFiles/AppConfig.json') as file:
            data = json.load(file)
        return data


    def update_config(self, data):
        with open('Service/Model/ConfigFiles/AppConfig.json', 'w') as file:
            json.dump(data, file)



class Config:

    WMPLAYER = AppConfig()
    IMAGE_OUTPUT = AppConfig()
    BG_IMAGE_OUTPUT = AppConfig()
    CAMERA_INDEX = AppConfig()
    KERAS_MODEL = AppConfig()
    PLAYER = AppConfig()
    DEFAULT_PLAYER = AppConfig()

    def set_param(self, name, new_value=None):
        Config.__dict__[name].__set__(value=new_value)



config = Config()

