import serial.tools.list_ports

def check_usb_port_enabled():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'USB' in port.description:
            return True
    return False

# Example usage
is_usb_enabled = check_usb_port_enabled()
print("USB port enabled:", is_usb_enabled)
