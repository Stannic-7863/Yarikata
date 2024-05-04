from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QPlainTextEdit,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QDialogButtonBox
)

from PySide6.QtCore import (
    Qt
)


class GetTaskDetailsDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setUpTaskNameInputFeild()
        self.setUpButtons()
        self.addWidgetsToMainLayout()

    def setUpTaskNameInputFeild(self) -> None:
        self.input_feild_task_name = QPlainTextEdit()
        self.input_feild_task_name.setPlaceholderText("Task Name")
        self.input_feild_task_name.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.WidgetWidth)

    def setUpButtons(self) -> None:
        self.buttons = QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Save

        self.button_box = QDialogButtonBox(self.buttons)

        self.button_box.accepted.connect(self.on_accept)
        self.button_box.rejected.connect(self.reject)

    def addWidgetsToMainLayout(self) -> None:
        self.layout.addWidget(self.input_feild_task_name)
        self.layout.addWidget(self.button_box)

    def getTaskData(self) -> str:
        return self.input_feild_task_name.toPlainText().strip()

    def on_accept(self):
        if self.input_feild_task_name.toPlainText().strip():
            self.accept()
            return True
        else:
            self.reject()
