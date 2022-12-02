from cmath import pi
from mainwindow import Ui_MainWindow
from portDialog import Ui_Dialog as port_dialog
from joystickDialog import Ui_Dialog as joystick_dialog
from axisSetDialog import Ui_Dialog as axis_dialog
import serial_widget_thread
from robot_control import Robot
from joystick_control import joystick_manager, flash_joyState_text, load_joy_options, spd_map_func
from robot_control import Robot
from PySide6.QtGui import QIcon, QShortcut
import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
import numpy as np

main_window = Ui_MainWindow() # 主界面
dialog_port = port_dialog()   # 串口调试助手
dialog_joyconfig = joystick_dialog()  # 手柄设置窗口
dialog_axis_add = axis_dialog()       # 手柄轴设置窗口

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
# thread_listen      = serial_widget_thread.read_thr(SurgRobot, dialog_port)
# thread_listen.name = "串口调试助手线程"
thread_joylisten   = flash_joyState_text()
thread_joylisten.name = "手柄调试助手线程"
thread_StepAndSpeed   =  serial_widget_thread.msg_fresh_thr(SurgRobot, dialog_port)
thread_StepAndSpeed.name = "串口异步处理线程"


cursor = dialog_port.recv_Text.textCursor()
joy_config_flag  = True
joy_config_index = -1
fashion_flag = False

global_options = {
    "temp_ports_list": [],
    "temp_joys_list" : [],
    "last_port"      : 0,
    "last_joy"       : 0,
    "end_char"       : 0,
    "skin_mode"      : "classic",
    "gear_level"     : 0,
    "step_levels"    : [0, 0, 0],
    "disable_states" : [True, True, True],
}

class Speed_Conver:
    """速度转换矩阵表示"""
    def __init__(self,motorId,spd):
        self.w_MG1 = 0 # 导丝递送电机输入(°/s)
        self.f_MG2 = 0 # 导丝旋转电机输入(Hz)
        self.f_MC1 = 0 # 直线平台电机输入(Hz)
        # self.f_MC2 = 0 # 导管递送电机输入(°/s)
        self.spd = spd
        self.motorId = motorId
        self.theta_s1 = 1.8 # 导丝转台电机的步距角
        self.theta_s2 = 1.8 # 直线平台电机的步距角
        self.K = 1/18 # 导丝转台的齿比
        self.K1 = 1/2.5 # 导丝转台电机的细分
        self.K2 = 1/32 # 直线平台电机的细分
        self.d1 = 8 # 单位mm  导丝递送摩擦轮直径
        # self.d2 = 8 # 单位mm  导管递送摩擦轮直径
        self.S = 10 # 单位mm  直线平台的导程
 
    def speed_conversion(self):
        A_1 = np.array([[360,0,0],
                        [0,360/(self.theta_s1*self.K1),0],
                        [0,0,360/(self.theta_s2*self.K2)]])
        A_2 = np.array([[1/(np.pi*self.d1),0,-1/(np.pi*self.d1)],
                       [0,1/(self.K*360),0],
                       [0,0,1/self.S]])
        temp = np.linalg.pinv(np.matmul(A_1,A_2))
        if(self.motorId == 0):
            self.f_MC1 = self.spd
        if(self.motorId == 1):
            self.w_MG1 = self.spd
        if(self.motorId == 2):
            self.f_MG2 = self.spd
        y= np.array([self.w_MG1,self.f_MG2,self.f_MC1*14*np.pi]).T
        speed_cop = np.matmul(temp,y) # 导丝速度（mm/s），导丝旋转速度(°/s)，导管速度(mm/s)
        main_window.speed_UI_list[0].display(round(-speed_cop[2],3))
        main_window.speed_UI_list[1].display(round(-speed_cop[0],3))
        main_window.speed_UI_list[2].display(round(-speed_cop[1],3))
        if SurgRobot.mode_select :
            main_window.speed_UI_list[1].display(0)
        

