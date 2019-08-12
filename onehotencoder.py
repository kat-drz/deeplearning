import sys

path = sys.argv[1]
file = open(path, 'r')

holder = file.read()
holder1 = str(holder)
holder2 = holder1.replace("\n","")
uppercase = holder2.upper()

#remove all sequence numbers from all lines
import re
test = re.sub('1|\t|2|3|4|5|6|7|8|9|0|SEQ|CHR|-|:', "", uppercase)
newone = test.split(">")
newone = [x for x in newone if x]

#checking for presence of N in sequence
lettern = "N"
result = [component for component in lettern if(component in newone)]
    
#if N is present in sequence, an error message is displayed

for line in newone:

    if (bool(result)) == True:
        print("The input sequence is invalid, N is present.")
        sys.exit()
  
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
