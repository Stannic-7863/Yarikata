from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QTabWidget,
    QWidget
)

from modules.home import Home
from modules.pomodoro import Pomodoro


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_widget = QWidget()
        self.main_widget_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_widget_layout)

        self.navigation_bar = QTabWidget()

        self.navigation_bar.addTab(Home(), "Home")
        self.navigation_bar.addTab(Pomodoro(), "Pomodoro")

        self.main_widget_layout.addWidget(self.navigation_bar)

        self.setCentralWidget(self.main_widget)

        self.showMaximized()


if __name__ == "__main__":

    app = QApplication()
    main_window = Main()
    app.exec()
