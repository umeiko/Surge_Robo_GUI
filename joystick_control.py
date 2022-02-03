from signal import Signals
import pygame
from pygame import joystick
import threading
from PySide6.QtCore import Signal, QObject
# 导入依赖
import time



pygame.init()
joystick.init()


joy_config = {
    "default" : {
        "axis"      : [(0, 1, -1, 1, -3600, 3600),
                       (1, 3, -1, 1, -3600, 3600),
                       (2, 4, -1, 1, 0, -3600),
                       (2, 5, -1, 1, 0, 3600),
                      ],
        "button"   : [(6, "plus_gaer"), (7, "minus_gear")],
    }
}

def save_options():
    """导出配置到文件中"""
    import json as json
    with open("joy_config.json", 'w') as js_file:
        js_string = json.dumps(joy_config, sort_keys=True, indent=4, separators=(',', ': '))
        js_file.write(js_string)

def load_options():
    """从文件中加载配置"""
    global joy_config
    import json as json
    with open("joy_config.json", 'r') as js_file:
        temp_robo_options = json.load(js_file)
        joy_config = temp_robo_options


def plus_gaer(robot, widget):
    level_value = robot.plus_gear_level()
    level_value = int(level_value * 5)
    widget.setValue(level_value)

def minus_gaer(robot, widget):
    level_value = robot.minus_gear_level()
    level_value = int(level_value * 5)
    widget.setValue(level_value)


def spd_map_func(map_in=[-1,1], map_out=[-3600, 3600]):
    """将速度从区间a线性映射到区间b，返回函数的斜率k和偏置b"""
    k = (map_out[1] - map_out[0]) / (map_in[1] - map_in[0])
    b = (map_out[0] - k*map_in[0])
    return k, b

def spd_map_func_(maps=[-1, 1, -3600, 3600]):
    """将速度从区间a线性映射到区间b，返回函数的斜率k和偏置b"""
    k = (maps[3] - maps[2]) / (maps[1] - maps[0])
    b = (maps[2] - k*maps[0])
    return k, b

def axis_shift_cancelling(axis_value, fix_value=0.05):
    """消除轴的零漂"""
    if fix_value > axis_value  > -fix_value:
        axis_value  = 0
    elif -1. < axis_value  < -1 + fix_value:
        axis_value  = -1
    elif 1. > axis_value  > 1 - fix_value:
        axis_value  = 1
    return axis_value


class joystick_manager():
    def __init__(self, robot, main_window) -> None:
        self.joy = None
        self.thread = None
        self.main_window = main_window
        self.robot = robot
        self.signals = Signal_Worker()
        pass
    
    def start_joystick(self, id):
        """开始手柄线程"""
        if self.thread is not None:
            self.thread.isRunning = False
            del self.joy
        self.joy = joystick.Joystick(id)
        self.thread = thread_joystick(self.joy, self.robot, self.main_window)
        self.config_joystick()
        self.thread.start()
    
    def close_joystick(self):
        """关闭手柄线程"""
        if self.thread is not None:
            self.thread.isRunning = False
            del self.joy
            self.thread = None
    
    def scan_joystick(self):
        """扫描连接到系统上的手柄"""
        joy_names = [joystick.Joystick(i).get_name() for i in range(joystick.get_count())]
        return joy_names

    def config_joystick(self):
        moto_axes = [[], [], [], [], []]
        for i in joy_config["default"]["axis"]:
            moto_axes[i[0]].append(i)

        for k, i in enumerate(moto_axes):
            if len(i) == 1:
                j = i[0]
                self.thread.bond_axis_func(j[0], j[1], [*j[2::]])
            elif len(i) == 2:
                axis_1 = i[0][1]
                map_1  = [*i[0][2::]]
                axis_2 = i[1][1]
                map_2  = [*i[1][2::]]
                self.thread.bond_double_axes_func(k, axis_1, axis_2, map_1, map_2)
                
        self.thread.bond_button_func(6, lambda: minus_gaer(self.robot, self.main_window.gear_level_slider))
        self.thread.bond_button_func(7, lambda: plus_gaer(self.robot, self.main_window.gear_level_slider))
        


