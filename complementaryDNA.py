#Complementary DNA challenge

def DNA_strand(dna):
    output = []
    for l in dna:
        if l == 'T':
            output.append('A')
        elif l == 'A':
            output.append('T')
        elif l == 'C':
            output.append('G')
        elif l == 'G':
            output.append('C')
    return ''.join(output)
    
    
Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
