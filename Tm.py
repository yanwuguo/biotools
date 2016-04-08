### function to calculate Tm for the input DNA sequence

#Basic Melting Temperature (Tm) Calculations

#The two standard approximation calculations are used. For sequences less than 14 nucleotides the formula is
#Tm= (wA+xT) * 2 + (yG+zC) * 4
#where w,x,y,z are the number of the bases A,T,G,C in the sequence, respectively (from Marmur,J., and Doty,P. (1962) J Mol Biol 5:109-118 [PubMed]).
#For sequences longer than 13 nucleotides, the equation used is
#Tm= 64.9 +41*(yG+zC-16.4)/(wA+xT+yG+zC)
#See Wallace,R.B., Shaffer,J., Murphy,R.F., Bonner,J., Hirose,T., and Itakura,K. (1979) Nucleic Acids Res 6:3543-3557 (Abstract) and Sambrook,J., and Russell,D.W. (2001) Molecular Cloning: A Laboratory #Manual. Cold Spring Harbor Laboratory Press; Cold Spring Harbor, NY. (CHSL Press)
#ASSUMPTIONS:
#Both equations assume that the annealing occurs under the standard conditions of 50 nM primer, 50 mM Na+, and pH 7.0.

def CalTm(seq):
    ## Check if the input is a legal sequece:
    seq = seq.replace(" ","")
    upperseq = seq.upper()
    for base in upperseq:
        if base not in "ATCG":
            print "Erro: Input is not a valid DNA sequence"
    ## number of A,T,C,G in the sequence
    base_dict = dict()
    for base in upperseq:
        base_dict[base] = base_dict.get(base,0) + 1
    wA = base_dict["A"]
    xT = base_dict["T"]
    yG = base_dict["G"]
    zC = base_dict["C"]
    if len(upperseq) < 14:
        Tm= (wA+xT) * 2 + (yG+zC) * 4
    if len(upperseq) >= 14:
        Tm= 64.9 +41*(yG+zC-16.4)/(wA+xT+yG+zC)
    return Tm

