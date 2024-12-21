from PyQt5 import QtCore, QtGui, QtWidgets


class MovablePolygon(QtWidgets.QGraphicsPolygonItem):
    def __init__(self, polygon, label_text):
        super().__init__(polygon)
        self.setBrush(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        self.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 2))
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        # Create label and set it as a child of this polygon item
        self.label = QtWidgets.QGraphicsTextItem(label_text, self)
        self.label.setDefaultTextColor(QtGui.QColor(0, 0, 0))
        self.label.setFont(QtGui.QFont("Arial", 12))
        self.update_label_position()


    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemPositionChange:
            self.update_label_position()
        return super().itemChange(change, value)

    def update_label_position(self):
        # Set the label position relative to the polygon
        rect = self.boundingRect()
        self.label.setPos(rect.center() - QtCore.QPointF(self.label.boundingRect().width() / 2,
                                                         self.label.boundingRect().height() / 2))

        rect = self.boundingRect()

        self.label.setPos(rect.center() - QtCore.QPointF(self.label.boundingRect().width() / 2,

                                                         self.label.boundingRect().height() / 2))

    def contextMenuEvent(self, event):
        context_menu = QtWidgets.QMenu()
        # Создаем действия для контекстного меню
        action_edit = context_menu.addAction("Редактировать")
        action_delete = context_menu.addAction("Удалить")
        # Подключаем действия к слотам
        action_edit.triggered.connect(self.edit_polygon)
        action_delete.triggered.connect(self.delete_polygon)
        # Выполняем контекстное меню
        context_menu.exec(event.screenPos())

    def edit_polygon(self):
        # Логика для редактирования многоугольника

        print("Редактировать многоугольник")

    def delete_polygon(self):
        # Логика для удаления многоугольника
        print("Удалить многоугольник")
        self.scene().removeItem(self)
        del self





class Ui_MainWindow(object):
    def __init__(self):
        self.counter = {}  # Словарь для хранения счетчиков для каждого типа метки

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 639)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(600, 0, 191, 591))
        self.listWidget.setObjectName("listWidget")

        item1 = QtWidgets.QListWidgetItem("BOOL2BOOL")
        item2 = QtWidgets.QListWidgetItem("DWORD2DWORD")
        self.listWidget.addItem(item1)
        self.listWidget.addItem(item2)

        self.listWidget.itemPressed.connect(self.on_item_clicked)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 591, 591))
        self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtWidgets.QMenu(parent=self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSettings = QtWidgets.QAction(parent=MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.keyPressEvent = self.keyPressEvent  # Подключаем обработчик нажатий клавиш

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Delete:
            selected_items = self.scene.selectedItems()  # Получаем выбранные элементы
            for item in selected_items:
                if isinstance(item, MovablePolygon):  # Проверяем, является ли элемент многоугольником
                    self.scene.removeItem(item)  # Удаляем элемент из сцены
                    del item  # Освобождаем память




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuAdd.setTitle(_translate("MainWindow", "&Add"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSettings.setText(_translate("MainWindow", "S&ettings"))

    def on_item_clicked(self, item):
        label_text = item.text()
        if label_text not in self .counter:
            self.counter[label_text] = 0
        self.counter[label_text] += 1
        numbered_label = f"{label_text}_{self.counter[label_text]}"

        polygon = QtGui.QPolygonF([
            QtCore.QPointF(50, 50),
            QtCore.QPointF(150, 50),
            QtCore.QPointF(150, 75),
            QtCore.QPointF(137, 75),
            QtCore.QPointF(137, 125),
            QtCore.QPointF(150, 125),
            QtCore.QPointF(150, 150),
            QtCore.QPointF(50, 150),
            QtCore.QPointF(50, 125),
            QtCore.QPointF(63, 125),
            QtCore.QPointF(63, 75),
            QtCore.QPointF(50, 75)
        ])
        # Create a movable polygon item with a numbered label
        polygon_item = MovablePolygon(polygon, numbered_label)
        self.scene.addItem(polygon_item)






if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  # Используйте exec_() для PyQt5