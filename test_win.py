from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from instr import (
    txt_title,
    win_width,
    win_height,
    txt_starttest1,
    txt_starttest2,
    txt_starttest3,
    txt_hintname,
    txt_hintage,
    txt_hinttest1,
    txt_hinttest2,
    txt_hinttest3,
    txt_name,
    txt_age,
    txt_test1,
    txt_test2,
    txt_test3,
    btn_width,
    btn_height,
    input_height,
    input_width
)

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_ui()
        self.connect_events()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def init_ui(self):
        # buttons
        self.first_btn = QPushButton(txt_starttest1)
        self.second_btn = QPushButton(txt_starttest2)
        self.third_btn = QPushButton(txt_starttest3)
        self.send_result_btn =  QPushButton("Send the result")

        self.first_btn.setFixedSize(btn_width, btn_height)
        self.second_btn.setFixedSize(btn_width, btn_height)
        self.third_btn.setFixedSize(btn_width, btn_height)
        self.send_result_btn.setFixedSize(btn_width, btn_height)

        # line edits
        self.fullname_input = QLineEdit(txt_hintname)
        self.age_input = QLineEdit(txt_hintage)
        self.test1_input = QLineEdit(txt_hinttest1)
        self.test2_input = QLineEdit(txt_hinttest2)
        self.test3_input = QLineEdit(txt_hinttest3)

        self.fullname_input.setFixedSize(input_width, input_height)
        self.age_input.setFixedSize(input_width, input_height)
        self.test1_input.setFixedSize(input_width, input_height)
        self.test2_input.setFixedSize(input_width, input_height)
        self.test3_input.setFixedSize(input_width, input_height)

        # labels
        self.fullname_lb = QLabel(txt_name)
        self.age_lb = QLabel(txt_age)
        self.test1_lb = QLabel(txt_test1)
        self.test2_lb = QLabel(txt_test2)
        self.test3_lb = QLabel(txt_test3)

        # Handle timer UI
        self.timer_lb = QLabel('00:00:00')
        font = QFont("Arial", 32)
        self.timer_lb.setFont(font)

        # layouts
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.fullname_lb)
        vLayout.addWidget(self.fullname_input)

        vLayout.addWidget(self.age_lb)
        vLayout.addWidget(self.age_input)

        vLayout.addWidget(self.test1_lb)
        vLayout.addWidget(self.first_btn)
        vLayout.addWidget(self.test1_input)
        
        vLayout.addWidget(self.test2_lb)
        vLayout.addWidget(self.second_btn)

        vLayout.addWidget(self.test3_lb)
        vLayout.addWidget(self.third_btn)
        vLayout.addWidget(self.test3_input) 

        vLayout.addWidget(self.send_result_btn, alignment = Qt.AlignCenter)

        # set timer layout
        v2Layout = QVBoxLayout()
        v2Layout.addWidget(self.timer_lb)

        hLayout = QHBoxLayout()
        hLayout.addLayout(vLayout)
        hLayout.addLayout(v2Layout)
        
        self.setLayout(hLayout)

    def connect_events(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    test = TestWin()
    test.show()
    app.exec()

