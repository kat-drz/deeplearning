path = 'dnasequence.txt'
file = open(path, 'r')

holder = file.read()
print(holder)

#remove all sequence numbers from all lines
import re
test = re.sub('1|2|3|4|5|6|7|8|9|0|>|s|e|q|S|E|Q|:', "", holder)
newone = test.split("\n")
print(newone)
newone = [x for x in newone if x != []]

#list of undesirable letters in the input sequence
bad_list = ["N", "a", "t", "g", "c"]

#checking for presence of any of the components in bad_list in sequence
result = [component for component in bad_list if(component in newone)]
    
#if undesirable letters are present in sequence, an error message is displayed

for line in newone:

    if (bool(result)) == True:
        print("The input sequence is invalid.")
        print("Please check for lowercase letters and/or 'N'.")
  
#if sequence is in the correct format, proceed with one hot encoding

    else:   
     #mapping of bases to integers as a dictionary
        bases = "ATCG"
        base_to_integer = dict((i, c) for c, i in enumerate(bases))

    #encoding input sequence as integers
    
        integer_encoded = [base_to_integer[y] for y in line]

    #one hot encoding
        onehot_encoded = list()
        for value in integer_encoded:
            base = [0 for x in range(len(bases))]
            base[value] = 1
            onehot_encoded.extend(base)
        print(onehot_encoded)
