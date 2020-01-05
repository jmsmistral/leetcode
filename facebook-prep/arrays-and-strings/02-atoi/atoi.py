import sys

def myAtoi(s: str) -> int:

    # Trim the whitespace from either side of the string
    # check if the first character is an optional + or - symbol (toggle flag for negative values)
    # iterate through each numeric character in reverse and append to a stack
    # pop each character cast to an integer and multiply by the 10^(index + 1) and sum to an accumulator
    cleanString = s.lstrip().rstrip()
    if len(cleanString) == 0:
        return 0

    negativeFlag = False
    if cleanString[0] == '-':
        negativeFlag = True
    if cleanString[0] == '-' or cleanString[0] == '+':
        cleanString = cleanString[1:]

    reverseOrder = []
    for char in cleanString:
        if not char.isnumeric():
            break
        reverseOrder.append(char)
    reverseOrder = reverseOrder[::-1]
    if len(reverseOrder) == 0:
        return 0

    sum = 0
    for i in range(len(reverseOrder)):
        sum += (10 ** i) * int(reverseOrder[i])
    if negativeFlag:
        sum *= -1

    int_max = (2**31) - 1
    int_min = (2**31) * -1
    if sum > int_max:
        return int_max
    if sum < int_min:
        return int_min
    return sum


if __name__ == '__main__':
    s = '   -213.csadasdf   '
    myAtoi(s)
