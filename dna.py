def dna(s):
    count_A=s.count("A")
    count_C = s.count("C")
    count_G = s.count("G")
    count_T = s.count("T")
    return str(count_A)+" "+str(count_C)+" "+str(count_G)+" "+str(count_T)

print(dna("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

'''
count_A=s.count("A")
count_C = s.count("C")
count_G = s.count("G")
count_T = s.count("T")
print(str(count_A)+" "+str(count_C)+" "+str(count_G)+" "+str(count_T))
'''