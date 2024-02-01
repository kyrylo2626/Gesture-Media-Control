from PyQt5 import Qt, QtCore, QtGui, QtWidgets

from Client.View.DraggableFrame import DraggableFrameForm
from Service.Controller.ConfigController.ActionConfig import ActionConfig

class GestureManualForm:

    def __init__(self, mode):
        self.window = DraggableFrameForm()
        self.mode = mode
        self.setupUi()

        self.changeLabels = []


    def setupUi(self):

        self.window.resize(1300, 940)
        self.window.frame.setGeometry(QtCore.QRect(10, 10, 1280, 920))

        self.window.label.setGeometry(QtCore.QRect(0, 20, 1280, 40))
        if self.mode == 'change':
            self.window.label.setText("Оберіть команди, які бажаєте змінити місцями:")
        else:
            self.window.label.setText("Інструкція користування:")

        self.window.toolButton.setGeometry(QtCore.QRect(1209, 0, 71, 71))
        self.window.toolButton.clicked.connect(self.window.close)
        
        self.frame1 = QtWidgets.QFrame(self.window.frame)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.frame1.setGeometry(QtCore.QRect(25, 75, 1230, 820))

        self.labels_manager(ActionConfig.get_action())

        self.window.slots_connect()
        self.window.show()
    

    def labels_manager(self, listLabelsText):
        listLabels = []
        position = 205
        index = 0
        for i in listLabelsText.items():
            if index > 3:
                position = 820
                index = 0

            listLabels.append(self.label_factory(index, position, i))

            index += 1



    def label_factory(self, index, position, text):
        if self.mode == 'change':
            UIElement = QtWidgets.QPushButton
        else:
            UIElement = QtWidgets.QLabel

        label = UIElement(self.frame1)
        label.setGeometry(QtCore.QRect(position, index*205, 406, 201))
        label.setText(text[1])

        if self.mode == 'change':
            label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            label.setObjectName(f"label_ges_change")
            label.keyCommand = text[0]
            label.clicked.connect(lambda: self.label_click(label))
        else:
            label.setAlignment(QtCore.Qt.AlignCenter)


        return label

    
    def label_click(self, label):
        self.changeLabels.append(label)
        label.setStyleSheet("border: 2px solid black;")

        if len(self.changeLabels) > 1:

            firstText = self.changeLabels[0].text()
            secondText = self.changeLabels[1].text()
            self.changeLabels[0].setText(secondText)
            self.changeLabels[1].setText(firstText)

            self.changeLabels[0].setStyleSheet("border: none;")
            self.changeLabels[1].setStyleSheet("border: none;")

            ActionConfig.set_action(self.changeLabels)

            self.changeLabels = []