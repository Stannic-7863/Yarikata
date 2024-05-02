from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QCheckBox
)


class TaskCheckBoxWidget(QCheckBox):
    def __init__(self, task_name: str, task_id: int):
        self.task_name = task_name
        self.task_id = task_id
