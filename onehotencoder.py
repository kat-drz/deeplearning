#possible input values
bases = "ATCG"

#mapping of bases to integers as a dictionary
base_to_integer = dict((i, c) for c, i in enumerate(bases))
print(base_to_integer)

#example input sequence to be one hot encoded
sequence = "AGATATAC"

#encoding input sequence as integers
integer_encoded = [base_to_integer[y] for y in sequence]
print(integer_encoded)

#one hot encoding
onehot_encoded = list()
for value in integer_encoded:
    base = [0 for x in range(len(bases))]
    base[value] = 1
    onehot_encoded.append(base)
    
print(onehot_encoded)



      
