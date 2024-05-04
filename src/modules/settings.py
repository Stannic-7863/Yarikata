from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


class Settings(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
