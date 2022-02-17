from mainwindow import Ui_MainWindow
from portDialog import Ui_Dialog as port_dialog
from joystickDialog import Ui_Dialog as joystick_dialog
from axisSetDialog import Ui_Dialog as axis_dialog
import serial_widget_thread
from robot_control import Robot
from joystick_control import joystick_manager, flash_joyState_text, save_joy_options, load_joy_options
from robot_control import Robot
import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog



main_window = Ui_MainWindow()  # 主界面

dialog_port = port_dialog()   # 串口调试助手
dialog_joyconfig = joystick_dialog()  # 手柄设置窗口
dialog_axis_add = axis_dialog()   # 手柄轴设置窗口

QueryTimer = QTimer()
QueryTimer.setInterval(10)
app = QApplication(sys.argv)
w = QMainWindow()

diaPortAPP = QDialog()  # 串口调试助手
diaJoyAPP  = QDialog()  # 手柄设置窗口
axisAPP = QDialog()     # 手柄轴设置窗口

dialog_joyconfig.setupUi(diaJoyAPP)
dialog_port.setupUi(diaPortAPP)
dialog_axis_add.setupUi(axisAPP)
main_window.setupUi(w)
main_window.speed_UI_list = [main_window.cath_speed_lcd, 
                             main_window.wire_speed_lcd,
                             main_window.wire_rotSpeed_lcd]



SurgRobot = Robot()
JoyStick = joystick_manager(SurgRobot, main_window)
thread_listen    = serial_widget_thread.read_thr(SurgRobot, dialog_port)
thread_listen.name = "串口调试助手线程"
thread_joylisten = flash_joyState_text()
thread_joylisten.name = "手柄调试助手线程"
cursor = dialog_port.recv_Text.textCursor()

robo_options = {
    "temp_ports_list": [],
    "temp_joys_list" : [],
    "last_port"      : 0,
    "last_joy"       : 0,
    "end_char"       : 0,
}


def fresh_ports():
    ports, names = SurgRobot.scan_ports()    
    for k, i in enumerate(robo_options["temp_ports_list"]):
        if i not in names:
            main_window.com_select.removeItem(k+1)
    
    for k, i in zip(ports, names):
        if i not in robo_options["temp_ports_list"]:
            main_window.com_select.addItem(i)    
    robo_options["temp_ports_list"] = names


def fresh_joystick():
    joys = JoyStick.scan_joystick()
    for k, i in enumerate(robo_options["temp_joys_list"]):
        if i not in joys:
            main_window.joystick_select.removeItem(k+1)
    
    for  i in joys:
        if i not in robo_options["temp_joys_list"]:
            main_window.joystick_select.addItem(i)
    robo_options["temp_joys_list"] = joys


def func_for_show_ports(*args):
    """展示串口的函数"""
    fresh_ports()
    main_window.com_select.showPopup()


def func_for_select_port(*args):
    """选择连接到某个串口"""
    index = args[0]
    if index > 0:
        SurgRobot.open_robot_port(SurgRobot.port_list[index-1]) 
    else:
        SurgRobot.close_robot_port()
    robo_options["last_port"] = index


def func_for_show_joysticks(*args):
    """展示手柄的函数"""
    fresh_joystick()
    main_window.joystick_select.showPopup()


def func_for_select_joystick(*args):
    """连接并启动某个手柄的函数"""
    index = args[0]
    if index > 0:
        JoyStick.start_joystick(index-1)
    else:
        JoyStick.close_joystick()
    robo_options["last_joy"] = index
    
def func_for_gearlevel_change(*args):
    """更改速度档位的函数"""
    SurgRobot.gear_level = (main_window.gear_level_slider.value() * 0.2)
    print(SurgRobot.gear_level)
    pass

def func_for_send_serial_msg(*args):
    endings = ["", "\n", "\r", "\r\n"]
    msg = dialog_port.send_Input.text()
    msg += endings[dialog_port.end_select.currentIndex()]
    SurgRobot.write_ser(msg)
    dialog_port.send_Input.clear()

def open_serial_thread():
    """打开监听串口的后台线程"""
    global thread_listen
    thread_listen.start()

def open_joy_thread():
    """打开监听手柄的后台线程"""
    global thread_joylisten
    thread_joylisten.start()

def func_for_open_joySet_dialog(*args):
    dialog_joyconfig.joyStateShow.clear()
    global thread_joylisten
    JoyStick.close_joystick()
    index = robo_options["last_joy"]
    if index > 0:
        thread_joylisten.set_joy(robo_options["last_joy"]-1)
    else:
        dialog_joyconfig.joyStateShow.append("手柄未选择")

def func_for_close_joySet_dialog(*args):
    global thread_joylisten
    thread_joylisten.ignore_joy()
    index = robo_options["last_joy"]
    if index > 0:
        JoyStick.start_joystick(robo_options["last_joy"]-1)
    

def func_for_open_serial_dialog(*args):
    """打开串口小部件时运行的函数"""
    dialog_port.recv_Text.clear()
    if not SurgRobot.ser.isOpen():
        dialog_port.recv_Text.append("串口未打开")
    global thread_listen
    SurgRobot.flush_ser()
    thread_listen.show = True
    pass


def func_for_close_serial_dialog(*args):
    """关闭串口小部件时运行的函数"""
    global thread_listen
    thread_listen.show = False
    pass

def func_for_select_end_char(*args):
    '''串口监视器选择结束符的函数'''
    robo_options["end_char"]=args[0]


