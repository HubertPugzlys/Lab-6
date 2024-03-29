# Hubert Pugzlys

def encode(password):
    password_list = list(password)
    new_password = ''
    for value in password_list:
        value = int(value) + 3
        new_password += str(value)

    return new_password
def decode(new_password):
    password_list = list(new_password)
    original_password = ''
    for value in new_password:
        value = int(value) - 3
        original_password += str(value)
    return original_password


def main():
    running = True
    encoded_password = ''
    password = ''
    while running:
        print('''Menu  
------------- 
1. Encode  
2. Decode  
3. Quit\n''')

        user_selection = int(input('Please enter an option: '))
        if user_selection == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif user_selection == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n')
        else:
            break


if __name__ == '__main__':
    main()

