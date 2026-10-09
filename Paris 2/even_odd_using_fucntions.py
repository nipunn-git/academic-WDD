def main():
    n = int(input("Enter a number: "))
    if is_even(n):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n%2==0 else False

    """ OR

    if n % 2 == 0:
        return True
    else:
        return False

    """
main()