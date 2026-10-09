def isLeap(n):
    if (n%400==0) or (n%4==0 and n%100!=0):
        print(f"{n} is a leap year")
    else:
        print(f"{n} is not a leap year")

def main():
    year=int(input("Enter a year: "))
    isLeap(year)
main()

# *args
def find_largest(*args):
    if not args:
        return None
    return max(args)
print("Largest of 2 numbers:", find_largest(10, 25))
print("Largest of 3 numbers:", find_largest(5, 89, 12))
print("Largest of 5 numbers:", find_largest(100, 45, 300, 12, 98))

# **kwargs
def display_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("User 1 Information:")
display_user_info(name="Alice", age=25, city="New York")

print("\nUser 2 Information:")

#fibo
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
fib_10 = [fibonacci(i) for i in range(10)]
squared_fib = list(map(lambda x: x**2, fib_10))
print("First 10 Fibonacci numbers:", fib_10)
print("Square of first 10 Fibonacci numbers:", squared_fib)