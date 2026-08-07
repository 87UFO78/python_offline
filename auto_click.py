import sys
from pathlib import Path
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.click = False
        self.a = ""
        self.b = ""
        
        self.setWindowTitle("報工系統")
        self.setFixedSize(350, 350)

        # 外層：TextEdit 與按鈕區水平排列
        main_layout = QHBoxLayout()

        self.input_box = QTextEdit(self)
        self.input_box.setPlaceholderText("請在此輸入文字...")
        self.input_box.setFixedWidth(150)
        main_layout.addWidget(self.input_box)

        # 按鈕區：四個按鈕垂直排列
        button_layout = QVBoxLayout()

        self.start_button = QPushButton("開始報工", self)
        self.start_button.clicked.connect(self.get_input_text)
        button_layout.addWidget(self.start_button)

        self.a_button = QPushButton("修改 A", self)
        self.a_button.clicked.connect(lambda: self.set_value("a"))
        button_layout.addWidget(self.a_button)

        self.b_button = QPushButton("修改 B", self)
        self.b_button.clicked.connect(lambda: self.set_value("b"))
        button_layout.addWidget(self.b_button)

        self.c_button = QPushButton("修改 C", self)
        self.c_button.clicked.connect(lambda: self.set_value("c"))
        button_layout.addWidget(self.c_button)

        self.label = QLabel("未選擇工號", self)
        button_layout.addWidget(self.label)

        # 讓按鈕靠上排列
        button_layout.addStretch()

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def set_value(self, variable_name):
        text = self.input_box.toPlainText()

        if variable_name == "a":
            self.a = "123456"
            self.b = "654321"
            self.label.setText(f"報工帳號已切換成: {self.a}")
            self.click = True
        elif variable_name == "b":
            self.a = "111111"
            self.b = "222222"
            self.label.setText(f"報工帳號已切換成: {self.a}")
            self.click = True
        elif variable_name == "c":
            self.a = "333333"
            self.b = "444444"
            self.label.setText(f"報工帳號已切換成: {self.a}")
            self.click = True

    def get_input_text(self):
        if not self.click:
            self.label.setText("請先選擇工號")
            return

def resource_path(filename):
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / filename

if __name__ == "__main__":
    # 必須先建立 QApplication
    app = QApplication(sys.argv)

    icon_path = resource_path("icon.ico")
    icon = QIcon(str(icon_path))

    app.setWindowIcon(icon)

    window = MainWindow()
    window.setWindowIcon(icon)
    window.show()

    sys.exit(app.exec())