def fresh_ports():
    """刷新系统当前连接的串口设备"""
    main_window.com_select.setItemText(0, "断开连接")
    ports, names = SurgRobot.scan_ports()
    
    for k, i in enumerate(global_options["temp_ports_list"]):
        # 删除已不存在的端口
        if i not in ports:
            main_window.com_select.removeItem(k+1)
            if global_options["temp_ports_list"]:
                global_options["temp_ports_list"].pop(k)
    
    for k, i in enumerate(names):
        # 添加新出现的端口
        if ports[k] not in global_options["temp_ports_list"]:
            main_window.com_select.addItem(i)
            if global_options["temp_ports_list"]:
                global_options["temp_ports_list"].append(ports[k])
    
    if not global_options["temp_ports_list"]:
        global_options["temp_ports_list"] = ports


def fresh_joystick():
    '''刷新系统当前连接的手柄设备'''
    joys = JoyStick.scan_joystick()
    for k, i in enumerate(global_options["temp_joys_list"]):
        if i not in joys:
            main_window.joystick_select.removeItem(k+1)
    
    for  i in joys:
        if i not in global_options["temp_joys_list"]:
            main_window.joystick_select.addItem(i)
    global_options["temp_joys_list"] = joys

def func_for_show_ports(*args):
    """展示串口的函数"""
    fresh_ports()
    main_window.com_select.showPopup()

def func_for_select_port(*args):
    """选择连接到某个串口"""
    index = args[0]
    if index > 0:
        SurgRobot.open_robot_port(global_options["temp_ports_list"][index-1])
    else:
        SurgRobot.close_robot_port()
    global_options["last_port"] = index


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
    global_options["last_joy"] = index
    
def func_for_gearlevel_change(*args):
    """更改速度档位的函数"""
    SurgRobot.gear_level = (main_window.gear_level_slider.value() * 0.2)
    global_options["gear_level"] = main_window.gear_level_slider.value()
    print(SurgRobot.gear_level)
    pass

def func_for_send_serial_msg(*args):
    endings = ["", "\n", "\r", "\r\n"]
    msg = dialog_port.send_Input.text()
    msg += endings[dialog_port.end_select.currentIndex()]
    SurgRobot.write_ser(msg)
    dialog_port.send_Input.clear()

# def open_serial_thread():
#     """打开监听串口的后台线程"""
#     global thread_listen
#     thread_listen.start()

def open_joy_thread():
    """打开监听手柄的后台线程"""
    global thread_joylisten
    thread_joylisten.start()

def func_for_open_joySet_dialog(*args):
    """打开手柄调试窗口时运行的函数"""
    dialog_joyconfig.joyStateShow.clear()
    global thread_joylisten
    JoyStick.close_joystick()
    index = global_options["last_joy"]
    if index > 0:
        thread_joylisten.set_joy(global_options["last_joy"]-1)
    else:
        dialog_joy_setting_update(load_joy_options()["default"])
        dialog_joyconfig.joyStateShow.append("手柄未选择")


def func_for_close_joySet_dialog(*args):
    """关闭手柄调试窗口时运行的函数"""
    global thread_joylisten
    thread_joylisten.ignore_joy()
    index = global_options["last_joy"]
    if index > 0:
        JoyStick.start_joystick(global_options["last_joy"]-1)
    

def func_for_open_serial_dialog(*args):
    """打开串口小部件时运行的函数"""
    dialog_port.recv_Text.clear()
    if not SurgRobot.ser.isOpen():
        dialog_port.recv_Text.append("串口未打开")
    global thread_listen
    SurgRobot.flush_ser()
    thread_StepAndSpeed.freshText = True
    # thread_listen.show = True
    thread_StepAndSpeed.pause = True


def func_for_close_serial_dialog(*args):
    """关闭串口小部件时运行的函数"""
    global thread_listen
    # thread_listen.show = False
    thread_StepAndSpeed.freshText = False
    thread_StepAndSpeed.pause = False

def func_for_select_end_char(*args):
    '''串口监视器选择结束符的函数'''
    global_options["end_char"]=args[0]


def func_for_print_args(*args):
    """将传入的事件参数全部打印出来"""
    print(args)

def func_for_lcd_speed(*args):
    """刷新速度显示窗口"""
    motoId, spd = args
    speed_c = Speed_Conver(motoId,spd)
    speed_c.speed_conversion()

def func_for_lcd_pos(*args):
    """刷新位置显示窗口"""
    x, y, z = args
    if x is not None:
        main_window.cath_pos_speed_lcd.display(round(x, 3))
    if y is not None:
        main_window.wire_pos_lcd.display(round(y, 3))
    if z is not None:
        main_window.wire_rotPos_lcd.display(round(z, 3))

