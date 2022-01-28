from mainwindow import Ui_MainWindow
from robot_control import Robot
from joystick_control import joystick_manager
import mainwindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from robot_control import Robot

main_window = Ui_MainWindow()
SurgRobot = Robot()
JoyStick = joystick_manager()
robo_options = {
    "temp_ports_list":[],
}

def func_for_show_ports(*args):
    """展示串口的函数"""
    ports, names = SurgRobot.scan_ports()
    
    for k, i in enumerate(robo_options["temp_ports_list"]):
        if i not in names:
            main_window.com_select.removeItem(k+1)
    
    for k, i in zip(ports, names):
        if i not in robo_options["temp_ports_list"]:
            main_window.com_select.addItem(i)
    
    robo_options["temp_ports_list"] = names
    main_window.com_select.showPopup()


def func_for_select_port(*args):
    """选择连接到某个串口"""
    index = args[0]
    if index > 0:
        SurgRobot.open_robot_port(SurgRobot.port_list[index-1])
    else:
        SurgRobot.close_robot_port()
    print(index)


def func_for_show_joysticks(*args):
    joys = 

def func_for_select_joystick(*args):
    pass


def bind_methods():
    main_window.com_select.mousePressEvent = func_for_show_ports
    main_window.com_select.currentIndexChanged.connect(func_for_select_port) 
    # 展示串口
    main_window.all_stop_button.clicked.connect(func_for_show_ports)

    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QMainWindow()
    main_window.setupUi(w)
    bind_methods()
    w.show()
    sys.exit(app.exec())
