from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    #forwards state
    if state == 0:
        mycontroller.drive_forwards()

        #odometry based transition condition
        if mycontroller.left_odom.get_count() >= 3500 and mycontroller.right_odom.get_count() >= 3500:
            state = 1
            #reset the odmetry counts
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()

    #turning state
    elif state == 1:
        mycontroller.custom_left_turn(135)
        turns_made+=1
        state=2
    elif state == 4:
        mycontroller.custom_left_turn(120)
        turns_made+=1
        state=2
    elif state == 2:
        mycontroller.drive_forwards()
        #shortfowards state
        if mycontroller.left_odom.get_count() >= 300 and mycontroller.right_odom.get_count() >= 300:
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
            if turns_made < 1:
                state=1
            elif turns_made >=1 and turns_made < 3:
                state=4
            elif turns_made ==3:
                state=3
    elif state == 3:
        mycontroller.stop()
