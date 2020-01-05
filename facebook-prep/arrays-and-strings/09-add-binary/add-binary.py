import sys

def integerToBinaryConverter(n):
    binaryConversionMap = '01'
    if n < 2:
        return binaryConversionMap[n]
    else:
        return integerToBinaryConverter(n // 2) + binaryConversionMap[n % 2]

def addBinary(a: str, b: str) -> str:
    # first convert strings to binary
    binToIntConverted = []
    for binaryStr in [a, b]:
        binSum = 0
        val = list(reversed(binaryStr))
        for i in range(len(val)):
            binSum += (2**i) * int(val[i])
        binToIntConverted.append(binSum)

    # add integers
    intSum = sum(binToIntConverted)

    # convert result back to binary
    return integerToBinaryConverter(intSum)


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(addBinary(a, b))

    a = '1010'
    b = '1011'
    print(addBinary(a, b))


# Another optimzed way of solving this
# def addBinary(self, a, b) -> str:
#     x, y = int(a, 2), int(b, 2)
#     while y:
#         x, y = x ^ y, (x & y) << 1
#     return bin(x)[2:]