def dialog_joy_setting_update(dict):
    """传入手柄配置字典，刷新手柄设置菜单中的当前配置"""
    dialog_joyconfig.nowSettingShow.clear()
    motoName = ["导管递送", "导丝递送", "导丝旋转"]
    for axis_bind_tuple in dict["axis"]:
        motoID, axis, fromLow, fromHigh, toLow, toHigh = axis_bind_tuple
        dialog_joyconfig.nowSettingShow.addItem(f"轴{axis}: {motoName[motoID]}\n    ({fromLow},{fromHigh})->({toLow},{toHigh})")
    pass

def disable_swicher(button_id, state=None):
    """绑定禁用-启用按钮的方法, 同时可以改变机器人的禁用情况"""
    button = None
    style_str = ""
    if button_id == 0:
        button = main_window.cath_disable_button
        SurgRobot.flags[0] = not SurgRobot.flags[0]
    elif button_id == 1:
        button = main_window.wire_disable_button
        SurgRobot.flags[1] = not SurgRobot.flags[1]
    elif button_id == 2:
        button = main_window.wire_rot_disable_button
        SurgRobot.flags[2] = not SurgRobot.flags[2]
    if global_options["skin_mode"] == "classic":
        style_str = ""
    elif global_options["skin_mode"] == "MaterialDark":
        style_str = "_dark"
    text = button.text()
    
    def set_state(button, state):
        if state:
            button.setText(f"{text[0:2]}禁止{text[4::]}")
            SurgRobot.change_disable_state(button_id, False)
            button_icon = QIcon()
            button_icon.addFile(f":/disable{style_str}.png", QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(button_icon)
            global_options["disable_states"][button_id] = True
        else:
            button.setText(f"{text[0:2]}启用{text[4::]}")
            SurgRobot.change_disable_state(button_id, True)
            button_icon = QIcon()
            button_icon.addFile(f":/accept{style_str}.png", QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(button_icon)
            global_options["disable_states"][button_id] = False 

    if state is None:
        if global_options["disable_states"][button_id]:
            set_state(button, False)
        else:
            set_state(button, True)
    else:
        set_state(button, state)           

def func_for_serial_erro(*args):
    """串口异常处理的函数"""
    print(args)
    SurgRobot.ser.close()
    main_window.com_select.setItemText(0, "连接失败, 请重试")
    main_window.com_select.setCurrentIndex(0)
    diaPortAPP.close()

def func_for_insert_port_text(*args):
    """将文本插入到串口信息显示器中"""
    text, is_html = args
    if is_html:
        cursor.insertHtml(text)
    else:
        cursor.insertText(text)

def func_add_step_mission(id, dir=1, time=1):
    """添加单步前进任务"""
    if id == 0:
        value = main_window.cath_step_slider.value()
        k, b = spd_map_func((0, 99), (0.5, 2))  
        value = -dir * (k * value + b) * 640 / (14 * np.pi)
    elif id == 1:
        
        value = main_window.wire_step_slider.value()
        k, b = spd_map_func((0, 99), (0.5, 2))
        value = -dir * (k * value + b) * 360 / (8 * np.pi) 
    elif id == 2:
        value = main_window.wireRot_step_slider.value()
        k, b = spd_map_func((0, 99), (5, 45))
        value = -dir * (k * value + b) * 9000 / 360
    # value = dir * (k * value + b)
    thread_StepAndSpeed.addStep(id, value, time)

def func_for_emergency_stop(*args):
    """急停开关执行的指令"""
    SurgRobot.all_stop()
    thread_StepAndSpeed.clearMissons()
def bind_methods():
    """为各个小部件绑定事件"""
    global thread_listen
    SurgRobot.spd_signal.connect(func_for_lcd_speed)
    SurgRobot.port_erro_signal.connect(func_for_serial_erro)
    
    # thread_StepAndSpeed
    thread_StepAndSpeed.worker.speed_sig.connect(func_for_lcd_pos)
    
    # com_select
    main_window.com_select.mousePressEvent = func_for_show_ports
    main_window.com_select.currentIndexChanged.connect(func_for_select_port) 
    main_window.com_select.wheelEvent=lambda *args: None
    
    # joystick_select
    main_window.joystick_select.mousePressEvent = func_for_show_joysticks
    main_window.joystick_select.currentIndexChanged.connect(func_for_select_joystick)
    main_window.joystick_select.wheelEvent=lambda *args: None  
    
    # gear_level_slider
    main_window.gear_level_slider.setPageStep(1)
    main_window.gear_level_slider.valueChanged.connect(func_for_gearlevel_change)
    
    # step_slider
    main_window.cath_step_slider.valueChanged.connect(
        lambda x:main_window.cath_step_text.setText(f"{(0.5+0.01515152*x):.2f}mm"))
    main_window.wire_step_slider.valueChanged.connect(
        lambda x:main_window.wire_step_text.setText(f"{(0.5+0.01515152*x):.2f}mm"))
    main_window.wireRot_step_slider.valueChanged.connect(
        lambda x:main_window.wireRot_step_text.setText(f"{(5+0.40404*x):.2f}°"))
    
    # menu
    main_window.menu_joySet.triggered.connect(diaJoyAPP.exec)
    main_window.menu_Port.triggered.connect(diaPortAPP.exec)
    main_window.style_dark.triggered.connect(change_style_dark)
    main_window.style_classic.triggered.connect(change_style_classic)
    
    # dialog_port
    shortcut = QShortcut(diaPortAPP)
    shortcut.setKey(u'Return')
    shortcut.activated.connect(func_for_send_serial_msg)
    dialog_port.pushButton.clicked.connect(func_for_send_serial_msg)
    dialog_port.pushButton_2.clicked.connect(dialog_port.recv_Text.clear)
    dialog_port.end_select.currentIndexChanged.connect(func_for_select_end_char)
    # dialog_port.AutoLast.clicked.connect(thread_listen.jump_to_last_line)
    dialog_port.AutoLast.clicked.connect(thread_StepAndSpeed.jump_to_last_line)
    
    # thread_listen.worker.jump_sig.connect(dialog_port.recv_Text.setTextCursor)
    # thread_listen.worker.send_char_sig.connect(func_for_insert_port_text)
    # thread_listen.worker.erro_sig.connect(func_for_serial_erro)
    thread_StepAndSpeed.worker.jump_sig.connect(dialog_port.recv_Text.setTextCursor)
    thread_StepAndSpeed.worker.send_char_sig.connect(func_for_insert_port_text)
    thread_StepAndSpeed.worker.erro_sig.connect(func_for_serial_erro)
    
    diaPortAPP.showEvent = func_for_open_serial_dialog
    diaPortAPP.closeEvent = func_for_close_serial_dialog
    
    # dialog_joy
    dialog_joyconfig.addSettingButton.clicked.connect(axisAPP.exec)
    thread_joylisten.signal_boject.text_sender.connect(dialog_joyconfig.joyStateShow.setPlainText)
    thread_joylisten.signal_boject.dic_sender.connect(dialog_joy_setting_update)
    
    diaJoyAPP.accepted.connect(func_for_close_joySet_dialog)
    diaJoyAPP.rejected.connect(func_for_close_joySet_dialog)
    dialog_joyconfig.nowSettingShow.itemDoubleClicked.connect(change_joyset)
    diaJoyAPP.showEvent = func_for_open_joySet_dialog
    # dialog_axis_add
    dialog_axis_add.buttonBox.accepted.connect(save_joyset)

    # buttons: steps and all_stop
    main_window.all_stop_button.clicked.connect(func_for_emergency_stop) 
    main_window.cath_up_button.clicked.connect(lambda: func_add_step_mission(0))
    main_window.cath_down_button.clicked.connect(lambda: func_add_step_mission(0, -1))
    main_window.wire_up_button.clicked.connect(lambda: func_add_step_mission(1))
    main_window.wire_down_button.clicked.connect(lambda: func_add_step_mission(1, -1))
    main_window.wire_clock_button.clicked.connect(lambda: func_add_step_mission(2))
    main_window.wire_antiClock_button.clicked.connect(lambda: func_add_step_mission(2, -1))

    # buttons: disable_state
    main_window.cath_disable_button.clicked.connect(lambda: disable_swicher(0))
    main_window.wire_disable_button.clicked.connect(lambda: disable_swicher(1))
    main_window.wire_rot_disable_button.clicked.connect(lambda: disable_swicher(2))
    main_window.cath_mode_select.currentIndexChanged.connect(
                            lambda: WrittingNotOfOther(main_window.cath_mode_select.currentIndex()))  # 点击下拉列表，触发对应事件


def WrittingNotOfOther(id):
    if id == 1:
        SurgRobot.mode_select = 1
    else:
        SurgRobot.mode_select = 0    
            

def close_methods(*args):
    """主窗口关闭时进行的动作"""
    save_options()
    # thread_listen.isRunning = False
    thread_joylisten.isRunning = False
    thread_StepAndSpeed.isRunning = False
    SurgRobot.close_robot_port()
    JoyStick.close_joystick()

    
def init_methods(*args):
    """主函数开始运行时的动作"""
    load_joy_options()
    load_options()
    # open_serial_thread()
    open_joy_thread()
    thread_StepAndSpeed.start()

def change_style_classic():
    """切换样式到经典"""
    if global_options["skin_mode"] != "classic":
        global_options["skin_mode"] = "classic"
        w.setStyleSheet("")
        diaPortAPP.setStyleSheet("")
        main_window.cath_up_button.setStyleSheet(u"border-image: url(:/up.png);\n""")
        main_window.cath_down_button.setStyleSheet(u"border-image: url(:/down.png);\n""")
        main_window.wire_up_button.setStyleSheet(u"border-image: url(:/up.png);\n""")
        main_window.wire_down_button.setStyleSheet(u"border-image: url(:/down.png);\n""")
        main_window.wire_clock_button.setStyleSheet(u"border-image: url(:/clock-wise.png);\n""")
        main_window.wire_antiClock_button.setStyleSheet(u"border-image: url(:/anti-clock-wise.png);\n""")
        button_icon_accept, button_icon_disable = QIcon(), QIcon()
        button_icon_disable.addFile(u":/disable.png", QSize(), QIcon.Normal, QIcon.Off)
        button_icon_accept.addFile(u":/accept.png", QSize(), QIcon.Normal, QIcon.Off)
        buttons = [main_window.cath_disable_button, main_window.wire_disable_button, main_window.wire_rot_disable_button]
        for button, state in zip(buttons, global_options["disable_states"]):
            if state:
                button.setIcon(button_icon_disable)
            else:
                button.setIcon(button_icon_accept)

def change_style_dark():
    """切换样式到暗黑"""
    if global_options["skin_mode"] != "MaterialDark":
        global_options["skin_mode"] = "MaterialDark"
        style_file = './resources/QSS/MaterialDark.qss'
        style_sheet = read_qss_file(style_file)
        diaPortAPP.setStyleSheet(style_sheet)
        w.setStyleSheet(style_sheet)
        main_window.cath_up_button.setStyleSheet(u"border-image: url(:/up_dark.png);\n""")
        main_window.cath_down_button.setStyleSheet(u"border-image: url(:/down_dark.png);\n""")
        main_window.wire_up_button.setStyleSheet(u"border-image: url(:/up_dark.png);\n""")
        main_window.wire_down_button.setStyleSheet(u"border-image: url(:/down_dark.png);\n""")
        main_window.wire_clock_button.setStyleSheet(u"border-image: url(:/clock-wise_dark.png);\n""")
        main_window.wire_antiClock_button.setStyleSheet(u"border-image: url(:/anti-clock-wise_dark.png);\n""")
        button_icon_accept, button_icon_disable = QIcon(), QIcon()
        button_icon_disable.addFile(u":/disable_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        button_icon_accept.addFile(u":/accept_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        buttons = [main_window.cath_disable_button, main_window.wire_disable_button, main_window.wire_rot_disable_button]
        for button, state in zip(buttons, global_options["disable_states"]):
            if state:
                button.setIcon(button_icon_disable)
            else:
                button.setIcon(button_icon_accept)

def save_joyset(*args):
    """保存手柄设置"""
    global joy_config_index
    global joy_config_flag
    import json
    with open("joy_config.json", 'r') as js_file:
      temp_robo_options = json.load(js_file)
      joy_config = temp_robo_options  
    if joy_config_flag:  
       if  int(dialog_axis_add.motoSelect.currentIndex())>0: 
          joy_config["default"]["axis"].append(
              [int(dialog_axis_add.motoSelect.currentIndex())-1,
              int(dialog_axis_add.axisSelect.currentText()),
              float(dialog_axis_add.lowAxis.value()),
              float(dialog_axis_add.highAxis.value()),
              float(dialog_axis_add.lowSpeed.value()),
              float(dialog_axis_add.highSpeed.value())])
    else:
      joy_config_flag = True
      if  int(dialog_axis_add.motoSelect.currentIndex()) > 0:
        joy_config["default"]["axis"][joy_config_index] = \
            [int(dialog_axis_add.motoSelect.currentIndex())-1,
            int(dialog_axis_add.axisSelect.currentText()),
            float(dialog_axis_add.lowAxis.value()),
            float(dialog_axis_add.highAxis.value()),
            float(dialog_axis_add.lowSpeed.value()),
            float(dialog_axis_add.highSpeed.value())] 
      else:
          del joy_config["default"]["axis"][joy_config_index]
    with open("joy_config.json", 'w') as js_file:
      js_string = json.dumps(joy_config, sort_keys=True, indent=4, separators=(',', ': '))
      js_file.write(js_string)
    load_joy_options()
    dialog_joy_setting_update(load_joy_options()["default"])

def change_joyset(*args):
    """读取手柄设置函数"""
    import json
    with open("joy_config.json", 'r') as js_file:
      temp_robo_options = json.load(js_file)
      joy_config = temp_robo_options
    dialog_axis_add.motoSelect.setCurrentIndex(joy_config['default']['axis'][dialog_joyconfig.nowSettingShow.currentRow()][0]+1)
    dialog_axis_add.axisSelect.setCurrentText(str(joy_config['default']['axis'][dialog_joyconfig.nowSettingShow.currentRow()][1]))
    dialog_axis_add.lowAxis.setValue(joy_config['default']['axis'][dialog_joyconfig.nowSettingShow.currentRow()][2])
    dialog_axis_add.highAxis.setValue(joy_config['default']['axis'][dialog_joyconfig.nowSettingShow.currentRow()][3])
    dialog_axis_add.lowSpeed.setValue(joy_config['default']['axis'][dialog_joyconfig.nowSettingShow.currentRow()][4])
    dialog_axis_add.highSpeed.setValue(joy_config['default']['axis'][dialog_joyconfig.nowSettingShow.currentRow()][5])
    global joy_config_index
    global joy_config_flag
    joy_config_flag = False
    joy_config_index = dialog_joyconfig.nowSettingShow.currentRow()
    axisAPP.exec()  

def save_options():
    """导出主窗口的配置到文件中"""
    import json as json
    with open("main_config.json", 'w') as js_file:
        js_string = json.dumps(global_options, sort_keys=True, indent=4, separators=(',', ': '))
        js_file.write(js_string)

def load_options():
    """从文件中加载主窗口配置"""
    import json as json
    with open("main_config.json", 'r') as js_file:
        temp_robo_options = json.load(js_file)
    fresh_ports()
    fresh_joystick()

    for key in global_options:
        try:
            temp_robo_options[key]
        except:
            temp_robo_options[key] = global_options[key]

    if temp_robo_options["temp_ports_list"] == global_options["temp_ports_list"]:
        main_window.com_select.setCurrentIndex(temp_robo_options["last_port"])

    if temp_robo_options["temp_joys_list"] == global_options["temp_joys_list"]:
        main_window.joystick_select.setCurrentIndex(temp_robo_options["last_joy"])
    dialog_port.end_select.setCurrentIndex(temp_robo_options["end_char"])

    if temp_robo_options["skin_mode"] == "MaterialDark":
        change_style_dark()
    
    if 0 <= temp_robo_options["gear_level"] <= 5:
        SurgRobot.gear_level = temp_robo_options["gear_level"]
        main_window.gear_level_slider.setValue(temp_robo_options["gear_level"])
    
    for button_id, state in enumerate(temp_robo_options["disable_states"]):
        disable_swicher(button_id, state)


def read_qss_file(qss_file_name):
    with open(qss_file_name, 'r',  encoding='UTF-8') as file:
        return file.read()     
        


def main():
    bind_methods()
    init_methods()
    w.closeEvent = close_methods
    w.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()
    


