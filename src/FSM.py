def FSM(orientation, speed):
    # Change states
    state_props = [(0,1,"None"), (1,-1,"None"), (2,1,"Left"), (3,1,"Right"), (4,-1,"Right"), (5,-1,"Left")]
    if FSM.state == 0:
        FSM.state, FSM.throttle_dir, FSM.steer_dir = { \
            "Up":state_props[0], \
            "Down":state_props[1], \
            "Left":state_props[2], \
            "Right":state_props[3]}[orientation]
    elif FSM.state == 1:
        FSM.state, FSM.throttle_dir, FSM.steer_dir = { \
            "Up":state_props[0], \
            "Down":state_props[1], \
            "Left":state_props[4], \
            "Right":state_props[5]}[orientation]
    elif FSM.state == 2:
        FSM.state, FSM.throttle_dir, FSM.steer_dir = { \
            "Up":state_props[0], \
            "Down":state_props[2], \
            "Left":state_props[2], \
            "Right":state_props[3]}[orientation]
    elif FSM.state == 3:
        FSM.state, FSM.throttle_dir, FSM.steer_dir = { \
            "Up":state_props[0], \
            "Down":state_props[1], \
            "Left":state_props[2], \
            "Right":state_props[3]}[orientation]
    elif FSM.state == 4:
        FSM.state, FSM.throttle_dir, FSM.steer_dir = { \
            "Up":state_props[4], \
            "Down":state_props[1], \
            "Left":state_props[4], \
            "Right":state_props[5]}[orientation]
    elif FSM.state == 5:
        FSM.state, FSM.throttle_dir, FSM.steer_dir = { \
            "Up":state_props[0], \
            "Down":state_props[1], \
            "Left":state_props[4], \
            "Right":state_props[5]}[orientation]
    return "%s,%s" % (FSM.steer_dir, FSM.throttle_dir * speed)
FSM.state = 0
FSM.throttle_dir = 1
FSM.steer_dir = "None"
FSM.speed = 0
