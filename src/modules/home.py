from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


class Home(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
