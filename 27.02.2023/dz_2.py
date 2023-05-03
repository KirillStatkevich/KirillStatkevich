word="ΝΙΨΟΝΑΝΟΜΗΜΑΤΑΜΗΜΟΝΑΝΟΨΙΝ"

def palidrom(text):
    if text[0]!=text[-1]:
        return False
    if len(text)<=1:
        return True
    return palidrom(text[1:-1])
print(palidrom(word))