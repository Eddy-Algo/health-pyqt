from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton
)

from instr import (
    txt_title,
    win_width,
    win_height,
    btn_width, btn_height
)


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_ui()
        self.connect_events()

    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
    
    def init_ui(self):
        self.ruffier_index_lb = QLabel("Ruffier index:")
        self.performance_lb = QLabel("This is where we display your performance")
        self.reset_btn = QPushButton("Start over")
        
        self.reset_btn.setFixedSize(btn_width, btn_height)

        vLayout = QVBoxLayout()
        vLayout.addWidget(self.ruffier_index_lb, alignment = Qt.AlignCenter)
        vLayout.addWidget(self.performance_lb, alignment = Qt.AlignCenter)
        vLayout.addWidget(self.reset_btn, alignment = Qt.AlignCenter)
        
        self.setLayout(vLayout)

    def connect_events(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    test = FinalWin()
    test.show()
    app.exec()
    