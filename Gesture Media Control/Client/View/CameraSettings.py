from PyQt5 import QtCore, QtGui, QtWidgets

from Client.View.DraggableFrame import DraggableFrameForm
from Service.Controller.DeviceController.CameraController import camera

class CameraSettingsForm:

    def __init__(self):
        self.window = DraggableFrameForm()
        self.setupUi()


    def setupUi(self):

        self.window.frame.setGeometry(QtCore.QRect(70, 80, 780, 330))

        self.window.label.setGeometry(QtCore.QRect(0, 20, 780, 40))
        self.window.label.setText("Оберіть веб-камеру:")

        self.window.toolButton.setGeometry(QtCore.QRect(709, 0, 71, 71))
        self.window.toolButton.clicked.connect(self.window.close)

        self.buttons_manager(camera.camera_init())

        self.window.slots_connect()
        self.window.show()


    def buttons_manager(self, listCamera):
        lenghtListCamera = len(listCamera)
        if lenghtListCamera < 4: position = 240
        else: position = 60

        listButtons = []
        for i in range(lenghtListCamera):
            if i > 2: listButtons.append(self.button_factory(i-2, listCamera[i], 420))
            else: listButtons.append(self.button_factory(i+1, listCamera[i], position))


    def button_factory(self, index, name, position):
        button = QtWidgets.QPushButton(self.window.frame)
        button.setGeometry(QtCore.QRect(position, (index*80)+10, 300, 50)) #60 #240
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setObjectName(f"button_{name}")
        button.setText(name)

        button.clicked.connect(lambda: self.button_name(name))

        return button

    
    def button_name(self, name):
        camera.set_camera(name)
        self.window.close()

