#
# Complete the 'betterCompression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def betterCompression(s):
    # Write your code here
    """
    Receiving a string like a1b3c1k1a2c5k3, output would be "a3b3c6k4" which adds up the occurrence of the alphabets.
    Parameter: s - the string to compress
    Returns: ret - the properly compressed string with combined count
    Exception: Assumed user input is correct and not a negative because e.g. '-9' was input, the minus is a char in here.

    Consider a string, S, that is a series of characters, each followed by its frequency as an integer.
    The string is not compressed correctly, so there may be multiple occurrences of the same character.
    A properly compressed string will consist of one instance of each character in alphabetical order followed by the
    total count of that character within the string.

    Example:
    The string 'a3c9b2c1 'has two instances where 'd is followed by a count: once with 9 occurrences,
    and again with 1. It should be compressed to 'a3b2c10'!

    Constraints
    *   1s size of S ≤ 100000
    *   'a's characters in S≤'z
    *   1s frequency of each character in S ≤ 1000
    """
    temp = {}
    length = len(s)
    i = 0
    while i < length:
        character = s[i]
        i += 1
        count = 0

        if s[i] == '-':
            return "Error input, cannot be negative"

        while i < length and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1

        if character in temp:
            temp[character] += count
        else:
            temp[character] = count

    ret = ''

    for character in sorted(temp.keys()):
        ret += character + str(temp[character])

    return ret


print(betterCompression("a1b2c3a2b4"))
