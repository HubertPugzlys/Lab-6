def encode(password):
    password_list = list(password)
    new_password = ''
    for value in password_list:
        value += 3
        new_password += value

    return new_password


def main():
    running = True
    newVar = 123
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
        if user_selection == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')




if __name__ == '__main__':
    main()

