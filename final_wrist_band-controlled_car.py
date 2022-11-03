import modi
import time
# modi.update_module_firmware()
bundle1 = modi.MODI(
    conn_type= 'ble',
    network_uuid='3D39547C'
)
bundle2 = modi.MODI(
    conn_type= 'ble',
    network_uuid='43A9C65B'
)
gyro = bundle1.gyros[0]
motor1=bundle2.motors[0]
# motor2=bundle2.motors[1]

def saturate(x):
    if x>100: return 100
    if x<-100: return -100
    return x

def go_forward(x=100):
    if x > 100:
        x = 100
    motor1.speed = -x, x
    # motor2.speed = -x, x
    # time.sleep(sec)
    # stop_car()
def rotate_right(x):
    '''
        -100, -100
        -100, -100
        For rotate right by some degree
    '''
    if x > 100:
        x = 100
    motor1.speed = -x, -x
    # motor2.speed = -x, -x

def rotate_left(x):
    '''
        100, 100
        100, 100
        For rotate left by some degree
    '''
    if x > 100:
        x = 100
    motor1.speed = x, x
    # motor2.speed = x, x
def stop_car():
    '''
    Stop the car by making the speed 0
    '''
    motor1.speed = 0, 0
    # motor2.speed = 0, 0

def testgyro():
    gyro_pitch = gyro.pitch
    gyro_roll = gyro.roll
    gyro_yaw = gyro.yaw
    print("gyro_pitch:", gyro.pitch, "gyro_roll:", gyro.roll, "gyro_yaw", gyro.yaw)
    time.sleep(0.1)
while True:
    gyro_pitch = gyro.pitch
    gyro_roll = gyro.roll
    if gyro_pitch > 30 and abs(gyro_pitch) > abs(gyro_roll):
        go_forward(saturate(abs(gyro_pitch)/90 * 100))
    elif gyro_pitch < -30 and abs(gyro_pitch) > abs(gyro_roll):
        go_forward(saturate(-abs(gyro_pitch)/90 * 100))
    elif gyro_roll > 30 and abs(gyro_pitch) < abs(gyro_roll):
        rotate_right(saturate(abs(gyro_roll)/90 * 100))
    elif gyro_roll < -30 and abs(gyro_pitch) < abs(gyro_roll):
        rotate_left(saturate(abs(gyro_roll)/90 * 100))
    else:
        stop_car()
    # testgyro()