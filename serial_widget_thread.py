import time
import threading
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QTextCursor

class jump_worker(QObject):
    jump_sig  = Signal(QTextCursor)
    send_char_sig = Signal(str)
    def sendCursor(self, Cursor):
        self.jump_sig.emit(Cursor)
    def sendChar(self, char):
        self.send_char_sig.emit(char)


class read_thr(threading.Thread):
    """串口调试助手的收信线程"""
    def __init__(self, robot, portDialog):
        threading.Thread.__init__(self)
        self.isRunning = False
        self.show  = False
        self.robot = robot
        self.ser = robot.ser
        self.worker = jump_worker()
        self.portDialog = portDialog
        self.cursor = portDialog.recv_Text.textCursor()
    
    def jump_to_last_line(self):
        if self.portDialog.AutoLast.isChecked():
            try:
                self.worker.sendCursor(self.cursor)
            except:
                pass
    
    def run(self):
        temp = b""
        self.isRunning = True
        
        while self.isRunning:
            if self.ser.isOpen() and self.show:
                self.robot.read_lock.acquire()
                text = self.ser.read()
                self.robot.read_lock.release()
                if text:
                    temp += text
                    try:  # 解决汉字等二进制转换的问题
                        text_ = temp.decode(encoding="utf-8")
                        temp = b""
                        self.worker.sendChar(text_)
                    except:
                        pass
                    self.jump_to_last_line()
                       
            time.sleep(0.001)
        print("串口打印线程被终止")


