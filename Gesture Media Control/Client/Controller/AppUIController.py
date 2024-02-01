from Client.View.MainApp import MainAppForm

from Service.Controller.ConfigController.AppConfig import config
from Service.Controller.DeviceController.PlayerController import PlayerController
from Service.Controller.RecognizeController.Recognizer import Recognizer


class AppUIController:
    
    def __init__(self):
        self.mainWindow = MainAppForm()
        self.set_checkBox_UI()

        self.mainWindow.wmplayer_checkBox.clicked.connect(self.set_player)
        self.mainWindow.image_checkBox.clicked.connect(lambda: config.set_param('IMAGE_OUTPUT'))
        self.mainWindow.bg_image_checkBox.clicked.connect(lambda: config.set_param('BG_IMAGE_OUTPUT'))
        self.mainWindow.manual_button.clicked.connect(lambda: self.mainWindow.show_manual_window('read'))              # Інструкція
        self.mainWindow.set_camera_button.clicked.connect(self.mainWindow.show_camera_window)                     # Обрати веб-камеру
        self.mainWindow.set_gesture_button.clicked.connect(lambda: self.mainWindow.show_manual_window('change'))       # Обрати команди жестам
        self.mainWindow.set_player_button.clicked.connect(self.new_player)

        self.mainWindow.switch_slider.valueChanged.connect(self.recognizer_setup)

        self.mainWindow.window.show()


    def recognizer_setup(self):
        if self.mainWindow.switch_slider.value() == 0:
            self.recognizer = Recognizer(self.mainWindow.switch_slider)
            self.recognizer.active = True
            self.recognizer.recognize()
        elif self.mainWindow.switch_slider.value() == 100:
            self.recognizer.active = False
            self.recognizer = None
        self.mainWindow.correct_pos()


    def new_player(self):
        file = self.mainWindow.choose_file()[0]
        if file != "": PlayerController().set_player(file)


    def set_player(self):
        if config.WMPLAYER is True: self.new_player()
        else: PlayerController().set_main_player()
        config.set_param('WMPLAYER')


    def set_checkBox_UI(self):

        if config.WMPLAYER is True: self.mainWindow.wmplayer_checkBox.setChecked(True)
        else: self.mainWindow.wmplayer_checkBox.setChecked(False)

        if config.IMAGE_OUTPUT is True: self.mainWindow.image_checkBox.setChecked(True)
        else: self.mainWindow.image_checkBox.setChecked(False)

        if config.BG_IMAGE_OUTPUT is True: self.mainWindow.bg_image_checkBox.setChecked(True)
        else: self.mainWindow.bg_image_checkBox.setChecked(False)



        
    
    





