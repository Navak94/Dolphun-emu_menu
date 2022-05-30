from __future__ import print_function


from inputs import get_gamepad


def main():
    """Just print out some event infomation when the gamepad is used."""
    x = 0
    analog_info=""
    menu_info =""
    while 1:
        
        events = get_gamepad()
        for event in events:
            #print(event.ev_type, event.code, event.state)
            analog_info = str(event.code)
            analog_info= analog_info.replace("ABS_","").replace("SYN_REPORT0","")
            analogState = str(event.state)
            menu_info = analog_info + analogState
            menu_info= menu_info.replace("SYN_REPORT0","")
            if "Y" or "X" in analog_info:
                print(menu_info)
                

            
if __name__ == "__main__":
    main()
