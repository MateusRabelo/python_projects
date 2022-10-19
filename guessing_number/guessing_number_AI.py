import random

# função que não cheguei a usar
def random_number_range(min_number, max_number):
    random.randint(min_number, max_number)
    return min_number, max_number


#função que faz o computador palpitar um número
def computer_guess(num_max):
    #variáveis
    random_num = random.randint(0, num_max)
    random_num_min = 0
    random_num_max = num_max
    opt = 'a'
    
    # Entrada das alternativas pela primeira vez
    print('\nis {}? (H) too high, (L) too low, and (C) Correct'.format(random_num), end=' | ')
    while opt != 'c' or opt != 'C':
        
        opt = str(input())
        if random_num_max == random_num_min or random_num_min == random_num_max:
            print("\nYour number is {}. I know, don't try to joke me.\n".format(random_num))
            break
        
        elif opt == 'H' or opt == 'h':
            random_num_max = random_num
            #print("\nJoin 'too high' option\n")
            print("\nThe number there's between", random_num_min ,"e", random_num_max)
            random_num = random.randint(random_num_min, random_num_max)
            print('Is {}? (H) too high,(L) too low, and (C) Correct'.format(random_num), end=' | ')
    
        elif opt == 'L' or opt == 'l':
            random_num_min = random_num
            #print("\nJoin 'too low' option\n")
            print("\nthe number there's between", random_num_min ,"e", random_num_max)
            random_num = random.randint(random_num_min, random_num_max)
            print('Is {}? (H) too high,(L) too low, and (C) Correct'.format(random_num), end=' | ')
    
        elif opt == 'C' or opt == 'c': 
            print('Yeah, i "acertei" :)')
            break
        
        else:
            print("ERROR - Incorrect option.")
            print('Please, input the correct alternative: (H) high, (L) too low or (C) Correct')
            
    final_answer = str(input(("Let's try again? [s/n]\n")))
    if final_answer == 's':
        computer_guess(num_max = int(input(("Até onde vai seu número? (port to english after) "))))
    else: print("\nBye man! Thank's for the experience ;)")
        

def main():
    char = str(input(("Whats'up man, can i guess the number you're thinking? [s/n] ")))

    if char == 's' or 'S':
        print("Okay, let's play!")
        
        #num_min = int(input("Qual o valor mínimo do seu número? "))
        num_max = int(input(("Até onde vai seu número? (port to english after) ")))
        computer_guess(num_max)
        
        
    else: print("...\nOkay, goodbye :(")
    
    
main()