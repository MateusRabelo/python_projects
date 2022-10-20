import random

def guess(x):
    
    random_num = random.randint(0, x)
    
    for i in range(10):
        user_guess = int(input("\nWhat is your guess? "))
        if user_guess < random_num:
            print("\nToo low man, try again more high :)", end='')
        elif user_guess > random_num:
            print("\nHey hey hey, keep calm, guess more low ;)", end='')
        elif user_guess == random_num:
            print("\nOkay okay, i lost and you win, you found my number\n")
            break
        else:
            print("\nError - incorrect option", end='')
            
        
        
def main():
    x = int(input("\nWhat is the max limit? "))
    guess(x)
    
main()