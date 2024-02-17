def hamm(s,t):
    d=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            d+=1
    return d

print(hamm('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'))