class thread_joystick(threading.Thread):
    """传入pygame.joystick.Joystick实例，以及robot实例。该实例提供set_speed(int id, fload speed)方法"""
    def __init__(self, joy, robot, main_window=None, FPS=60) -> None:
        threading.Thread.__init__(self)
        self.CLOCK = pygame.time.Clock()
        self.robot = robot
        self.joy = joy
        self.joy.init()
        self.FPS = FPS
        self.main_window = main_window
        self.axes_list = [0 for _ in range(self.joy.get_numaxes())]
        self.button_list = [0 for _ in range(self.joy.get_numaxes())]
        self.axes_ctrl_funcs =   []
        self.button_ctrl_funcs = [None for _ in range(self.joy.get_numbuttons())]
        self.isRunning = False
    
    def run(self):
        print(f"手柄{self.joy.get_name()}进程开启")
        self.isRunning = True
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    # 运行所有的按钮控制程序
                    btn = event.button
                    if self.button_ctrl_funcs[btn] is not None:
                        self.button_ctrl_funcs[btn]()
                    
            # 运行所有的轴速度控制程序
            for func in self.axes_ctrl_funcs:
                if func is not None:
                    func()
            self.CLOCK.tick(self.FPS)
        print("手柄进程被终止")     

    def axis_speed_ctrl(self, axis_id, moto_id, k, b):
        '''通过轴号控制电机的速度'''
        
        axis_value = self.joy.get_axis(axis_id)
        # if 0.05 > axis_value  > -0.05:
        #     axis_value  = 0
        # if -1. < axis_value  < -0.995:
        #     axis_value  = -1
        # if 1. > axis_value  > 0.995:
        #     axis_value  = 1
        axis_value = axis_shift_cancelling(axis_value)
        
        speed = k*axis_value + b if axis_value != 0 else 0
        speed_old = self.axes_list[axis_id]
        
        if abs(speed-speed_old) > 2 or (speed==0 and speed_old!=0):
            self.robot.set_speed(moto_id, speed)
            self.axes_list[axis_id] = speed
    
    def double_axis_ctrl(self, moto_id, axis_1, k1, b1, axis_2, k2, b2):
        '''同时通过两个轴控制电机的速度'''
        axis1_value = self.joy.get_axis(axis_1)
        axis2_value = self.joy.get_axis(axis_2)
        
        axis1_value = axis_shift_cancelling(axis1_value)
        axis2_value = axis_shift_cancelling(axis2_value)
        
        speed1 = k1*axis1_value + b1 if axis1_value != 0 else 0
        speed2 = k2*axis2_value + b2 if axis2_value != 0 else 0
        
        speed1_old = self.axes_list[axis_1]
        speed2_old = self.axes_list[axis_2]
        
        speed = speed1 + speed2
        speed_old = speed1_old + speed2_old
        
        if abs(speed-speed_old) > 2 or (speed==0 and speed_old!=0):
            self.robot.set_speed(moto_id, speed)
            self.axes_list[axis_1] = speed1
            self.axes_list[axis_2] = speed2
        

    
    def bond_button_func(self, button_num, func):
        """将按钮号与指定的函数相绑定"""
        self.button_ctrl_funcs[button_num] = func

    def bond_axis_func(self, moto_id, axis_num, spd_map=(-1, 1, 3600, -3600)):
        """将电机的控制与指定的轴号相连"""
        k, b = spd_map_func(map_in=(spd_map[0], spd_map[1]), map_out=(spd_map[2], spd_map[3]))
        self.axes_ctrl_funcs.append(lambda: self.axis_speed_ctrl(axis_num, moto_id, k, b))
    
    def bond_double_axes_func(self, moto_id, axis_1, axis_2, spd_map_1=(-1, 1, 0, -3600), spd_map_2=(-1, 1, 0, 3600)):
        """"""
        k1, b1 = spd_map_func_(spd_map_1)
        k2, b2 = spd_map_func_(spd_map_2)
        print(moto_id, axis_1, k1, b1, axis_2, k2, b2)
        self.axes_ctrl_funcs.append(lambda: self.double_axis_ctrl(moto_id, axis_1, k1, b1, axis_2, k2, b2))


class Signal_Worker(QObject):
    sender = Signal(str)
    dic_sender = Signal(dict)
    def send_text(self, text):
        self.sender.emit(text)
    def send_dict(self, dic):
        self.dic_sender.emit(dic)

class flash_joyState_text(threading.Thread):
    def __init__(self, joyDialog):
        threading.Thread.__init__(self)
        self.joy = None
        # self.joy = joystick.Joystick(id)
        self.isRunning = False
        self.joyDialog = joyDialog
        self.send_str = Signal_Worker()
        self.lock = threading.Lock()
        self.last_len = 10

    def run(self):
        self.isRunning = True
        clock = pygame.time.Clock()
        self.joyDialog.joyStateShow.clear()
        
        while self.isRunning:
            if self.joy is not None:
                self.lock.acquire()
                text = self.get_state()
                self.lock.release()
                self.send_str.send_text(text)
            clock.tick(30)
    
    def set_joy(self, joyId):
        if self.joy is not None:
            self.ignore_joy()
        self.lock.acquire()
        self.joy = joystick.Joystick(joyId)
        self.joy.init()
        self.lock.release()

    def ignore_joy(self):
        if self.joy is not None:
            self.lock.acquire()
            self.joy.quit()
            self.joy = None
            self.lock.release()

    def get_state(self):
        state_str = ""
        indent_str = ""
        try:
            jid = self.joy.get_instance_id()
        except AttributeError:
            # get_instance_id() is an SDL2 method
            jid = self.joy.get_id()
        state_str += "{}Joystick {}\n".format(indent_str, jid)
        indent_str += "  "

        # Get the name from the OS for the controller/self.joy.
        name = self.joy.get_name()
        state_str += "{}Joystick name: {}\n".format(indent_str, name)

        try:
            guid = self.joy.get_guid()
        except AttributeError:
            # get_guid() is an SDL2 method
            pass
        else:
            state_str += "{}GUID: {}\n".format(indent_str, guid)

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = self.joy.get_numaxes()
        state_str += "{}Number of axes: {}\n".format(indent_str, axes)
        indent_str += "  "

        for i in range(axes):
            axis = self.joy.get_axis(i)
            state_str += "{}Axis {} value: {:>6.3f}\n".format(indent_str, i, axis)
        
        indent_str = indent_str[::-2]

        buttons = self.joy.get_numbuttons()
        state_str += "{}Number of buttons: {}\n".format(indent_str, buttons)
        indent_str += "  "

        for i in range(buttons):
            button = self.joy.get_button(i)
            state_str +=  "{}Button {:>2} value: {}\n".format(indent_str, i, button)
        indent_str = indent_str[::-2]

        hats = self.joy.get_numhats()
        state_str += "{}Number of hats: {}\n".format(indent_str, hats)
        indent_str += "  "

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = self.joy.get_hat(i)
            state_str += "{}Hat {} value: {}\n".format(indent_str, i, str(hat))
        return state_str


if __name__ == "__main__":
    # 参数配置
    from robot_control import Robot

    # 初始化机器人
    robot = Robot("COM3")
    
    # 初始化舵机管理器
    a = thread_joystick(0, robot)