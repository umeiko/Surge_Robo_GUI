from pygame import joystick
# 导入依赖
import time
import struct
import serial
import pygame



def spd_map(map_0, map_1):
    """将速度从区间a线性映射到区间b，返回函数的斜率k和偏置b"""
    k = (map_1[1] - map_1[0]) / (map_0[1] - map_0[0])
    b = (map_1[0] - k*map_0[0])
    return k, b


class joysitck_manager():
    def __init__(self, joy_num, robot) -> None:
        self.robot = robot
        pygame.init()
        joystick.init()
        self.joystick = joystick.Joystick(joy_num)
        self.joystick.init()
        self.CLOCK = pygame.time.Clock()
        self.FPS = 120
        self.axes_list = [0 for i in range(self.joystick.get_numaxes())]
        self.button_list = [0 for i in range(self.joystick.get_numaxes())]
    
    def main_loop(self):
        k0, b0 = spd_map((-1, 1), (3600, -3600))
        k1, b1 = spd_map((-1, 1), (-3600, 3600))
        k3, b3 = spd_map((-1, 1), (-16000, 16000))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    self.pos_check()
                pass
            self.speed_ctrl(0, 0, k0, b0)
            self.speed_ctrl(1, 1, k1, b1)
            self.speed_ctrl(2, 2, k3, b3)
            self.CLOCK.tick(self.FPS)
    
    def speed_ctrl(self, axis_id, moto_id, k, b):
        axis_value = self.joystick.get_axis(axis_id)
        if 0.05 > axis_value  > -0.05:
            axis_value  = 0
        if -1. < axis_value  < -0.995:
            axis_value  = -1
        if 1. > axis_value  > 0.995:
            axis_value  = 1
        speed = k*axis_value + b
        speed_old = self.axes_list[axis_id]
        if abs(speed-speed_old) > 5 or (axis_value==0 and speed_old!=0):
            self.set_speed(moto_id, speed)
            self.axes_list[axis_id] = speed
    
    def set_speed(self, moto_id, spd_v):
        self.robot.set_speed(moto_id, spd_v)

    def pos_check(self):
        print(self.robot.get_position())


if __name__ == "__main__":
    # 参数配置
    from robot_control import Robot

    # 初始化机器人
    robot = Robot("COM3")
    
    # 初始化舵机管理器
    a = joysitck_manager(0, robot)
    a.main_loop()