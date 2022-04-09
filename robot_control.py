import serial
import serial.tools.list_ports
import struct
import threading
from PySide6.QtCore import Signal, QObject
import numpy as np

class Robot(QObject):
    spd_signal = Signal(int, float)  # id, spd
    port_erro_signal = Signal(str)
    def __init__(self,COM_num=None):
        super(Robot, self).__init__()
        self.read_lock = threading.Lock()
        self.write_lock = threading.Lock()
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.timeout = 0.005
        self.gear_level  = 0.2
        self.flags = [False, False, False] #禁止标志位
        if COM_num is not None:
            self.ser.port = COM_num
            self.ser.open()
            self.position = self.get_position()
        else:
            self.ser.port = None
            self.position = None

    def get_position(self):
        '''查询电机位置信息'''
        buffer = None
        if self.ser.isOpen():
            self.read_lock.acquire()
            self.write_lock.acquire()
            try:
                self.ser.read_all()
                msg = b"?\r\n"
                self.ser.write(msg)
                a = self.ser.read()
                for _ in range(25):
                    b = self.ser.read()
                    if a == b":" and b == b":":
                        buffer = self.ser.read(24)
                        break
                    else:
                        a = b
            except BaseException as e:
                self.port_erro_signal.emit(str(e))
            self.read_lock.release()
            self.write_lock.release()
        
        x, y, z = None, None, None
        if buffer is not None:
            try:
                x, y, z = struct.unpack("3q", buffer)
                x = x  / 6400* 10.715
                y = y / 360 * 8 * np.pi + x
                z = (z / 9000 * 360) % 360
            except:
                pass
        return (x, y, z)

    def set_speed_freq(self, id, freq):
        """设置步进电机的驱动频率"""
        msg = f":{id} {round(freq, 2)}\r\n".encode()
        if self.ser.isOpen():
            self.write_lock.acquire()
            try:
                self.ser.write(msg)
            except BaseException as e:
                self.port_erro_signal.emit(str(e))
            self.write_lock.release()
        else:
            print(msg)
    
    def set_speed(self, id, spd, is_geared=True):
        """设置某一轴的速度"""
        
        if is_geared:
            spd = self.gear_level * spd
        if self.flags[id]:    
          self.spd_signal.emit(id, spd)
          self.set_speed_freq(id, spd)
        else:
          self.spd_signal.emit(id, 0)  
          self.set_speed_freq(id, 0)   

    
    def scan_ports(self):
        """查询有哪些串口可用，返回一个列表"""
        options = serial.tools.list_ports.comports()
        ports = [i.device for i in options]
        names = [i.description for i in options]
        return ports, names
    
    def open_robot_port(self, port):
        """在输入的串口号上打开机器人通讯"""
        if (self.ser.isOpen() and port != self.ser.port):
            self.read_lock.acquire()
            self.write_lock.acquire()            
            self.ser.close()
            self.read_lock.release()
            self.write_lock.release() 
        self.ser.port = port
        
        if not self.ser.isOpen():
            try:
                self.ser.open()
            except BaseException as e:
                self.port_erro_signal.emit(str(e))
    
    def close_robot_port(self):
        """关闭机器人串口"""
        self.read_lock.acquire()
        self.write_lock.acquire()
        if self.ser.isOpen():
            self.ser.close()
        self.read_lock.release()
        self.write_lock.release()
    
    def plus_gear_level(self):
        """加快机器人的速度"""
        self.gear_level += 0.2
        if self.gear_level > 1:
            self.gear_level = 1
        return self.gear_level
    
    def minus_gear_level(self):
        """降低机器人的速度"""
        self.gear_level -= 0.2
        if self.gear_level < 0.2:
            self.gear_level = 0.2
        return self.gear_level
    
    def write_ser(self, content):
        """直接写内容到机器人的串口"""
        if isinstance(content, bytes):
            content = content
        elif isinstance(content, str):
            content = content.encode()
        else:
            return False
        if self.ser.isOpen():
            self.write_lock.acquire()
            try:
                self.ser.write(content)
            except BaseException as e:
                self.port_erro_signal.emit(str(e))
            self.write_lock.release()
            return True
        else:
            return False
    
    def all_stop(self):
        """停止所有的电机运动"""
        for i in range(3):
            self.set_speed_freq(i,0)
            self.spd_signal.emit(i, 0)
    
    def flush_ser(self):
        """清除串口缓冲区的内容"""
        if self.ser.isOpen():
            self.read_lock.acquire()
            try:
                self.ser.read_all()
            except BaseException as e:
                self.port_erro_signal.emit(str(e))
            self.read_lock.release()
    
    def change_disable_state(self, id, state):
        """更改介入器械的锁定-启用状态"""
        pass
            
        
if __name__ == "__main__":
    pass