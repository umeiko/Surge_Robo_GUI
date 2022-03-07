import time
import threading
import asyncio
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QTextCursor

class jump_worker(QObject):
    """一个提供信号的"""
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
    '''该线程通过异步的方式同时处理【获取位置信息】和【执行单步运行】'''
    def __init__(self, robot):
        threading.Thread.__init__(self)
        self.robot = robot
        self.worker = jump_worker()
        self.isRunning = True
        self.lock = threading.Lock()
        self.stepsQueues = [[],[],[]]
        self.pause = False
        
    def addStep(self, id, spd, delay_time):
        '''添加一个【单步前进】任务，输入电机号，单步速度与单步时间'''
        self.lock.acquire()
        self.stepsQueues[id].append((spd, delay_time))
        self.lock.release()
    
    def clearMissons(self):
        """清空队列中的所有待执行【单步前进】任务"""
        self.lock.acquire()
        [i.clear() for i in self.stepsQueues]
        self.lock.release()

    async def runStep(self, id, spd, delay_time):
        '''一个执行机器人单步运动的异步函数'''
        self.robot.set_speed(id, spd)
        await asyncio.sleep(delay_time)
        self.robot.set_speed(id, 0)
    
    def getMsg(self):
        '''实现【获取速度信息】的功能'''
        x, y, z = self.robot.get_position()
        return x, y, z

    async def loopStepRunner(self, id):
        '''异步循环检查是否有需要运行的【单步指令队列】'''
        while self.isRunning:
            if self.stepsQueues[id] and not self.pause:
                await self.runStep(id, *self.stepsQueues[id][0])
                self.lock.acquire()
                self.stepsQueues[id].pop(0)
                self.lock.release()
            await asyncio.sleep(0.001)
    
    async def loopGetMsgRunner(self, freq=2):
        '''异步循环地获取并刷新界面'''
        while self.isRunning:
            if not self.pause:
                x, y, z = self.getMsg()
                self.worker.speed_sig.emit(x, y, z)
            await asyncio.sleep(1/freq)

    async def mainLoop(self):
        '''异步应用的入口'''
        await asyncio.gather(
            self.loopGetMsgRunner(),
            self.loopStepRunner(0),
            self.loopStepRunner(1),
            self.loopStepRunner(2),
            )
        
    def run(self):
        asyncio.run(self.mainLoop())

if __name__ == "__main__":
    pass