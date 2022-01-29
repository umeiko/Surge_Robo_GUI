from pickle import NONE
import serial
import serial.tools.list_ports
import struct
import threading
import time


class Robot():
    def __init__(self,COM_num=None, main_window=None):
        self.read_lock = threading.Lock()
        self.write_lock = threading.Lock()
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.timeout = 5
        self.gear_level  = 0.2
        if COM_num is not None:
            self.ser.port = COM_num
            self.ser.open()
            self.position = self.get_position()
        else:
            self.ser.port = None
            self.position = None
        self.main_window = main_window
        self.port_list = []

    def get_position(self):
        '''查询电机位置信息'''
        buffer = None
        if self.ser.isOpen:
            self.read_lock.acquire()
            self.write_lock.acquire()
            self.ser.read_all()
            msg = b"?\r\n"
            self.ser.write(msg)
            
            a = self.ser.read()
            for _ in range(1024):
                b = self.ser.read()
                if a == b":" and b == b":":
                    buffer = self.ser.read(16)
                    break
                else:
                    a = b
            self.read_lock.release()
            self.write_lock.release()
        if buffer is not None:
            x, y = struct.unpack("2q", buffer)
            x = x / 100000 * 1.875
            y = y / 100000 * 1.875
        else:
            x, y = None, None
        return (x, y)

    def set_speed_freq(self, id, freq):
        """设置步进电机的速度"""
        freq = self.gear_level * freq
        if self.main_window is not None:
            self.main_window.speed_UI_list[id].display(freq)
        msg = f":{id} {round(freq, 2)}\r\n".encode()
        if self.ser.isOpen():
            self.write_lock.acquire()
            self.ser.write(msg)
            self.write_lock.release()
        else:
            print(msg)
    
    def set_speed(self, id, spd):
        self.set_speed_freq(id, spd)
    
    def scan_ports(self):
        """查询有哪些串口可用，返回一个列表"""
        options = serial.tools.list_ports.comports()
        ports = [i.device for i in options]
        names = [i.description for i in options]
        self.port_list = ports
        return ports, names
    
    def open_robot_port(self, port):
        """在输入的串口号上打开机器人通讯"""
        if (self.ser.isOpen() and port != self.ser.port):
            self.ser.close()
        self.ser.port = port
        if not self.ser.isOpen():
            self.ser.open()
    
    def close_robot_port(self):
        """关闭机器人串口"""
        if self.ser.isOpen():
            self.ser.close()
    
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
    



if __name__ == "__main__":
    pass