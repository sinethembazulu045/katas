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
    size = int(input("enter a size number"))
    for i in range(size):
        print ('#' * size)
square()

#Drawing a right angle triangle

def right_angle_triangle():
    num = int(input("number of raws: "))
    for i in range( num):
        for j in range( i+1):
            print("#", end ="")
        print("")
right_angle_triangle()

#drawing iscosceles triangle
def iscoscelsTri():
    num = int(input("number of raws: "))
    for i in range(1,num+1):
        print((num-i) * ' '+ i *'# ')
iscoscelsTri()

#finding the longest string in an array/lius
def Longestword(word):
    print("longest word:")
    words = list(word.split(" "))
    lenght =[]
    for i in words:
        lenght.append(len(i))
    LongestString = max(lenght)
    returnlist = []
    for j in words:
        if len(j)==LongestString:
            returnlist.append(j)
            list_word = j
            print(list_word)
Longestword(input('enter your sentence'))

# concanetion of lists
def concanetion():
    list1 =[]
    list2 =[]
    orderlist1 = input("enter your orderedlist1").split(" ")
    list1 = orderlist1

    orderlist2 = input("enter your orderedlist2").split(" ")
    list2 = orderlist2
    
    i = len(list1)
    stored_list =[]
    for j in range(i):
        stored_list.append(list1[j])
        stored_list.append(list2[j])
    print(stored_list)
concanetion()




