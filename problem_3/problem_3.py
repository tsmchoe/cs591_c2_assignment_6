# Problem 3 (String multiplication):
# Given 2 non-negative integers, num1 and ,num2, return the product of num1 and num2, also represented as a string. 
# You must use TDD to develop your solution. State any assumptions you make about the input and edge-cases. 
# NB: you may not use library functions to cast strings to integers, or vice-versa.

def string_multiplication(num1, num2):
    # returns the product of num1 and num2, represented as a string.
    # assuming that only non-negative integers inputed
    int1 = 0
    int2 = 0
    base = 1
    len1 = len(num1)
    len2 = len(num2)

    for element in num1:
        if element == "1":
            digit = 1
        elif element == "2":
            digit = 2
        elif element == "3":
            digit = 3
        elif element == "4":
            digit = 4
        elif element == "5":
            digit = 5
        elif element == "6":
            digit = 6
        elif element == "7":
            digit = 7
        elif element == "8":
            digit = 8
        elif element == "9":
            digit = 9
        elif element == "0":
            digit = 0
        #find base
        for i in range(len1-1):
                base = base * 10
        if digit != 0:
            int1 = int1 + (digit * (base))
        base = 1
        len1 = len1 - 1

    for element in num2:
        if element == "1":
            digit = 1
        elif element == "2":
            digit = 2
        elif element == "3":
            digit = 3
        elif element == "4":
            digit = 4
        elif element == "5":
            digit = 5
        elif element == "6":
            digit = 6
        elif element == "7":
            digit = 7
        elif element == "8":
            digit = 8
        elif element == "9":
            digit = 9
        elif element == "0":
            digit = 0
        #find base
        for i in range(len2-1):
                base = base * 10
        if digit != 0:
            int2 = int2 + (digit * (base))
        base = 1
        len2 = len2 - 1

    num_result = int1 + int2

    # convert result into string
    str_result = []
    while True:
        str_result.append(chr(ord('0') + num_result % 10))
        num_result = num_result // 10
        if num_result == 0:
            break
    return ''.join(reversed(str_result))
