def plusMinus(arr):
    # Write your code here
    pos, neg, zero = 0, 0, 0
    total = len(arr)
    for num in arr:
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