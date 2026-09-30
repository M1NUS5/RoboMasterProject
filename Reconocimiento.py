def start():
    robot_ctrl.set_mode(rm_define.robot_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_on)
    
    vision_ctrl.cond_wait(rm_define.cond_recononized_marker_number_one)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    gimbal_ctrl.rotate_witch_degree(rm_define.gimball_right, 45)
    
    vision_ctrl.cond.wait(rm_define.cond_reconized_marker_number_two)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)
    gimbal_ctrl.recenter()