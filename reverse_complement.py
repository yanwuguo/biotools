## function to take a DNA sequence input and print out its reverse complementary sequence
def RevCom(seq):
    ## Check if the input is a legal sequecee
    ## generate the reverse sequence
    rev_seq = upperseq[::-1]
    ## generate the complement sequence
    pair_dict = {'A':'T','T':'A','G':'C','C':'G'}
    rev_com = ""
    for base in rev_seq:
        rev_com = rev_com + pair_dict[base]

    return (upperseq,rev_com)



    
    
