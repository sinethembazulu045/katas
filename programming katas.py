def hello():
    Name = str(input())
    return Name
print("Hello " + hello())

#Exercise 2 checking if a number is even of odd
def evenOrOdd():
    num = int(input("insert a number you want to check"))
    if(num%2)==0:
        print("{0} is even".format(num))
    else:
        print("{0} is odd" .format(num))
evenOrOdd()

# Drawing a square

def square():
    size =int(input("enter a size number"))
    for i in range(size):
        print ('#' * size)
square()

