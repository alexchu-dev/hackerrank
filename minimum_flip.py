
def minimum_flip(target):
    """
    The function is to find the minimum of flips required from initial zeros to a string which contains "0"s and "1"s.
    Parameter: target - a string of 0s and 1s.
    Returns: flips - the number of flips required.
    Exception:

    Start with an initial string of zeros. Choose any digit to flip. When a digit is flipped, its value and those to the right switch state between 0 and 1. Given a target string of binary digits, determine the minimum number of flips required to achieve the target.

    Example:
    target = 01011
    Start with a string of 5 zeros, the same length string as the target.
    Initial String -> 00000
    Flip the 3rd digit -> 00111
    Flip the 2nd digit -> 01000
    Flip the 4th digit > 01011
    3 flips are required to reach the target. The return value is 3.
    Function Description
    Complete the function minimumFlips in the editor below.
    minimum Flips has the following parameter(s): string target: a string of Os and 1s to match
    Returns:
    int: the minimum number of flips needed to obtain the target string
    Constraints
    *   1 ≤ length of target ≤ 105
    *   0 ≤ target[i] ≤ 1
    *   The target string consists of digits 0 and 1
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

print(minimum_flip("010101101"))