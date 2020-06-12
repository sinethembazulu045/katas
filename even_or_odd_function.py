
#even or odd function that checks if the number is odd or even number
def odd_or_even(num): # where num can be even or odd number of my choice.
    if(num%2)==0:
        return num, "is even number"
    else:
        return num, "is odd number"
check =odd_or_even(3)
print(check)
