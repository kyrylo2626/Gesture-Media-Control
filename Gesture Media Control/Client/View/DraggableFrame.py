from PyQt5 import Qt, QtCore, QtGui, QtWidgets


class DraggableFrameForm(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()
        # Флаг відсілідкування стану переміщення
        self.dragging = False
        # Точка початку перетаскування
        self.drag_start_position = QtCore.QPoint()


    def mousePressEvent(self, event):
        # Початкова позиція при натисканні кнопки миші
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.drag_start_position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        # Переміщення вікна, якщо флаг перетаскування True
        if self.dragging:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        # Скидання флагу перетаскування при відпусканні кнопки миші
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False
            event.accept()

    def setupUI(self):
        self.setObjectName("MainWidget")
        self.setEnabled(True)
        self.resize(920, 470)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(15)
        self.setFont(font)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        with open("Client\View\Stylesheets\Style.qss", "r") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())
        self.setDocumentMode(False)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.startwidget = QtWidgets.QWidget(self)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(15)
        self.startwidget.setFont(font)
        self.startwidget.setObjectName("startwidget")

        self.frame = QtWidgets.QFrame(self.startwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        shadow = Qt.QGraphicsDropShadowEffect(blurRadius=10, xOffset=0, yOffset=0)
        self.frame.setGraphicsEffect(shadow)

        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setText("×")


        self.setWindowIcon(QtGui.QIcon("Client/View/Images/icon.ico"))
        self.setWindowTitle("Gesture Media Control")


    def slots_connect(self):
        self.setCentralWidget(self.startwidget)
        QtCore.QMetaObject.connectSlotsByName(self)


    def show_app(self, app):
        for window in app.windows:
            try: window.window.show()
            except AttributeError: pass


    def close_app(self, app):
        for window in app.windows:
            try: window.window.close()
            except AttributeError: pass
       

    def hide_app(self, app):
        for window in app.windows:
            try: window.window.hide()
            except AttributeError: pass

