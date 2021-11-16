
def textList(text, whitespaces):
    isWhiteSpace = lambda x: x in whitespaces

    res = []
    word = ""

    for ch in text:
        if (not isWhiteSpace(ch)):
            word += ch
        elif (word == "" and isWhiteSpace(ch)):
            continue
        else:
           res.append(word)
           word = ""
    res.append(word)
    return res

"""
isWhiteSpace - lambda function written to verificate if x is a member of whitespaces
result - list of tokens that we need to separate from whitespaces
if current character is not a member of whitespaces list we add it to word in case it is -
the algorithm checks if word is empty if it is - we coninue without making any changes
if word is not empty - we add it to result
"""

text = "Hello World \n one two \t tree wood"
whitespaces = [' ', '\n', '\t']
print(textList(text, whitespaces))

"""
whitespaces - a variable in which we indicate which characters we do not want to take into
text - string varible with the text we want to process
textList - function that take whitespaces and text variables and return string without whitespaces symbols
"""

"""['Hello', 'World', 'one', 'two', 'tree', 'wood']"""