def func_for_print_args(*args):
    """将传入的事件参数全部打印出来"""
    print(args)

def func_for_lcd_speed(*args):
    motoId, spd = args
    main_window.speed_UI_list[motoId].display(int(spd))

def dialog_joy_setting_update(dict):
    """传入手柄配置字典，刷新手柄设置菜单中的当前配置"""
    dialog_joyconfig.nowSettingShow.clear()
    motoName = ["导管递送", "导丝递送", "导丝旋转"]
    for axis_bind_tuple in dict["axis"]:
        motoID, axis, fromLow, fromHigh, toLow, toHigh = axis_bind_tuple
        dialog_joyconfig.nowSettingShow.addItem(f"轴{axis}: {motoName[motoID]}\n    ({fromLow},{fromHigh})->({toLow},{toHigh})")
    pass


def disable_swicher(button_id):
    """绑定禁用-启用按钮的方法"""
    button = None
    if button_id == 0:
        button = main_window.cath_disable_button
    elif button_id == 1:
        button = main_window.wire_disable_button
    elif button_id == 2:
        button = main_window.wire_rot_disable_button
    if button is not None:
        text = button.text()
        if text[2:4] == "禁止":
            button.setText(f"{text[0:2]}启用{text[4::]}")
            SurgRobot.change_disable_state(button_id, True)
        elif text[2:4] == "启用":
            button.setText(f"{text[0:2]}禁止{text[4::]}")
            SurgRobot.change_disable_state(button_id, False)
        else:
            print(f"异常值: {text}")


def bind_methods():
    """为各个小部件绑定事件"""
    global thread_listen
    SurgRobot.spd_signal.connect(func_for_lcd_speed)
    # com_select
    main_window.com_select.mousePressEvent = func_for_show_ports
    main_window.com_select.currentIndexChanged.connect(func_for_select_port) 
    # joystick_select
    main_window.joystick_select.mousePressEvent = func_for_show_joysticks
    main_window.joystick_select.currentIndexChanged.connect(func_for_select_joystick)     
    # gear_level_slider
    main_window.gear_level_slider.setPageStep(1)
    main_window.gear_level_slider.valueChanged.connect(func_for_gearlevel_change)
    # menu
    main_window.menu_joySet.triggered.connect(diaJoyAPP.exec)
    main_window.menu_Port.triggered.connect(diaPortAPP.exec)
    # dialog_port
    dialog_port.pushButton.clicked.connect(func_for_send_serial_msg)
    dialog_port.pushButton_2.clicked.connect(dialog_port.recv_Text.clear)
    dialog_port.end_select.currentIndexChanged.connect(func_for_select_end_char)
    dialog_port.AutoLast.clicked.connect(thread_listen.jump_to_last_line)
    thread_listen.worker.jump_sig.connect(dialog_port.recv_Text.setTextCursor)
    thread_listen.worker.send_char_sig.connect(cursor.insertText)
    diaPortAPP.showEvent = func_for_open_serial_dialog
    diaPortAPP.closeEvent = func_for_close_serial_dialog
    # dialog_joy
    dialog_joyconfig.addSettingButton.clicked.connect(axisAPP.exec)
    dialog_joyconfig.nowSettingShow.itemDoubleClicked.connect(func_for_print_args)
    thread_joylisten.signal_boject.text_sender.connect(dialog_joyconfig.joyStateShow.setPlainText)
    thread_joylisten.signal_boject.dic_sender.connect(dialog_joy_setting_update)
    diaJoyAPP.rejected.connect(func_for_close_joySet_dialog)
    diaJoyAPP.showEvent = func_for_open_joySet_dialog
    diaJoyAPP.leaveEvent = func_for_close_joySet_dialog

    # buttons: steps
    main_window.all_stop_button.clicked.connect(SurgRobot.all_stop) 
    main_window.cath_up_button.clicked.connect(SurgRobot.all_stop)
    # buttons: disable_state
    main_window.cath_disable_button.clicked.connect(lambda: disable_swicher(0))
    main_window.wire_disable_button.clicked.connect(lambda: disable_swicher(1))
    main_window.wire_rot_disable_button.clicked.connect(lambda: disable_swicher(2))
    
    pass

def close_methods(*args):
    """主窗口关闭时进行的动作"""
    save_options()
    thread_listen.isRunning = False
    thread_joylisten.isRunning = False
    SurgRobot.close_robot_port()
    JoyStick.close_joystick()

    
def init_methods(*args):
    """主函数开始运行时的动作"""
    load_joy_options()
    load_options()
    open_serial_thread()
    open_joy_thread()


def save_options():
    """导出配置到文件中"""
    import json as json
    with open("main_config.json", 'w') as js_file:
        js_string = json.dumps(robo_options, sort_keys=True, indent=4, separators=(',', ': '))
        js_file.write(js_string)

def load_options():
    """从文件中加载配置"""
    import json as json
    with open("main_config.json", 'r') as js_file:
        temp_robo_options = json.load(js_file)
    fresh_ports()
    fresh_joystick()
    if temp_robo_options["temp_ports_list"] == robo_options["temp_ports_list"]:
        main_window.com_select.setCurrentIndex(temp_robo_options["last_port"])

    if temp_robo_options["temp_joys_list"] == robo_options["temp_joys_list"]:
        main_window.joystick_select.setCurrentIndex(temp_robo_options["last_joy"])
    
    dialog_port.end_select.setCurrentIndex(temp_robo_options["end_char"])

def main():
    bind_methods()
    init_methods()
    w.closeEvent = close_methods
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    


