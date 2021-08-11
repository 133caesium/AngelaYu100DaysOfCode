
def sum_digits(twoDigitNumber):
    if type(twoDigitNumber) != int:
        raise AttributeError("I need a number to work!")
    if (twoDigitNumber>99 or twoDigitNumber<10):
        raise ValueError("The number is too big or too small!")
    first_digit = int(str(twoDigitNumber)[0])
    second_digit = int(str(twoDigitNumber)[1])
    sum_of_digits = first_digit+second_digit
    return sum_of_digits

if __name__ == '__main__':
    print(sum_digits(10))