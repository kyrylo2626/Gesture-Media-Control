from PyQt5 import QtCore, QtGui, QtWidgets

from Client.View.DraggableFrame import DraggableFrameForm
from Client.View.CameraSettings import CameraSettingsForm
from Client.View.GestureManual import GestureManualForm

class MainAppForm:

    def __init__(self):
        self.window = DraggableFrameForm()
        self.setupUi()

        self.popUpWindow = None
        self.manual = None
        self.windows = [self.popUpWindow, self.manual, self]


    def setupUi(self):

        self.window.frame.setGeometry(QtCore.QRect(10, 10, 900, 450))

        self.window.label.setGeometry(QtCore.QRect(0, 20, 900, 40))

        self.window.toolButton.setGeometry(QtCore.QRect(829, 0, 71, 71))
        self.window.toolButton.clicked.connect(lambda: self.window.hide_app(self))

        self.label_2 = QtWidgets.QLabel(self.window.frame)
        self.label_2.setGeometry(QtCore.QRect(500, 110, 500, 60))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.window.frame)
        self.label_3.setGeometry(QtCore.QRect(710, 110, 500, 60))
        self.label_3.setObjectName("label_3")

        self.manual_button = QtWidgets.QPushButton(self.window.frame)
        self.manual_button.setGeometry(QtCore.QRect(75, 100, 300, 50))
        self.manual_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manual_button.setObjectName("manual_button")

        self.set_camera_button = QtWidgets.QPushButton(self.window.frame)
        self.set_camera_button.setGeometry(QtCore.QRect(75, 180, 300, 50))
        self.set_camera_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_camera_button.setObjectName("set_camera_button")

        self.set_gesture_button = QtWidgets.QPushButton(self.window.frame)
        self.set_gesture_button.setGeometry(QtCore.QRect(75, 260, 300, 50))
        self.set_gesture_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_gesture_button.setObjectName("set_gesture_button")

        self.set_player_button = QtWidgets.QPushButton(self.window.frame)
        self.set_player_button.setGeometry(QtCore.QRect(75, 340, 300, 50))
        self.set_player_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_player_button.setObjectName("set_player_button")

        self.wmplayer_checkBox = QtWidgets.QCheckBox(self.window.frame)
        self.wmplayer_checkBox.setGeometry(QtCore.QRect(425, 215, 520, 70))
        self.wmplayer_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wmplayer_checkBox.setChecked(False)
        self.wmplayer_checkBox.setTristate(False)
        self.wmplayer_checkBox.setStyleSheet("padding-left: 25px")
        self.wmplayer_checkBox.setObjectName("wmplayer")

        self.image_checkBox = QtWidgets.QCheckBox(self.window.frame)
        self.image_checkBox.setGeometry(QtCore.QRect(425, 285, 520, 70))
        self.image_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.image_checkBox.setChecked(False)
        self.image_checkBox.setTristate(False)
        self.image_checkBox.setStyleSheet("padding-left: 25px")
        self.image_checkBox.setObjectName("image")

        self.bg_image_checkBox = QtWidgets.QCheckBox(self.window.frame)
        self.bg_image_checkBox.setGeometry(QtCore.QRect(425, 340, 520, 70))
        self.bg_image_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bg_image_checkBox.setChecked(False)
        self.bg_image_checkBox.setTristate(False)
        self.bg_image_checkBox.setStyleSheet("padding-left: 25px")
        self.bg_image_checkBox.setObjectName("bg_image")
        
        self.switch_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.window.frame)
        self.switch_slider.setFixedSize(120, 70)
        self.switch_slider.setValue(100)
        self.switch_slider.setMinimum(0)
        self.switch_slider.setMaximum(100)
        self.switch_slider.setTickInterval(100)
        self.switch_slider.setSingleStep(100)
        self.switch_slider.setPageStep(100)
        self.switch_slider.sliderReleased.connect(self.correct_pos)
        # self.switch_slider.valueChanged.connect(self.slider_action)
        self.switch_slider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.switch_slider.setGeometry(QtCore.QRect(570, 105, 120, 50))
        
        self.tray_icon = QtWidgets.QSystemTrayIcon(self.window)
        self.tray_icon.setIcon(QtGui.QIcon("Client/View/Images/icon.ico"))
        show_action = QtWidgets.QAction("Показати", self.window)
        quit_action = QtWidgets.QAction("Закрити", self.window)
        show_action.triggered.connect(lambda: self.window.show_app(self))
        quit_action.triggered.connect(lambda: self.window.close_app(self))
        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.activated.connect(self.showMenuOnTrigger)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.window.label.setText("Gesture Media Control")
        self.label_2.setText("ВКЛ")
        self.label_3.setText("ВИКЛ")
        self.wmplayer_checkBox.setText("Використовувати стандартний\nплеєр Windows Media Player")
        self.image_checkBox.setText("Показувати вхідне зображення")
        self.bg_image_checkBox.setText("Показувати вихідне зображення")
        self.manual_button.setText("Інструкція")
        self.set_camera_button.setText("Обрати веб-камеру")
        self.set_gesture_button.setText("Обрати команди жестам")
        self.set_player_button.setText("Обрати музичний плеєр")

        self.window.slots_connect()


    def correct_pos(self):
        if self.switch_slider.value() < 50:
            corrected = 0
        else:
            corrected = 100
        self.switch_slider.setValue(corrected)


    def showMenuOnTrigger(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.window.show_app(self)

    
    def choose_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self.window, caption='Оберіть плеєр:', filter='(*.exe)')
        return file


    def show_camera_window(self):
        self.popUpWindow = CameraSettingsForm()
        self.windows[0] = self.popUpWindow


    def show_manual_window(self, mode):
        self.manual = GestureManualForm(mode)
        self.windows[1] = self.manual