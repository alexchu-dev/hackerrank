"""
Determine the factors of a number (i.e., all positive integer values that evenly divide into a number) and then return the p(th) element of the list, sorted ascending. If there is no p(th) element, return 0.

Example:
n = 20
p = 3

The factors of 20 in ascending order are {1, 2, 4, 5, 10, 20}. Using 1-based indexing. if p = 3, then 4 is returned. If p > 6, 0 would be returned.

Function Description
Complete the function pthFactor in the editor.
pthFactor has the following parameter(s):
long int n: the integer whose factors are to be found
long int p: the index of the factor to be returned

Returns:
long int the value of the pth integer factor of n or, if there is no factor at that index, then 0 is returned.

Constraints
*  1 <= n <= 10^15
*  1 <= p <= 10^9
"""
def pthFactorEven(n, p):
    factors = []
    power2 = 0
    factors.append(1)
    factors.append(n)
    while (n % 2) == 0:
        power2 += 1
        if (2 ** power2) not in factors:
            factors.append(2 ** power2)
        if (n // 2) not in factors:
            factors.append(n // 2)
        n //= 2
    factors.sort()
    print(factors)
    return factors[p - 1]

print(pthFactorEven(20, 3))
