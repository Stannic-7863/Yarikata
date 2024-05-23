from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


class Settings(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.setParent(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
