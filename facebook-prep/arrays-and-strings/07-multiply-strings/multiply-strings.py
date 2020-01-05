import sys

def convertIntToString(num):
    intToStringConversionMap = '0123456789'
    if num < 10:
        return intToStringConversionMap[num]
    else:
        return convertIntToString(num // 10) + intToStringConversionMap[num % 10]

def multiply(num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0':
        return '0'
    stringConvertedValues = []
    for stringVal in [num1, num2]:
        valArray = stringVal.split()
        valArray.reverse()
        intVal = 0
        for i in range(len(valArray)):
            intVal += (10**i) * int(valArray[i])
        stringConvertedValues.append(intVal)
    multIntVal = 1
    if len(stringConvertedValues):
        for intVal in stringConvertedValues:
            multIntVal *= intVal
        return convertIntToString(multIntVal)
    return '0'


if __name__ == '__main__':
    num1 = '20'
    num2 = '30'
    print(multiply(num1, num2))

    num1 = '0'
    num2 = '1'
    print(multiply(num1, num2))

    num1 = '0'
    num2 = '1'
    print(multiply(num1, num2))
