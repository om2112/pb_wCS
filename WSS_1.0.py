'''
    author:om2112@github
    this programm prints all words in sentace which comes before and after comma(')
    without repitation


'''
def csplit(string, index, sign): #function thar returns words before and after comma(,)
    i = index
    while string[i] != ' ': #word before comma(,)
        if i-1 >= 0 and string[i-1] != ' ' and string[i-1] != sign:
            i=i-1
        else:
            i=i
            break
    word0 = ''.join(string[i:index:1])  #creas word from given index of comma to balnk space before word
    i = index
    while string[i] != ' ' :    #word after comma(,)
        if i+1 > len(string)-1:
            i = i
            break
        else:
            if string[i+1] != ' ' and  string[i+1] != sign:
                i = i+1
            else:
                i=i
                break
    word1 = ''.join(string[index+1:i+1:1])  #creas word from given index of comma to balnk space after word
    if word0 != "" and word1 == "": #returns no of words and words
        return 1,word0
    elif word0 == "" and word1 != "":
        return 1,word1
    else:
        return 2,word0, word1
    
def cm_split(string, sign): #function that returns all words after and before comma(')
    i=0
    tword0=[]    #empty list of words
    for ch in string:   #fatches words from string using csplit function
        if  ch == sign:  
            b = csplit(string,i,sign)
            j = 0
            tword0 = tword0 + list(b[j+1:])   #adds words to list tword
        i=i+1
    j = 0
    while j<len(tword0): #remove repeat elements from list
        count = tword0.count(tword0[j])
        if count == 1:
            j = j+1
        else:
            tword0.remove(tword0[j])
            j = 0
    return tword0
        
string = input("Please enter a string:")
sign = input("Please enter a sign:")

print(cm_split(string, sign))

