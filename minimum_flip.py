
def minimum_flip(target):
    """
    The function is to find the minimum of flips required from initial zeros to a string which contains "0"s and "1"s.
    Parameter: target - a string of 0s and 1s.
    Returns: flips - the number of flips required.
    Exception:
    """
    flips = 0
    initial = "0"

    for digit in target:
        if int(digit) > 1:
            print("Input must be 0 or 1, not", digit)
            return -1

        if digit != initial:
            flips += 1
            initial = digit

    return flips

minimum_flip("010101101")