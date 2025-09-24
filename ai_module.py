def anomaly_detection(data):
    if data.get("wheel_status") == "stuck":
        return "reverse"
    elif data.get("obstacle") == True:
        return "turn_left"
    return "move_forward"