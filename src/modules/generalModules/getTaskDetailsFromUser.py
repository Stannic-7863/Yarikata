from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QPlainTextEdit,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QDialogButtonBox,
    QRadioButton,
    QButtonGroup,
    QFrame,
)


from PySide6.QtCore import (
    Qt
)

from modules.defaults.app_settings import CONFIG

from modules.generalModules.taskData import TaskData


class GetTaskDetailsDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.window_frame = QFrame(parent=self)
        self.window_frame.setObjectName("window_frame")
        self.window_frame_layout = QVBoxLayout()
        self.window_frame.setLayout(self.window_frame_layout)
        self.layout.addWidget(self.window_frame)

        self.setUpTaskNameInputFeild()
        self.setUpPriorityRadioButtons()
        self.setUpButtons()
        self.addWidgetsToMainLayout()
        self.styleSheetSet()

    def setUpTaskNameInputFeild(self) -> None:
        self.task_name_plain_text = QPlainTextEdit()
        self.task_name_plain_text.setPlaceholderText("Task Name")
        self.task_name_plain_text.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.WidgetWidth)

    def setUpPriorityRadioButtons(self) -> None:
        self.priority_button_container = QWidget()
        self.priority_button_container_layout = QHBoxLayout()
        self.priority_button_container.setLayout(
            self.priority_button_container_layout)

        self.priority_button_group = QButtonGroup()

        self.high_priority_button = QRadioButton("High Priority")
        self.mid_priority_button = QRadioButton("Middle Priority")
        self.low_prioirty_button = QRadioButton("Low Priority")

        self.priority_button_group.addButton(self.high_priority_button)
        self.priority_button_group.addButton(self.mid_priority_button)
        self.priority_button_group.addButton(self.low_prioirty_button)

        self.priority_button_container_layout.addWidget(
            self.high_priority_button)
        self.priority_button_container_layout.addWidget(
            self.mid_priority_button)
        self.priority_button_container_layout.addWidget(
            self.low_prioirty_button)

    def setUpButtons(self) -> None:
        self.buttons = QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Save

        self.button_box = QDialogButtonBox(self.buttons)

        self.button_box.accepted.connect(self.on_accept)
        self.button_box.rejected.connect(self.reject)

    def addWidgetsToMainLayout(self) -> None:
        self.window_frame_layout.addWidget(self.task_name_plain_text)
        self.window_frame_layout.addWidget(self.priority_button_container)
        self.window_frame_layout.addWidget(self.button_box)

    def getTaskData(self) -> str:
        data = TaskData(self.task_name_plain_text.toPlainText(), 1, 0, 0)
        return data

    def on_accept(self):
        if self.task_name_plain_text.toPlainText().strip():
            self.accept()
            return True
        else:
            self.reject()

    def styleSheetSet(self) -> None:
        self.setStyleSheet(f"""
            QDialog {{
                background-color : {CONFIG.global_background_color};
                border : {CONFIG.global_border_thickness}px {CONFIG.global_border_type} {CONFIG.global_border_color};
                border-radius : {CONFIG.dialogbox_border_roundness}px;
                color : {CONFIG.global_font_color};
            }}

            #window_frame {{
                border : {CONFIG.global_border_thickness}px {CONFIG.global_border_type} {CONFIG.global_border_color};
                border-radius : {CONFIG.dialogbox_border_roundness}px;
            }}
        """)
