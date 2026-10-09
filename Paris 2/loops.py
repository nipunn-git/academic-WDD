def main():
    print_square(5)

def print_square(size):
    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #print brick
            print("#", end="")
        
        #print new line
        print()

main()

#for loop example
for i in range(3):  # for i in range(1,6+1,2) it means that i will start at 1 and go up to 6 in increments of 2 
    print("meow")

#while loop example
i=0
while i<5: #i goes from 0 to 4, so it will print "meow" 5 times
    print("meow")
    i+=1

#for each loop example
myFruitsList = ["apple", "banana", "cherry", "kiwi", "mango"]
for fruit in myFruitsList:
    print(fruit)

#for each loop example with range
for i in range(len(myFruitsList)):
    print(myFruitsList[i])

#for each loop is also known as traversal, because it traverses through the list and prints each element in the list.