from utils.input_validator import get_valid_input
from game_logic.hint_generator import generate_hint
from utils.random_generator import random_generator
from game_logic.score_calculator import scorer





def main():
    correct_answer = random_generator(1, 100)
    print (correct_answer)
    scorerClass = scorer()

    while True:
        user_input = get_valid_input(1, 100)
        
        if user_input == correct_answer:
            print('That''s it, you guessed correctly!')
            print(scorerClass.get_score())
            repeat = input('Do you want to play again? (y/n): ')
            if repeat == 'y':
                main()
            else:
                break

        else:
            
            generate_hint(user_input, correct_answer)
            scorerClass.decrement_score()

if __name__ == '__main__':
    main()

