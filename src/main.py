from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QTabWidget,
    QWidget
)

from PySide6.QtGui import (
    QIcon
)

from modules.home import Home
from modules.pomodoro import Pomodoro
from modules.stats import Stats
from modules.settings import Settings


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_widget = QWidget()
        self.main_widget_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_widget_layout)

        self.navigation_bar = QTabWidget(movable=True)
        self.navigation_bar.setTabPosition(QTabWidget.TabPosition.North)

        self.navigation_bar.addTab(
            Home(), QIcon.fromTheme("home"), "Home"
        )
        self.navigation_bar.addTab(
            Pomodoro(), QIcon.fromTheme("clock"), "Pomodoro"
        )
        self.navigation_bar.addTab(
            Stats(), QIcon.fromTheme("adjustcurves"), "Stats"
        )
        self.navigation_bar.addTab(
            Settings(), QIcon.fromTheme("settings-configure"), "Settings"
        )

        self.main_widget_layout.addWidget(self.navigation_bar)

        self.setCentralWidget(self.main_widget)

        self.showMaximized()


if __name__ == "__main__":

    app = QApplication()
    main_window = Main()
    app.exec()
