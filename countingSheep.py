import sys
import itertools

# This function will helps in dealing with numbers having length 2 or greater i.e. 12, 34, 50 or 100 etc.
# It converts 50 into [5, 0] and 100 into [1, 0, 0]
def solve(inp):
    arr = [int(i) for i in inp]
    return arr

# Here I am reading from input file.
ReadFromFile = open("inp.txt", "r+")
getInp = ReadFromFile.read()

# Splitting the input into an array of parts.
parts = getInp.split("\n")

# This directly put 'print' statements into output file "out.txt"
sys.stdout = open("out.txt", "w")

# Running total number of test cases.
for i in range(int(parts[0])):
    if int(parts[i+1]) == 0:
        print('Case #%d: INSOMNIA' % (i+1))

    else:
        # Declaring an empty array/list of 10 i.e. [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (my background is from C++, so I use array.)
        a = [0] * 10
        # To see that the sheep has seen every number, we simply update every element of the above array. Until all the
        # elements are greater than 0. 
        
        if len(parts[i+1]) > 1: # Cheking if the length of element is greater than 1.
            getArr = solve(parts[i+1]) # Calling solve function above.
            for j in getArr:
                a[int(j)] += 1 # Incrementing elements of array.
        else:
            a[int(parts[i+1])] += 1 # Incrementing elements of array.


        x = 2; # multiplier
        res = 0 # will store the last number
        
        # Running infinite loop. This will terminate as soon as all the elements of list are greater than 0.
        for condition in itertools.count(): 
            if all(elem > 0 for elem in a): # This condition check all elements of array i.e. a[i] > 0 etc.
                print ('Case #%d: %d' % (i+1, res))
                break # Break the loop as soon as condition satisfies
                
            else:
                res = x * int(parts[i+1]) 
                if len(str(res)) > 1:
                    get = solve(str(res))
                    for g in get:
                        a[int(g)] += 1 # Incrementing elements of array.
                    x += 1 # Incrementing multipler
                else:
                    a[int(res)] += 1 # Incrementing elements of array.
                    x += 1 # Incrementing multipler
