import serial
import serial.tools.list_ports
import struct
import time

class Robot():
    def __init__(self, COM_num=None, lock=None):
        self.lock = lock
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.timeout = 5
        if COM_num is not None:
            self.ser.port = COM_num
            self.ser.open()
            self.position = self.get_position()
        else:
            self.ser.port = None
            self.position = None

        self.spd_now = 0
        self.port_list = []

    def get_position(self):
        '''查询电机位置信息'''
        if self.lock is not None:
            self.lock.acquire()
        self.ser.read_all()
        msg = b"?\r\n"
        self.ser.write(msg)
        a = self.ser.read()
        buffer = None
        for _ in range(1024):
            b = self.ser.read()
            if a == b":" and b == b":":
                buffer = self.ser.read(16)
                break
            else:
                a = b
        if self.lock is not None:
            self.lock.release()
        if buffer is not None:
            x, y = struct.unpack("2q", buffer)
            x = x / 100000 * 1.875
            y = y / 100000 * 1.875
        else:
            x, y = None, None
        return (x, y)

    def set_speed_freq(self, id, freq):
        """设置步进电机的速度"""
        msg = f":{id} {int(freq)}\r\n".encode()
        if self.lock is not None:
            self.lock.acquire()
        if self.ser.isOpen():
            self.ser.write(msg)
        if self.lock is not None:
            self.lock.release()
    
    def set_speed(self, id):
        pass
    
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
        self.ser.open()
    
    def close_robot_port(self):
        """关闭机器人串口"""
        if self.ser.isOpen():
            self.ser.close()

if __name__ == "__main__":
    pass