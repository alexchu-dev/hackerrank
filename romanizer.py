def romanizer(numbers):
    # Write your code here
    arabic_roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    def arabic_to_roman(num):
        res = ''
        for value in sorted(arabic_roman.keys(), reverse=True):
            while num >= value:
                res += arabic_roman[value]
                num -= value
        return res

    final_roman = [arabic_to_roman(num) for num in numbers]
    return final_roman


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = romanizer(numbers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
