#Longest string
def Longest_word(words):
    longest_string = max(string_list, key=len)
    return longest_string

string_list = ["the","quick","brown", "fox", "ate", "my", "chickens"]
print(Longest_word(string_list))

