def is_numeric(message):
    try:
        float(message)
        return True
    except ValueError:
        return False

def is_positive_number(message):
    if float(message) <= 0:
        return False
    else:
        return True
    