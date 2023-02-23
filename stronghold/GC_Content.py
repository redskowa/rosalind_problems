def readFile(filePath):
    '''Reading a file and returning a list of lines'''
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    '''GC content ration in a DNA/RNA sequence'''
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100, 6)


# === Read data from file (FASTA formatted file)
# Storing File contents in a list
FASTAFile = readFile("rosalind_problems/test_data/gc_content.txt")
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""


# === Clean/Prepare the data (format for ease of use with gc_content function)
# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print(FASTADict)

# === Format the data (store the data in convenient way)
# === Run needed operation on the data (pass to gc_content function)
# Using Dictionary Comprehension to generate a new dictionary with GC Content as the value rather than the strand
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

print(RESULTDict)

# Looking for max value in values() of the results dictionary
MaxGCKey = max(RESULTDict, key=RESULTDict.get)

# === Collect the results (Rosalind submission)
print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')