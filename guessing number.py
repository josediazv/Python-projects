import time
import random
attempts = 5
random = random.randint(1,10)
print(f"This is a guessing number game, you have {attempts} attempts")
time.sleep(0.5)
for i in range(attempts):
    
    usernumber=int(input("Enter a number:"))

    if usernumber == random:
        print("Correct, you won")
        break
    elif usernumber > random:
        print(f"Your number ({usernumber}) is higher than the random. You have {attempts-1} attempts left.")
        attempts -=1
    elif usernumber < random:
        print(f"Your number ({usernumber}) is lower than the random. You have {attempts-1} attempts left.")
        attempts -=1
    if attempts==0:    
        print("You ran out of attempts")
    continue
