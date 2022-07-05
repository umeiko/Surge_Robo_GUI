"""
提供手柄信号处理的模块
"""
def axis_shift_cancelling(axis_value:float, fixValue:float)->float:
    """手柄的漂移补偿"""
    if fixValue > axis_value  > -fixValue:
        axis_value  = 0.
    elif -1. < axis_value  < -1. + fixValue:
        axis_value  = -1.
    elif 1. > axis_value  > 1. - fixValue:
        axis_value  = 1.
    return axis_value

def deal_speed(axisValue:float, speedOld:float, k:float, b:float, fixValue:float)->float:
    """对手柄信号进行简易滤波"""
    axisValue = axis_shift_cancelling(axisValue, fixValue)
    speed = k * axisValue + b if axisValue != 0. else 0.
    if abs(speed-speedOld) > 2. or (speed==0. and speedOld!=0.):
        return speed
    else:
        return speedOld

def deal_double_speed(axis1Value:float, axis2Value:float, speedOld:float, k1:float, b1:float, k2:float, b2:float, fixValue:float)->float:
    """对手柄信号进行简易滤波, 但是同时处理两个手柄轴的速度"""
    axis1Value = axis_shift_cancelling(axis1Value, fixValue)
    axis2Value = axis_shift_cancelling(axis2Value, fixValue)
    speed1 = k1*axis1Value + b1 if axis1Value != 0. else 0.
    speed2 = k2*axis2Value + b2 if axis2Value != 0. else 0.   
    speed = speed1 + speed2      
    if abs(speed-speedOld) > 2. or (speed==0. and speedOld != 0.):
        return speed
    else:
        return speedOld