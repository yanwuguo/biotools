## function to take a DNA sequence input and print out its reverse complementary sequence


def RevCom(seq):
    ## Check if the input is a legal sequece:
    seq = seq.replace(" ","")
    upperseq = seq.upper()
    ## generate the reverse sequence
    rev_seq = upperseq[::-1]
    ## generate the complement sequence
    pair_dict = {'A':'T','T':'A','G':'C','C':'G'}
    rev_com = ""
    for base in rev_seq:
        rev_com = rev_com + pair_dict[base]

    return (upperseq,rev_com)


## translate input DNA sequence with six reading frame and find the longest one

aa_dict = {'CTT': ['L', 'Leu'], 'ATG': ['M', 'Met'], 'ACA': ['T', 'Thr'], 'ACG': ['T', 'Thr'], 'ATC': ['I', 'Ile'], 'AAC': ['N', 'Asn'], 'ATA': ['I', 'Ile'], 'AGG': ['R', 'Arg'], 'CCT': ['P', 'Pro'], 'ACT': ['T', 'Thr'], 'AGC': ['S', 'Ser'], 'AAG': ['K', 'Lys'], 'AGA': ['R', 'Arg'], 'CAT': ['H', 'His'], 'AAT': ['N', 'Asn'], 'ATT': ['I', 'Ile'], 'CTG': ['L', 'Leu'], 'CTA': ['L', 'Leu'], 'CTC': ['L', 'Leu'], 'CAC': ['H', 'His'], 'AAA': ['K', 'Lys'], 'CCG': ['P', 'Pro'], 'AGT': ['S', 'Ser'], 'CCA': ['P', 'Pro'], 'CAA': ['Q', 'Gln'], 'CCC': ['P', 'Pro'], 'TAT': ['Y', 'Tyr'], 'GGT': ['G', 'Gly'], 'TGT': ['C', 'Cys'], 'CGA': ['R', 'Arg'], 'CAG': ['Q', 'Gln'], 'TCT': ['S', 'Ser'], 'GAT': ['D', 'Asp'], 'CGG': ['R', 'Arg'], 'TTT': ['F', 'Phe'], 'TGC': ['C', 'Cys'], 'GGG': ['G', 'Gly'], 'TAG': ['*', 'Stp'], 'GGA': ['G', 'Gly'], 'TGG': ['W', 'Trp'], 'GGC': ['G', 'Gly'], 'TAC': ['Y', 'Tyr'], 'TTC': ['F', 'Phe'], 'TCG': ['S', 'Ser'], 'TTA': ['L', 'Leu'], 'TTG': ['L', 'Leu'], 'TCC': ['S', 'Ser'], 'ACC': ['T', 'Thr'], 'TAA': ['*', 'Stp'], 'GCA': ['A', 'Ala'], 'GTA': ['V', 'Val'], 'GCC': ['A', 'Ala'], 'GTC': ['V', 'Val'], 'GCG': ['A', 'Ala'], 'GTG': ['V', 'Val'], 'GAG': ['E', 'Glu'], 'GTT': ['V', 'Val'], 'GCT': ['A', 'Ala'], 'TGA': ['*', 'Stp'], 'GAC': ['D', 'Asp'], 'CGT': ['R', 'Arg'], 'GAA': ['E', 'Glu'], 'TCA': ['S', 'Ser'], 'CGC': ['R', 'Arg']}


def translation (seq):
    ## Check if the input is a legal sequece:
    seq = seq.replace(" ","")
    upperseq = seq.upper()
    revseq = RevCom(upperseq)
    aa = ""
    seq_aa_lst = [[],[]]
    for i in [0,1,2]:
        while i + 3 <= len(upperseq):
            aa = aa + aa_dict[upperseq[x:3+x]][0]
            aa_rev = aa_rev + aa_dict[revseq[x:3+x]][0]
            i = i + 3
        seq_aa_lst[0][i] = aa
        seq_aa_lst[1][i] = aa_rev
    return seq_aa_lst
    

for base in upperseq:
    if base not in "ATCG":
        print "Erro: Input is not a valid DNA sequence"


