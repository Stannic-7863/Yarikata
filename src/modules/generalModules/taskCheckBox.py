from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QCheckBox,
    QLabel,
    QMenu,
    QToolButton,
    QPushButton,
    QSizePolicy,
    QApplication
)

from PySide6.QtGui import (
    QIcon,
    QAction,
    QKeyEvent
)

from PySide6.QtCore import (
    Qt
)


from modules.generalModules.taskData import TaskData


class TaskCheckBoxWidget(QWidget):
    def __init__(self, task_data: TaskData):
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.data = task_data

        self.setTaskName()
        self.setUpButtons()

    def setTaskName(self) -> None:
        self.task_name_label = QLabel(self)
        self.task_name_label.setText(self.data.task_name)
        self.task_name_label.setWordWrap(True)

        self.layout.addWidget(self.task_name_label)

    def setUpButtons(self) -> None:

        self.buttons_container = QWidget()
        self.buttons_container_layout = QHBoxLayout()
        self.buttons_container.setLayout(self.buttons_container_layout)
        self.buttons_container.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        self.menu_button = QToolButton()
        self.menu_button.setPopupMode(
            QToolButton.ToolButtonPopupMode.InstantPopup)
        self.menu_button.setIcon(QIcon.fromTheme("menu_new"))

        self.setUpMenu()

        self.delete_button = QPushButton(QIcon.fromTheme("delete"), "")
        self.delete_button.clicked.connect(lambda: self.deleteLater())
        self.delete_button.hide()

        self.buttons_container_layout.addWidget(self.delete_button)
        self.buttons_container_layout.addWidget(self.menu_button)

        self.layout.addWidget(self.buttons_container)

    def setUpMenu(self) -> None:
        self.main_menu = QMenu()

        self.change_priority_menu = QMenu("Change Priority")
        self.change_priority_hard_action = QAction("Hard")
        self.change_priority_mid_action = QAction("Mid")
        self.change_priority_low_action = QAction("Low")
        self.change_priority_menu.addActions(
            [self.change_priority_hard_action, self.change_priority_mid_action, self.change_priority_low_action])

        self.main_menu.addMenu(self.change_priority_menu)
        self.menu_button.setMenu(self.main_menu)

    def enterEvent(self, event) -> None:
        self.setFocus()

    def leaveEvent(self, event) -> None:
        self.toggleHiddenButtons(False)
        self.clearFocus()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Shift:
            self.toggleHiddenButtons(True)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Shift:
            self.toggleHiddenButtons(False)

    def toggleHiddenButtons(self, visible):
        self.delete_button.setVisible(visible)
