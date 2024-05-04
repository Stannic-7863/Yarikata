from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QCheckBox,
    QLabel
)

from PySide6.QtGui import (
    QPalette
)

from PySide6.QtCore import (
    Qt
)


class TaskCheckBoxWidget(QWidget):
    def __init__(self, task_name: str, task_id: int):
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.task_name: str = task_name
        self.task_id: int = task_id

        self.setTaskName()

    def setTaskName(self) -> None:
        self.task_name_label = QLabel(self)
        self.task_name_label.setText(self.task_name)
        self.task_name_label.setWordWrap(True)

        self.layout.addWidget(self.task_name_label)

    def enterEvent(self, event) -> None:
        self.setStyleSheet(f"background : #f23f23;")

    def leaveEvent(self, event) -> None:
        self.setStyleSheet("")
