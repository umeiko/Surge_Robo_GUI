import time
import threading
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QTextCursor

class jump_worker(QObject):
    jump_sig  = Signal(QTextCursor)
    send_char_sig = Signal(str, bool)
    erro_sig  = Signal()
    speed_sig = Signal(float, float, float)
    def sendCursor(self, Cursor):
        self.jump_sig.emit(Cursor)
    def sendChar(self, char, mode):
        self.send_char_sig.emit(char, mode)


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
                try:
                    text = self.ser.read()
                except:
                    self.worker.erro_sig.emit()
                self.robot.read_lock.release()
                
                if text:
                    temp += text
                    try:  # 解决汉字等二进制转换的问题
                        decode_str = temp.decode(encoding="utf-8")
                        for k, i in enumerate(decode_str):
                            if i in "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0e\x0f":
                                decode_str = decode_str[:k] + "\\x" + temp[k:k+1].hex() + decode_str[k+1:]
                        self.worker.sendChar(decode_str, False)
                        temp = b""
                    except BaseException as e:
                        msg = str(e).split(":")[-1]
                        if msg == " unexpected end of data":
                            if len(temp) >3:
                                decode_str = ""
                                for k, _ in enumerate(temp):
                                    decode_str += "\\x" + temp[k:k+1].hex()
                                self.worker.sendChar(decode_str, False)
                                temp = b""
                        else:
                            decode_str = ""
                            for k, _ in enumerate(temp):
                                decode_str += "\\x" + temp[k:k+1].hex()
                            self.worker.sendChar(decode_str, False)
                            temp = b""
                    self.jump_to_last_line()               
            time.sleep(0.001)
        print("串口打印线程被终止")


class msg_fresh_thr(threading.Thread):
    def __init__(self, robot):
        threading.Thread.__init__(self)
        self.ser = robot.ser
        self.worker = jump_worker()
        self.is_running = True
    
    def run(self):
        while self.is_running:
            pass
