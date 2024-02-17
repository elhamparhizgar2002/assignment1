def subs(s,t):
    l=[]
    p=0
    while p<len(s) and t in s[p:]:
        p1=s.index(t,p)
        l.append(p1+1)
        p=p1+1
    return l

s='GATATATGCATATACTT'
t='ATAT'
print(subs(s,t))