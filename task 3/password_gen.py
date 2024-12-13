import random

class Passwordgenerator:
    def __init__(self):
        self.__password_characters = [
            # Lowercase letters
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

            # Uppercase letters
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

            # Digits
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

            # Special characters
            '@', '#', '$', '&', '.'
        ]
        self.generate()

    def generate(self):
        a = input("Do you want to generate a password (yes/no): ").strip().lower()
        if a == 'yes':
            self.function()
        elif a == 'no':
            print("Exiting program.")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.generate()

    def function(self):
        try:
            length = int(input("Enter the length of the password you want: "))
            if length <= 0:
                print("Password length must be a positive number.")
                self.function()
                return

            random.shuffle(self.__password_characters)

            __pc = [random.choice(self.__password_characters) for _ in range(length)]
            __gen_password = ''.join(__pc)

            print("Generated Password: ", __gen_password)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.function()

obj = Passwordgenerator()