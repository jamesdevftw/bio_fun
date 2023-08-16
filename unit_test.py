
from util import translate_codon, translate_sequence, save_sequence, bin_to_sequence
import os

def compression_rate():
    file_path = "dna_input.txt"
    file_size = os.path.getsize(file_path)
    output_path = "data.bin"
    compressed_size = os.path.getsize(output_path)
    print(f"The size of '{file_path}' is {file_size} bytes.")
    compressed_rate = 100-(compressed_size/file_size)*100
    print("Compressed by: " + str(compressed_rate) + "%")

def test_translation():
    valid_codons = ["ATG", "GTA", "CAA", "TGC", "AGT", "CGC", "TGA"]
    invalid_codons = ["XYZ", "AUG", "CC", "CGAU", "UGA", ""]

    print("Testing valid codons:")
    for codon in valid_codons:
        protein_cdna = translate_codon(codon)
        print(f"cDNA Codon: {codon}, Protein: {protein_cdna}")

    print("\nTesting invalid codons:")
    for codon in invalid_codons:
        protein_cdna = translate_codon(codon)
        print(f"cDNA Codon: {codon}, Protein: {protein_cdna}")

    file_path = "dna_input.txt"  # Change this to the path of your file
    with open(file_path, "r") as file:
        dna_sequence = file.read().replace("\n", "")

    codons = ""
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        codons+=translate_codon(codon)


    bin_string = save_sequence(codons)
    bin_to_sequence("data.bin")
    compression_rate()

if __name__ == "__main__":
    test_translation()

