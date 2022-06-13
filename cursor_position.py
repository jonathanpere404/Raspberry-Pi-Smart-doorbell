from pynput.mouse import Button, Controller

def mouse_pos(old_pos):
    mouse = Controller()
    current_mouse_position = mouse.position
    if(old_pos != current_mouse_position):
        return (True)
    else:
        return (False)

