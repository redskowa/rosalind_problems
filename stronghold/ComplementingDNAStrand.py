
DNA_Complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

## === Reverse Complement === ##
def reverse_complement(seq):
    '''Swapping adenine with thymine and guanine with cytosine. Then reversing generated string. 5' to 3' order'''
    return ''.join([DNA_Complement[nuc] for nuc in seq])[::-1]

print(reverse_complement("CCAGTGCGTTTCGTCAGGAGATAGGTGGGGGTACTGAGCGGCGACTCGGCATTGCTCCAAATAATGACAGGAGCAGAGCAAAAAAGTGTCGTCGACCTCAAATTTGGGTCCTAAACTTCTAAATCGGAGCCAAATGGCCGAGCCCTGGAGTGGCCGGACGTACTGGTCCCAGTTTGCCGGAAGTCACCTCCCTGCGAGCGTTATGTCATGCTGACACATAATTTTGTGGGTGACTAAATTCGATCGATGCCAGGAGTGGCCTCCCACATATACTCCCCCCCACGGGTCCATTGGATATATCTCTTGTACTTCAATCTAACATGGAGAATTCCCACAAGCCGACTCGCATAGGCCAAGCACCAACATTATGCGGTAGCCTTTTTCCTCGTAGCGCATTCCTGAGTAACAGTTGGAAAGAAGGTCACAGCCTCCTCACCTTTGGTACCGCCAGATCCGCATGACATACCTGCCCTGAAAGCTAGATGTGCAAGTGTTAAGATTCAACCGGCTAAGCGATATTACTAGGAACGATCGGTCCGAAGCCGGATTTGCCTGCGCTCGAGCACCTACTTCCATTGCTGTCCCTCACAGTGGAGCTGAACACAATTCTTCACCCCAAGGACATCTAGCCTCCACTTGGACGCGGATACGGATAAGTTCTCCTTCTATCTAGTACCATCGGATTGGCAGGCACAAAGAAATATGAGTTCAGTTTATGCTGCAGCCTCTATCATGGATTGAGAATGCTTGCTCCTAATACATAAGGGGAAACAGCTAGAACGTCCGATGGGTCCATTCACCCCCTCATATGCCCAAGCGATTTACAG"))