#Frame some text
sentence = "My name is snethemba"
def FrameText(words):
    wordlength = len(max(words,key =len))
    print( '*' *(wordlength+4))
    for word in words:
        print('* {a:{b}} *'.format(a=word, b=wordlength))
    print('*' * (wordlength +4))

print(FrameText(sentence.split(" ")))
