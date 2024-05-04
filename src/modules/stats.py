from PySide6.QtWidgets import (
    QWidget,
    QGridLayout
)


class Stats(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)
