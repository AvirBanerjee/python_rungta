def rev_sentence(str):
    words=str.split() #['Doing', 'Coding', 'IS', 'HELL']
    n=len(words)
    result=""

    for i in range(n-1,-1,-1):
        result= result+" "+words[i]

    return result          

value="Doing Coding IS HELL"
print(rev_sentence(value))