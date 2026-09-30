def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)

    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 180)
    gimbal_ctrl.recenter()

    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)