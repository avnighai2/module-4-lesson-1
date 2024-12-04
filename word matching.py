def matchWords(words):
    ctr = 0 
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of word with the same first and last charcter\n", lst)
    return ctr 

count = matchWords(['abc', 'cfc', 'aba', 'xyz', '1221'])
print("Number of words having first and last charcter are same:", count)