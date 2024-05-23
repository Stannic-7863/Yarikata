from PySide6.QtWidgets import (
    QWidget,
    QGridLayout
)


class Stats(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.setParent(parent)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
