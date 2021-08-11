
def sum_digits(twoDigitNumber):
    if type(twoDigitNumber) != int:
        raise AttributeError("I need a number to work!")
    if (twoDigitNumber>99 or twoDigitNumber<10):
        raise ValueError("The number is too big or too small!")
    first_digit = int(str(twoDigitNumber)[0])
    second_digit = int(str(twoDigitNumber)[1])
    sum_of_digits = first_digit+second_digit
    return sum_of_digits

def body_mass_index_calculator():
    height = float(input("enter your height in m:   "))
    weight = int(input("enter your weight in kg:  "))
    BMI = round((weight/height**2))
    print("Your BMI is "+str(BMI))
    return BMI

if __name__ == '__main__':
    print(sum_digits(10))
    body_mass_index_calculator()