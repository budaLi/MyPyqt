# @Time    : 2019/11/18 9:47
# @Author  : Libuda
# @FileName: demo02-应用程序图标.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #设置窗口和大小
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("1.png"))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
