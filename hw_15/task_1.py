# Ex.1 Loops
# Написать цикл, который опрашивает пользователя и
# выводит рандомное число.
# Цикл должен прерываться по символу Q(q)


from random import randint
from typing import Dict


def get_random_number() -> None:
    """Output for user random number

    :return: None
    """

    text_for_user: Dict[str, str] = {'entry': 'Do you need a randon number from 1 to 100?',
                                     'rule': 'If you need a number enter "Y" or enter "Q" to exit: ',
                                     'next': 'Do you need next random number (Y/Q): ',
                                     'result': f'This is your random number:',
                                     'exit': 'Bye',
                                     'error': 'Please enter "Y" or "Q": ',
                                     }
    print(text_for_user['entry'])
    question = 'rule'

    while True:
        user_answer = input(text_for_user[question]).lower()
        give_numb = user_answer == 'y'
        exit_loop = user_answer == 'q'
        if give_numb:
            rand_numb = randint(1, 100)
            print(text_for_user['result'], rand_numb)
            question = 'next'
        elif exit_loop:
            print(text_for_user['exit'])
            break
        else:
            question = 'error'


if __name__ == '__main__':
    get_random_number()
