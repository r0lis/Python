with open ("my_sequence.txt", "r") as txt_file:
    dna_string = txt_file.read()

# YOUR CODE HERE:
pattern = "TGA"
dna_segmented = []
segment_range = []
start_index = 0
for index in range(0, len(dna_string) - 2):
    if dna_string[index:index + 3] != pattern:
        continue
    else:
        dna_segmented.append(dna_string[start_index:index])
        segment_range.append([start_index, index - 1])
        start_index = index + 3
print(dna_segmented)
print(segment_range)

# split() method
#dna_segmented_split = dna_string.split("TGA")
#print(dna_segmented_split)