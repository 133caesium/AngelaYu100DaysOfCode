
def helloWorld():
    print("Hello World!")

def band_name_generator():
    print("Welcome to the band name generator.")
    city = input("Which city did you grow up in?\n")
    pet = input("What is the name of a pet?\n")
    print("Your band name could be "+city+" "+pet)

if __name__ == '__main__':
    helloWorld()
    band_name_generator()