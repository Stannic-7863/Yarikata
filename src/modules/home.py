from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QSizePolicy
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
    def __init__(self, parent) -> None:
        super().__init__()

        self.setParent(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setUpButtons()
        self.addWidgetsToMainLayout()

    def setUpButtons(self) -> None:

        self.button_container = QWidget()
        self.button_container_layout = QHBoxLayout()
        self.button_container.setLayout(self.button_container_layout)
        self.button_container.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        self.add_button = QPushButton(QIcon.fromTheme("im-irc"), "", self)
        self.add_button.setStatusTip("Add a new task")
        self.add_button.setToolTip("Add a new task")
        self.add_button.clicked.connect(self.onAddButtonTrigger)

        self.button_container_layout.addWidget(self.add_button)

    def addWidgetsToMainLayout(self) -> None:

        self.layout.addWidget(self.button_container, Qt.AlignmentFlag.AlignTop)
        self.layout.addStretch()

    def onAddButtonTrigger(self) -> None:
        print("Task Add Button Clicked")

        dialog = GetTaskDetailsDialog()

        if dialog.exec():
            data = dialog.getTaskData()
            print(f"Task Name : {data.task_name}")

            self.layout.insertWidget(1, TaskCheckBoxWidget(data))

        else:
            print("Action cancelled")
