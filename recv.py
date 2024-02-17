def recv(s):
    rev=s[::-1]
    sc=''
    for c in rev:
        if c=='T':
            sc+='A'
        elif c=='A':
            sc+='T'
        elif c=="C":
            sc+="G"
        elif c=="G":
            sc+="C"
    return sc

print(recv("AAAACCCGGT"))
'''
ACCGGGTTTT
ACCGGGTTTT
'''