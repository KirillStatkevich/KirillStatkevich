# word=input("input your string:\n")
word="ylibok tebe ded makar"
def recursive_string(text,i=0):
    if i==10:
        return print(text[::-1])
    print(text[::-1])
    text=text[::-1]
    recursive_string(text,i+1)
recursive_string(word)