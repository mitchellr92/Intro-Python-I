# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    if(x % 2 == 0):
        print("true")

is_even(4)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def evenNum(num):
    if (num % 2 == 0):
        print("Even!")
    elif (num % 2 != 0):
        print("Odd")

evenNum(num)
