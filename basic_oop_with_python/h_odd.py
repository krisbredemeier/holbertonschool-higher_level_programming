'''
function odd(x) that returns 1 if the number is odd, 0 otherwise
'''
def odd(x):
    if x == 0:
        return False
    elif x == 1:
        return True
    else:
        return not odd(x-1)
