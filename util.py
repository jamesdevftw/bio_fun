# Dictionary mapping codons to amino acids

amino_acid_to_binary = {
    "A": "0001", "C": "0010", "D": "0011", "E": "0100",
    "F": "0101", "G": "0110", "H": "0111", "I": "1000",
    "K": "1001", "L": "1010", "M": "1011", "N": "1100",
    "P": "1101", "Q": "1110", "R": "1111", "S": "0000",
    "T": "0010", "V": "0100", "W": "1000", "Y": "1100",
    "X": "1101", "*": "0000"
}


codon_to_amino_acid = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

def translate_codon(codon):
    """Translate a single codon to an amino acid."""
    codon = codon.upper()
    if codon in codon_to_amino_acid:
        return codon_to_amino_acid[codon]
    else:
        return "X"  # Unknown amino acid

def translate_sequence(sequence):
    """Translate a sequence of codons to a protein sequence."""
    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        amino_acid = translate_codon(codon)
        protein_sequence += amino_acid
    return protein_sequence

def save_binary_to_file(binary_string, file_path):
    print(len(binary_string))
    # Convert the binary string to bytes
    byte_data = bytes([int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)])

    # Save the bytes to a binary file
    with open(file_path, "wb") as file:
        file.write(byte_data)

def bin_to_sequence(fp):
    
    binary_digits = []

    try:
        with open(fp, "rb") as binary_file:
            byte = binary_file.read(1)
            while byte:
                binary_digits.extend(format(byte[0], '08b'))
                byte = binary_file.read(1)

        binary_string = ''.join(binary_digits)


    except FileNotFoundError:
        print(f"'{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", str(e))


    chunk_size = 4
    chunks = [binary_string[i:i+chunk_size] for i in range(0, len(binary_string), chunk_size)]

    for chunk in chunks:
        print("Chunk:", chunk)

    #Convert hex back to amino acids
    flipped_dict = {value: key for key, value in amino_acid_to_binary.items()}


def save_sequence(sequence):
	file_path = "data.bin"
	binary_data =""
	for a in sequence:
		binary_data += amino_acid_to_binary[a]

	save_binary_to_file(binary_data, file_path)
	print(f"Binary data saved to {file_path}")


# Example usage
cdna_sequence = "ATGGTGCATCGG"
mrna_sequence = cdna_sequence.replace("T", "U")

protein_cdna = translate_sequence(cdna_sequence)
protein_mrna = translate_sequence(mrna_sequence)

print("Protein (cDNA):", protein_cdna)
print("Protein (mRNA):", protein_mrna)

