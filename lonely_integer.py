# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# #
# # Complete the 'lonelyinteger' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY a as parameter.
# #

def lonelyinteger(my_list):
    """Find the only integer which is not in a pair.
    Parameters: my_list - A list of numbers which are all in pairs except one.
    Returns: res - The lonely number.
    Exception: Return 0 when all are pairs and no lonely number; Return a result of Bitwise XOR if more than 1 lonely
    number. Otherwise, assume user's input is correct.
    """
    res = 0
    for num in my_list:     # O(n)
        res ^= num          # Bitwise operation
    return res

print(lonelyinteger([1,3,5,3,1]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     a = list(map(int, input().rstrip().split()))
#
#     result = lonelyinteger(a)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
