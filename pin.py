def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isnumeric() is True:
            return True
        else:
            return False
    else:
        return False
validate_pin(pin)

#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
