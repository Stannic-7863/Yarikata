from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QToolBar
)

from PySide6.QtGui import (
    QIcon,
    QAction
)

from PySide6.QtCore import (
    Qt,
    QSize
)

from modules.generalModules.getTaskDetailsFromUser import GetTaskDetailsDialog
from modules.generalModules.taskCheckBox import TaskCheckBoxWidget


class Home(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setUpButtons()
        self.addWidgetsToMainLayout()

    def setUpButtons(self) -> None:

        self.button_container = QToolBar("Home Toolbar")

        self.add_button = QAction(QIcon.fromTheme("im-irc"), "", self)
        self.add_button.setStatusTip("Add a new task")
        self.add_button.setToolTip("Add a new task")
        self.add_button.triggered.connect(self.onAddButtonTrigger)

        self.button_container.addAction(self.add_button)

    def addWidgetsToMainLayout(self) -> None:

        self.layout.addWidget(self.button_container, Qt.AlignmentFlag.AlignTop)
        self.layout.addStretch()

    def onAddButtonTrigger(self) -> None:
        print("Task Add Button Clicked")

        dialog = GetTaskDetailsDialog()
        dialog.setWindowTitle("Add a new task")

        if dialog.exec():
            print(f"Task Name : {dialog.getTaskData()}")

            self.layout.insertWidget(1, TaskCheckBoxWidget(dialog.getTaskData(), 1))

        else:
            print("Action cancelled")
