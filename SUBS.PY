#FINDING  A MOTIF IN DNA



def find_motif_positions(dna_sequence, motif):
    positions = []
    motif_length = len(motif)
    for i in range(len(dna_sequence) - motif_length + 1):
        if dna_sequence[i:i + motif_length] == motif:
            positions.append(i + 1)  # Aggiungi 1 perché le posizioni in Python iniziano da 0
    return positions

print(find_motif_positions("GATAGTCTATGATAGTCTGATAGTCCGTCGGATAGTCATCCAGGATAGTCTAGCTGCCGATAGTCCTCCAAACGATAGTCCAGATAGTCGATAGTCGGGATAGTCGCGATAGTCGGGGTCGGATAGTCACGTAATTAGTCCTGGAGATAGTCGATAGTCCAAGATAGTCCGATAGTCGATAGTCGCGATAGTCACGGATAGTCCTTGGATAGTCCCACCGTGAGATAGTCTGATAGTCCTGTGGATAGTCTGATAGTCTGATAGTCGTGATAGTCATCGGATAGTCGATAGTCTGCTTTGATAGTCACCGTATTTTGCGATAGTCTCGATAGTCGTCGATAGTCAACAAAGATAGTCGCCGATAGTCGATAGTCCCTGATAGTCAGTGTCCAGATAGTCTGAACTGATGATAGTCGATAGTCGAGGATAGTCTGGATAGTCATTCGATAGTCTTGATAGTCAATGTGATAGTCGACTCGATAGTCGATAGTCTAGGAGGATAGTCGTGATAGTCTCCTCGAGATAGTCGATAGTCTAAAGGGATAGTCGATAGTCCACGTGGGGGATAGTCTAATGATAGTCGTCCGATAGTCAGATAGTCGATAGTCGATAGTCGATAGTCGATAGTCCGATAGTCGTTCACGATAGTCGAGGATAGTCTCCCAAGTGATAGTCGATAGTCGATAGTCCTCCTGGGATAGTCAAGCCCCTGATAGTCAAGATAGTCAGACGATAGTCGATAGTCCCCGAACAAGCGATAGTCGATAGTCGATAGTCTGGATAGTCAAGATAGTCGATAGTCGATAGTCCACAGATAGTCGGATAGTCGACGATAGTCGCATGGCCGATAGTCGATAGTCGGATAGTC" , "GATAGTCGA"))
