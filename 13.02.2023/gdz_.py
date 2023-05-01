with open("leson13.02.2023/text.txt") as f:
    lines = f.readlines()
    max_width = 40 
    result = ""
    col = 0
    for line in lines:
        for word in line.split():
            end_col = col + len(word)
            if col != 0:
                end_col += 1
            if end_col > max_width: 
                result += '\n'
                col = 0    
            if col != 0:
                result += ' ' 
                col += 1
            result += word 
            col += len(word)
        print (result)