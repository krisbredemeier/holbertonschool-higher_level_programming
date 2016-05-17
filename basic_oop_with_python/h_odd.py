def odd(x):
    if x == 0:
        return False
    elif x == 1:
        return True
    else:
        return not odd(x-1)
