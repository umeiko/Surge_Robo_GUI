import time
import threading



class read_thr(threading.Thread):
    """串口调试助手的收信线程"""
    def __init__(self, robot, portDialog):
        threading.Thread.__init__(self)
        self.isRunning = False
        self.show  = False
        self.robot = robot
        self.ser = robot.ser
        self.portDialog = portDialog
        self.cursor = self.portDialog.recv_Text.textCursor()
    
    def jump_to_last_line(self):
        if self.portDialog.AutoLast.isChecked():
            try:
                self.portDialog.recv_Text.setTextCursor(self.cursor)  # 滚动到游标位置
            except:
                pass

    
    def run(self):
        self.portDialog.recv_Text.clear()
        temp = b""
        self.isRunning = True
        
        while self.isRunning:
            if self.ser.isOpen() and self.show:
                self.robot.read_lock.acquire()
                text = self.ser.read()
                self.robot.read_lock.release()
                temp += text
                try:  # 解决汉字等二进制转换的问题
                    text_ = temp.decode(encoding="utf-8")
                    temp = b""
                    self.cursor.insertText(text_)
                except:
                    pass
                
                self.jump_to_last_line()
                       
            time.sleep(0.001)
        print("串口打印线程被终止")


