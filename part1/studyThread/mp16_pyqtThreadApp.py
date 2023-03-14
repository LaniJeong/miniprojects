# 스레드 사용 앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

class BackgroundWorker(QThread):     # PyQt5 스레드를 위한 클래스 존재
    procChanged = pyqtSignal(str)

    def __init__(self, count=0, parent=None) -> None:
        super().__init__()
        self.main = parent
        self.working = True         # 스레드 동작여부
        self.count = count

    def run(self):
        # self.parent.pgbTask.setRange(0, 100)
        # for i in range(0, 101):
        #     print(f'스레드 출력 > {i}')
        #     self.parent.pgbTask.setValue(i)
        #     self.parent.txblog.append(f'스레드 출력 > {i}')
        while self.working:
            self.procChanged.emit(f'스레드 출력 > {self.count}')
            self.count += 1     # 값 증가만

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyThread/threadApp.ui', self)
        self.setWindowTitle('스레드앱')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)
        # 쓰레드 초기화
        self.worker = BackgroundWorker(parent=self, count=0)
        # 백그라운드 워커에 있는 시그널 접근 함수
        self.worker.procChanged.connect(self.procUpdated)
        self.pgbTask.setRange(0, 100000)

    @pyqtSlot(int)
    def procUpdated(self, count):
        self.txblog.append(f'스레드 출력 > {count}')
        self.pgbTask.setValue(count)
        print(f'스레드 출력 > {count}')
    
    @pyqtSlot()
    def btnStartClicked(self):
        self.worker.start()
        self.worker.working = True

    def btnStartClicked(self):
        th = BackgroundWorker(self)
        th.start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())