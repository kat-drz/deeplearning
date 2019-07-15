#list of all possible bases
bases = "ATCG"

#input sequence for one hot encoding
sequence = "AGATATAC"

#list of undesirable letters in the input sequence
bad_list = ["N","a","t", "g", "c"]

#checking for presence of any of the components in bad_list in sequence
result = [component for component in bad_list if(component in sequence)]

#if undesirable letters are present in sequence, an error message is displayed
if (bool(result)) == True:
    print("The input sequence is invalid.")
    print("Please check for lowercase letters and/or 'N'.")
  
#if sequence is in the correct format, proceed with one hot encoding
else:
     #mapping of bases to integers as a dictionary
    base_to_integer = dict((i, c) for c, i in enumerate(bases))

    #encoding input sequence as integers
    integer_encoded = [base_to_integer[y] for y in sequence]

    #one hot encoding
    onehot_encoded = list()
    for value in integer_encoded:
        base = [0 for x in range(len(bases))]
        base[value] = 1
        onehot_encoded.extend(base)
    print(onehot_encoded)
