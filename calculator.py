import time

def multiply(x,y):
    return x*y

def  add(x,y):
    return x+y

def divide(x,y):
    return x/y

def  substract(x,y):
    return x-y

print("This is a simple calculator program.")
print("1 Add.")
print("2 Multiply.")
print("3 Substract.")
print("4 Divide.")
time.sleep(0.5)
while True:
    user_choice = int(input("Select your choice:"))
    if user_choice in(1,2,3,4):
        first_number = float(input("Enter your first number:"))
        time.sleep(0.5)
        second_number = float(input("Enter your second number:"))33
        time.sleep(0.5)
        
        if user_choice==1:
            print(first_number, '+', second_number, '=', add(first_number,second_number))

        elif user_choice==2:
            print(first_number, '*', second_number, '=', multiply(first_number,second_number))

        elif user_choice==3:
            print(first_number, '-', second_number, '=', substract(first_number,second_number))

        elif user_choice==4:
            print(first_number, '/', second_number, '=', divide(first_number,second_number))
        break
    else:
        print("Your input is not valid.")