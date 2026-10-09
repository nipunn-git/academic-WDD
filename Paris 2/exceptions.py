try:
    x = int(input("Enter a number: "))
    print(f"You entered: {x}")

except ValueError:
    print("That's not a valid number. Please enter an integer.")

##############         OR        ##############

try:
    x=int(input("Enter a number: "))
except ValueError:
    print("x is not an integer.")        
else:
    print(f"x is {x}")

#BASICALLY Except acts like "if" and "try" acts like condition

##############         OR        ##############

while True:
    try:
        x=int(input("Enter x: "))
    except ValueError:
        print("x aint an integer.")
    else:
        break

print(f"x is {x}")