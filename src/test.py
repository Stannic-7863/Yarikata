
import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QBrush, QPen

class RoundedDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Rounded Dialog')
        self.setGeometry(100, 100, 300, 200)
        
        # Set the stylesheet for rounded corners and border
        self.setStyleSheet("""
            QDialog {
                background-color: white;
                border: 2px solid #5A5A5A;
                border-radius: 15px;
            }
        """)

        layout = QVBoxLayout()
        label = QLabel("This is a dialog with rounded corners.")
        layout.addWidget(label)

        button = QPushButton("Close")
        button.clicked.connect(self.close)
        layout.addWidget(button)

        self.setLayout(layout)

    def paintEvent(self, event):
        # Ensure the rounded corners
        path = QPainter(self)
        path.setRenderHint(QPainter.Antialiasing)
        path.setBrush(QBrush(Qt.white))
        path.setPen(QPen(Qt.transparent, 0))
        rect = self.rect()
        rect.adjust(1, 1, -1, -1)
        path.drawRoundedRect(rect, 15, 15)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = RoundedDialog()
    dialog.show()
    sys.exit(app.exec_())

