
#even or odd function
def odd_or_even(num): # where num can be even or odd number of my choice.
    even_output ="{0} is even".format(num)
    odd_output ="{0} is odd" .format(num)
    if(num%2)==0:
        return even_output
    else:
        return odd_output
check =odd_or_even(3)

print(check)
