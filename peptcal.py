## peptide properties calculator.
## http://biotools.nubic.northwestern.edu/proteincalc.html

#aa_dict = { "A":[name, 3 letter code, MW,Hydropathy] }
# return lenght, MW, Approximate Volume, 3 letter code
# 3 to 1 convertor.
# percentage of each aa with 3 letter code
# soluble, 
## blast domain?

and results in a protein volume of approximately:
(1.21 x MW) A3/molecule


d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
     

A, Ala	71.07793	C, Cys	103.1454	D, Asp	115.0873	E, Glu	129.1139
F, Phe	147.1734	G, Gly	57.05138	H, His	137.1394	I, Ile	113.1576
K, Lys	128.1724	L, Leu	113.1576	M, Met	131.1985	N, Asn	114.1028
P, Pro	97.11508	Q, Gln	128.1293	R, Arg	156.1861	S, Ser	87.07733
T, Thr	101.1039	V, Val	99.13103	W, Trp	186.2095	Y, Tyr	163.1728
 
		
phos-Ser	167.0573
Acetyl	43.04453	Amide	16.0228		phos-Thr	181.0838
Biotin	227.3056		phos-Tyr	243.1528

aa_dict_1to3 = {'A': ['Ala',71.0779], 'C': ['Cys',103.145], 'E': ['Glu',129.114], 'D': ['Asp',115.087], 'G': ['GLY',57.0514], 
    'F': ['Phe',147.173], 'I': ['Ile',113.158], 'H': ['His',137.139], 'K': ['Lys',128.172], 'M': ['Met',131.199], 'L': ['Leu',113.158], 
    'N': ['Asn',114.103], 'Q': ['Gln',128.129], 'P': ['Pro',97.1151], 'S': ['Ser',87.0773], 'R': ['Arg',156.186], 'T': ['Thr',101.104],
    'W': ['Trp',186.21], 'V': ['Val',99.1310], 'Y': ['Tyr',163.173]}
    
    
    
def pepCal(aa_seq):
    aa_seq_dict = dict()
    aa_dict_1to3 = {'A': ['Ala',71.0779], 'C': ['Cys',103.145], 'E': ['Glu',129.114], 'D': ['Asp',115.087], 'G': ['GLY',57.0514], 
    'F': ['Phe',147.173], 'I': ['Ile',113.158], 'H': ['His',137.139], 'K': ['Lys',128.172], 'M': ['Met',131.199], 'L': ['Leu',113.158], 
    'N': ['Asn',114.103], 'Q': ['Gln',128.129], 'P': ['Pro',97.1151], 'S': ['Ser',87.0773], 'R': ['Arg',156.186], 'T': ['Thr',101.104],
    'W': ['Trp',186.21], 'V': ['Val',99.1310], 'Y': ['Tyr',163.173]}
    NterH = 1.008	
    CterOH = 17.0074
    for aa in aa_seq:
        aa_seq_dict[aa] = aa_seq_dict.get(aa, 0) + 1
    length = sum(aa_seq_dict.values())
    Float_length = float(length)
    MV_dict = dict()
    per_dict = dict()
    for aas in aa_seq_dict.items():
        MV_dict[aas[0]] = aas[1]*(aa_dict_1to3.get(aas[0])[1])
        per_dict[aas[0]] = [aa_dict_1to3.get(aa)[0],aas[1]/Float_length]
    MV = sum(MV_dict.values()) + NterH + CterOH
    One2Three = list()
    for aa in aa_seq:
        One2Three.append(aa_dict_1to3.get(aa)[0])
    Three = "".join(aa3 for aa3 in One2Three )
    return length, MV, per_dict.items(), Three
        
    
    
    
