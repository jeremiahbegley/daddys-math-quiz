"""
2-Minute Drill: Arithmetic Facts
Originally created on 16 Sep 2023
@author: Jeremiah Begley
"""

# libraries
import random
import time

def user_chooser(n):
    error_msg = 'Invalid input. Please try again.'
    while True:
        try:
            user_input = int(input())
            if user_input>=1 and user_input<=n:
                return user_input
            else:
                print(error_msg)
        except ValueError:
            print(error_msg)

def user_chooser_bool():
    error_msg = 'Invalid input. Please try again.'
    while True:
        try:
            user_input = int(input())
            if user_input==1:
                return True
            if user_input==0:
                return False
            else:
                print(error_msg)
        except ValueError:
            print(error_msg)

class Operation:
    def __init__(self, operation, op_char):
        pass


def addition(max_addend=10):
    x = random.randint(0,max_addend)
    y = random.randint(0,max_addend)
    n = x + y
    while True:
        try:
            ans = int(input(f'{x} + {y} = '))
            if ans == n:
                print('Correct!\n')
                return True
            else:
                print(f'* INCORRECT *\n{x} + {y} = {n}\n')
                return False
        except ValueError:
            print('That wasn\'t a number! Please try again!')

def subtraction(max_minuend=20):
    x = random.randint(0,max_minuend)
    y = random.randint(0,x)
    n = x - y
    while True:
        try:
            ans = int(input(f'{x} - {y} = '))
            if ans == n:
                print('Correct!\n')
                return True
            else:
                print(f'* INCORRECT *\n{x} - {y} = {n}\n')
                return False
        except ValueError:
            print('That wasn\'t a number! Please try again!')

def multiplication(max_factor=12):
    x = random.randint(0,max_factor)
    y = random.randint(0,max_factor)
    n = x * y
    while True:
        try:
            ans = int(input(f'{x} * {y} = '))
            if ans == n:
                print('Correct!\n')
                return True
            else:
                print(f'* INCORRECT *\n{x} * {y} = {n}\n')
                return False
        except ValueError:
            print('That wasn\'t a number! Please try again!')

def division(max_factor=12):
    quotient = random.randint(0,max_factor)
    divisor = random.randint(1,max(quotient,1))
    dividend = quotient * divisor
    while True:
        try:
            ans = int(input(f'{dividend} / {divisor} = '))
            if ans == quotient:
                print('Correct!\n')
                return True
            else:
                print(f'* INCORRECT *\n{dividend} / {divisor} = {quotient}\n')
                return False
        except ValueError:
            print('That wasn\'t a number! Please try again!')

while True:
    #initializing variables
    timer = 120 # 2 minutes
    num_correct = 0
    num_incorrect = 0

    #opening dialogue
    print('\nWelcome to Daddy\'s Math Quiz!\n\nPlease PRESS 1 for addition\nPlease PRESS 2 for subtraction\nPlease PRESS 3 for multiplication\nPlease PRESS 4 for division\nPlease PRESS 5 for CHOMMY MODE')
    choice = user_chooser(5)
    if choice==1:
        print('\nThis is 2-Minute Drill: Addition Facts 0-20. Press ENTER to begin.')
        input()
        timeout = time.time() + timer
        #this loop provides questions until time expires:
        while time.time() < timeout:
            if addition(10):
                num_correct += 1
            else:
                num_incorrect += 1
            print(f'{num_correct} right, {num_incorrect} wrong so far. {int(round(timeout-time.time(),0))} seconds left.\n\n\n')
        print(f'\n\nTime\'s up! You got {num_correct} questions right and {num_incorrect} wrong - that\'s {int(100*(round(num_correct/(num_correct+num_incorrect),2)))}%!')

    elif choice==2:
        print('\nThis is 2-Minute Drill: Subtraction Facts 0-20. Press ENTER to begin.')
        input()
        timeout = time.time() + timer
        #this loop provides questions until time expires:
        while time.time() < timeout:
            if subtraction(20):
                num_correct += 1
            else:
                num_incorrect += 1
            print(f'{num_correct} right, {num_incorrect} wrong so far. {int(round(timeout-time.time(),0))} seconds left.\n\n\n')
        print(f'\n\nTime\'s up! You got {num_correct} questions right and {num_incorrect} wrong - that\'s {int(100*(round(num_correct/(num_correct+num_incorrect),2)))}%!')
    
    elif choice==3:
        print('\nThis is 2-Minute Drill: Multiplication Tables 0-12. Press ENTER to begin.')
        input()
        timeout = time.time() + timer
        #this loop provides questions until time expires:
        while time.time() < timeout:
            if multiplication(12):
                num_correct += 1
            else:
                num_incorrect += 1
            print(f'{num_correct} right, {num_incorrect} wrong so far. {int(round(timeout-time.time(),0))} seconds left.\n\n\n')
        print(f'\n\nTime\'s up! You got {num_correct} questions right and {num_incorrect} wrong - that\'s {int(100*(round(num_correct/(num_correct+num_incorrect),2)))}%!')

    elif choice==4:
        print('\nThis is 2-Minute Drill: Division Facts 0-12. Press ENTER to begin.')
        input()
        timeout = time.time() + timer
        #this loop provides questions until time expires:
        while time.time() < timeout:
            if division(12):
                num_correct += 1
            else:
                num_incorrect += 1
            print(f'{num_correct} right, {num_incorrect} wrong so far. {int(round(timeout-time.time(),0))} seconds left.\n\n\n')
        print(f'\n\nTime\'s up! You got {num_correct} questions right and {num_incorrect} wrong - that\'s {int(100*(round(num_correct/(num_correct+num_incorrect),2)))}%!')

    else:
            print('\nThis is SUBTRACTION - CHOMMY MODE (6). Press ENTER to begin.')
            input()
            timeout = time.time() + timer
            #this loop provides questions until time expires:
            while time.time() < timeout:
                if subtraction(6):
                    num_correct += 1
                else:
                    num_incorrect += 1
                print(f'{num_correct} right, {num_incorrect} wrong so far. {int(round(timeout-time.time(),0))} seconds left.\n\n\n')
            print(f'\n\nTime\'s up! You got {num_correct} questions right and {num_incorrect} wrong - that\'s {int(100*(round(num_correct/(num_correct+num_incorrect),2)))}%!')


    #keeps the program from closing when it ends
    input('\nPlease press ENTER to proceed.')
