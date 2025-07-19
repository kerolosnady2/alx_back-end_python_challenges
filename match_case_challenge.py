'''
This is a simple Game For Guessing A Random Number The Program Do.

You Just Have 3 Tries.

This Program Did With While Loop And Match-Case To Control The Flow.

This Program Has UI For More Readability.

If You Don't Trust That The Program Doesn't Run Effectivly You Can Unhash Line Number 16.
'''
import random

random_number = random.randint(1, 10)

# print(random_number)

guess_number = int(input("Guess The Number => "))

counter = 2

while counter > 0:
    match guess_number:
        case int():
            if guess_number == random_number:
                print(" Ohh, YOU GOT IT!! CONGRATES ")
                break
        
            elif guess_number != random_number:
                print("".center(50,"*"))
                print(" Oops, bad luck. You didn't get it:( ".center(50, "*"))
                print("".center(50,"*"))
                print(" Try Again! ".center(50,"*"))
                print("".center(50,"*"))
                counter -= 1

                guess_number = int(input("Guess The Number => "))

            else:
                break

        case str():
            print("".center(50,"*"))
            print("ITS NOT A NUMBER!!!!!!!!!!")
            break
    
    if counter == 0:
        print("".center(50,"#"))
        print("Your Tries Are Now Zero")
        print("".center(50,"#"))

    print(f"Your Guess Tries Now Are: {counter}")