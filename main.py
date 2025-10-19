from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from PyQt5.QtCore import Qt

from instr import (
    txt_title,
    win_width,
    win_height,
    txt_hello,
    txt_instruction,
    txt_next,
    btn_width,
    btn_height
)

from test_win import TestWin



class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.set_appear()
        self.init_ui()
        self.connect_events()
        self.test_win = TestWin()
    
    def set_appear(self):
        # setting window appearance 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def init_ui(self):
        # create widgets
        self.welcome_msg = QLabel(txt_hello)
        self.instr = QLabel(txt_instruction)
        self.start_btn = QPushButton(txt_next)
        self.start_btn.setFixedSize(btn_width, btn_height)
        
        # set layout
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.welcome_msg)
        vLayout.addWidget(self.instr)
        vLayout.addWidget(self.start_btn, alignment = Qt.AlignCenter)

        self.setLayout(vLayout)
    
    def switch_next_screen(self):
        self.hide()
        self.test_win.show()

    def connect_events(self):
        self.start_btn.clicked.connect(self.switch_next_screen)

if __name__ == "__main__":
    app = QApplication([])
    main = Main()
    main.show()
    app.exec()