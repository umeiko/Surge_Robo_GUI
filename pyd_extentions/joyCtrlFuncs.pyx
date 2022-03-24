from libc.math cimport fabs

cdef float Caxis_shift_cancelling(float axis_value, float fixValue):
    if fixValue > axis_value  > -fixValue:
        axis_value  = 0.
    elif -1. < axis_value  < -1. + fixValue:
        axis_value  = -1.
    elif 1. > axis_value  > 1. - fixValue:
        axis_value  = 1.
    return axis_value


cdef float Cdeal_speed(float axisValue, float speedOld, float k, float b, float fixValue):
    axisValue = Caxis_shift_cancelling(axisValue, fixValue)
    speed = k * axisValue + b if axisValue != 0. else 0.
    if fabs(speed-speedOld) > 2. or (speed==0. and speedOld!=0.):
        return speed
    else:
        return speedOld

cdef float Cdeal_double_speed(float axis1Value, float axis2Value, float speedOld, float k1, float b1, float k2, float b2, float fixValue):
    axis1Value = Caxis_shift_cancelling(axis1Value, fixValue)
    axis2Value = Caxis_shift_cancelling(axis2Value, fixValue)
    speed1 = k1*axis1Value + b1 if axis1Value != 0. else 0.
    speed2 = k2*axis2Value + b2 if axis2Value != 0. else 0.   
    speed = speed1 + speed2      
    if fabs(speed-speedOld) > 2. or (speed==0. and speedOld != 0.):
        return speed
    else:
        return speedOld

def deal_speed(float axisValue, float speedOld, float k, float b, float fixValue):
    return Cdeal_speed(axisValue, speedOld, k, b, fixValue)
def deal_double_speed(float axis1Value, float axis2Value, float speedOld, float k1, float b1, float k2, float b2, float fixValue):
    return Cdeal_double_speed(axis1Value, axis2Value, speedOld, k1, b1, k2, b2, fixValue)