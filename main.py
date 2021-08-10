
def helloWorld():
    print("Hello World!")

def band_name_generator():
    print("Welcome to the band name generator.")
    city = input("Which city did you grow up in?\n")
    pet = input("What is the name of a pet?\n")
    print("Your band name could be "+city+" "+pet)

def name_length_calculator():
    name = input("What is your name?\n")
    print("Your name is "+str(len(name))+" characters long.")

if __name__ == '__main__':
    helloWorld()
    name_length_calculator()
    band_name_generator()