import os
import sys
import torch

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication
from detect import run
from PyQt5.QtGui import QIcon


if torch.cuda.is_available():
    dev = '0'
else:
    dev = 'cpu'
run_dict = {
    'weights': 'kid.pt',
    'source': 0,
    'imgsz': [640, 640],
    'conf_thres': 0.60,
    'iou_thres': 0.40,
    'max_det': 10,
    'device': dev,
    'view_img': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': True,
    'classes': None,
    'agnostic_nms': False,
    'augment': False,
    'visualize': False,
    'update': False,
    'project': 'runs/detect',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    'half': False,
}

run_dict_file = {
    'weights': 'kid.pt',
    'source': 'data/images',
    'imgsz': [640, 640],
    'conf_thres': 0.60,
    'iou_thres': 0.40,
    'max_det': 10,
    'device': dev,
    'view_img': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': False,
    'classes': None,
    'agnostic_nms': False,
    'augment': False,
    'visualize': False,
    'update': False,
    'project': 'runs/detect',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    'half': False,
}

class WindowClass(QWidget):
    def __init__(self,parent=None):
        super(WindowClass, self).__init__(parent)
        self.setWindowTitle('口罩佩戴检测__by_Kid')
        self.setWindowIcon(QIcon('ico.jpg'))
        self.btn_1 = QPushButton("Start from Camera")
        self.btn_2 = QPushButton("Start from File")
        self.btn_3 = QPushButton("Show the Result")
        self.btn_4 = QPushButton("Exit")


        self.btn_1.setCheckable(True)
        self.btn_1.toggle()

        self.btn_1.clicked.connect(lambda :self.wichBtn(self.btn_1))
        self.btn_2.clicked.connect(lambda :self.wichBtn(self.btn_2))
        self.btn_3.clicked.connect(lambda :self.wichBtn(self.btn_3))
        self.btn_4.clicked.connect(lambda :self.wichBtn(self.btn_4))

        self.resize(300,300)
        layout=QVBoxLayout()
        layout.addWidget(self.btn_1)
        layout.addWidget(self.btn_2)
        layout.addWidget(self.btn_3)
        layout.addWidget(self.btn_4)

        self.setLayout(layout)


    def wichBtn(self,btn):
        print("The button clicked is：" , btn.text())
        if btn.text() == 'Exit':
            sys.exit()
        if btn.text() == 'Start from Camera':
            run(**run_dict)
        if btn.text() == 'Show the Result':
            path = os.getcwd() + r'\runs\detect'
            os.system("start explorer %s" %path)
        if btn.text() == 'Start from File':
            run(**run_dict_file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowClass()
    win.show()
    sys.exit(app.exec_())