def gc(dataset_name):
    dna_strings={}
    f=open(dataset_name)
    id=""
    s=""
    for row in f:
        row=row.strip()
        if row:
            if row.startswith(">"):
                if id:
                    dna_strings[id]=s
                id=row[1:]
                s=""
            else:
                s+=row
    f.close()
    if id not in dna_strings:
        dna_strings[id]=s
    pmax=-1
    idmax=""
    for id in dna_strings:
        s=dna_strings[id]
        p=(s.count("C")+s.count("G"))/len(s)
        if p>pmax:
            pmax=p
            idmax=id
    return idmax,pmax*100

print(gc("gc_dataset.txt"))

