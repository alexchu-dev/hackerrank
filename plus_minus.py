def plusMinus(my_list):
    """Find the ratio of its elements that are positive, negative, and zero. Print the value in 6 precision.
    Parameters: my_list - A list of numbers including positive, negative, and zero.
    Returns: N/A. It prints the result.
    Exception: N/A.
    """
    pos, neg, zero = 0, 0, 0
    total = len(my_list)
    for num in my_list:     # O(n)
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    print('%.6f' % (pos/total))
    print('%.6f' % (neg/total))
    print('%.6f' % (zero/total))

plusMinus([2, 3, 5, 0])