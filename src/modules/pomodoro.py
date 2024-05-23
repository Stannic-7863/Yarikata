from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


class Pomodoro(QWidget):
    def __init__(self, parent) -> None:
        super().__init__()

        self.setParent(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
