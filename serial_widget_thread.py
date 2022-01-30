from portDialog import Ui_Dialog as port_dialog
import time
import threading



class read_thr(threading.Thread):
    def __init__(self, robot, portDialog):
        threading.Thread.__init__(self)
        self.isRunning = False
        self.robot = robot
        self.ser = robot.ser
        self.portDialog = portDialog
    
    def run(self):
        self.portDialog.recv_Text.clear()
        temp = b""
        cursor = self.portDialog.recv_Text.textCursor()
        pos = 0
        while self.ser.isOpen():
            if self.isRunning:
                self.portDialog.recv_Text.append("串口未打开")
                break
            self.robot.read_lock.acquire()
            text = self.ser.read()
            self.robot.read_lock.release()
            temp += text
            try:  # 解决汉字等二进制转换的问题
                text_ = temp.decode(encoding="utf-8")
                temp = b""
                self.portDialog.recv_Text.append(text_)
            except:
                pass
                # print("未能解码，保留继续", temp)
            
            if self.portDialog.AutoLast.isChecked():
                pos = len(self.portDialog.recv_Text.toPlainText())  # 获取文本尾部的位置
                cursor.setPosition(pos)  # 游标位置设置为尾部
                self.portDialog.recv_Text.setTextCursor(cursor)  # 滚动到游标位置    
        time.sleep(0.05)
        
