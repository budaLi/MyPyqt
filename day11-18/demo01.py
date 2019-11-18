# @Time    : 2019/11/18 9:39
# @Author  : Libuda
# @FileName: demo01.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w= QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle("Simple")
    w.show()


    #不写会导致窗口闪退
    sys.exit(app.exec_())