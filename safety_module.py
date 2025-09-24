def apply_safety(action):
    if action in ["reverse", "turn_left", "turn_right", "move_forward"]:
        return action
    return "stop"