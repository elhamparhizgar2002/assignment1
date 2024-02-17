def cons(collection):
    m_A=[]
    m_C=[]
    m_G=[]
    m_T=[]
    s = 'ACGT'
    consensus = ''
    for j in range(len(collection[0])):
        count_A=0
        count_C=0
        count_G=0
        count_T=0
        for i in range(len(collection)):
            if collection[i][j]=='A':
                count_A+=1
            if collection[i][j] == 'C':
                count_C += 1
            if collection[i][j] == 'G':
                count_G += 1
            if collection[i][j] == 'T':
                count_T += 1
        m_A.append(count_A)
        m_C.append(count_C)
        m_G.append(count_G)
        m_T.append(count_T)
        l=[count_A,count_C,count_G,count_T]
        consensus+=s[l.index(max(l))]
    profile=[m_A,m_C,m_G,m_T]
    return profile,consensus

collection=[
'ATCCAGCT',
'GGGCAACT',
'ATGGATCT',
'AAGCAACC',
'TTGGAACT',
'ATGCCATT',
'ATGGCACT'
]
print(cons(collection))