def generate_hint(user_input, correct_answer):
    if user_input < correct_answer:
        print('Your guess is too low!, try again!')
    elif user_input > correct_answer:
        print('Your guess is too high!, try again')

        


if __name__ == '__main__':
    generate_hint(24, 45)