def get_valid_input(start, end):
    while True:
        try:
            user_input = int(input('input a valid number: '))
            if start <= user_input <= end:
                return user_input 
            else:
                print(f'Please input a number between {start} and {end}')
                continue
        except:
            print("This is not a number, Please input a valid number")
            continue


if __name__ == '__main__':
    get_valid_input(1, 100)
    

