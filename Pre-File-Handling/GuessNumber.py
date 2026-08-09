import random
l_limit = int(input("From? "))
u_limit = int(input("To? "))    
generated_num = random.randint(l_limit, u_limit)
guessed_num = 0
trials = 0
while guessed_num != generated_num and trials <= 4:
    guessed_num = int(input("Take a guess: "))
    trials = trials + 1
    if guessed_num < generated_num:
        print("Too low!")
    elif guessed_num > generated_num:
        print("Too high!")
    else:
        print("You got it!")   
if guessed_num != generated_num:
    print("You reached the max attempts")
else:
     print("Nice! You took", trials, "attempts")