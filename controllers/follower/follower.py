from controller import Robot
robot = Robot()
TIME_STEP = 32
MAX_SPEED = 6.28

left_wheel = robot.getDevice('left wheel')
right_wheel = robot.getDevice('right wheel')
left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
left_wheel.setVelocity(0.0)
right_wheel.setVelocity(0.0)

left_ds = robot.getDevice('ds_l')
left_ds.enable(TIME_STEP)
right_ds = robot.getDevice('ds_r')
right_ds.enable(TIME_STEP)
front_ds = robot.getDevice('ds_m')
front_ds.enable(TIME_STEP)

while robot.step(TIME_STEP)!= -1:
    left_ds_value = left_ds.getValue()
    right_ds_value = right_ds.getValue()
    front_ds_value = front_ds.getValue()
    
    left_speed = 0.6 * MAX_SPEED 
    righ_speed = MAX_SPEED * 0.6
    
    if front_ds_value > 200 and front_ds_value < 760 or min(front_ds_value, left_ds_value, right_ds_value) > 160 :
        print("Prosto")
    elif left_ds_value > right_ds_value + 10 and 200 < left_ds_value < 760:
        print("Lewo")
        left_speed = 0.6 * -MAX_SPEED 
    elif right_ds_value > left_ds_value + 10 and 200 < right_ds_value < 760:
        print("Prawo")
        righ_speed = -MAX_SPEED * 0.6
        
    left_wheel.setVelocity(left_speed)
    right_wheel.setVelocity(righ_speed)






