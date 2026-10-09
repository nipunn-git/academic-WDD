def main():
    name = input("What is your name? ")
    hello(name)
    hello() #will print Hello, World because no argument is passed and default value is used


def hello(name="World"): #world is default value
    print("Hello,", name)

main()