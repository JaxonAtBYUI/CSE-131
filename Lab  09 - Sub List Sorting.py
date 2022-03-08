# 1. Name:
#      Jaxon Hamm
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      Sort a list of values by breaking it up into smaller sub lists.
# 4. What was the hardest part? Be as specific as possible.
#      Honestly, after having done all the design, I just went through and
#      it worked the first time with no errors.
# 5. How long did it take for you to complete the assignment?
#      1 hour

import json

# Get the filename from the user.
def get_filename():
    return input("What is the filename: ")
    

# Read the board and return the array inside of the file.
def read_file(filename):
    try:
        file = open(filename, 'r')
        text = file.read()
        array = json.loads(text)
        
    except:
        print("ERROR: Invalid File")
        return
    return array

# Disply the array after sorting it.
def display(array):
    print("The results of the sort are: \n", array)
    return

# Break the array up into sub lists and then merge the 
# lists together to sort the list piece by piece.
def sort(array):
    size = len(array)
    src = array
    des = [None] * size

    # Each iteration through the list.
    merges = 2
    while merges > 1:
        merges = 0
        begin1 = 0

        # Go through each sublist and sort it in ascending order
        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 +=1
            
            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and src[end2 - 1] <= src[end2]:
                end2 += 1

            merges += 1
            combine(src, des, begin1, begin2, end2)
            begin1 = end2
        src, des = des, src

    return src

# Combine the two smaller lists into a bigger list on the destination array
def combine(source, destination, begin1, begin2, end2):
    end1 = begin2

    for i in range(begin1, end2):
        if (begin1 < end1) and (begin2 == end2 or source[begin1] < source[begin2]):
            destination[i] = source[begin1]
            begin1 += 1
        else:
            destination[i] = source[begin2]
            begin2 += 1
    return

# Choose the mode that the program is running in
def runtime():
    print("What would you like to do?")
    print("- Test cases")
    print("- Sort List")
    choice = input("> ")

    if choice[0].lower() == 't':
        test_cases("Unsorted list", "mergeUnsorted.json")
        test_cases("All the same value", "mergeAllZero.json")
        test_cases("Negative Values", "mergeNegatives.json")
        test_cases("Tiny list", "mergeTiny.json")
        test_cases("Empty list", "empty.json")
        test_cases("Large List", "mergeLarge.json")
        input("Enter anything to continue")
        
    else:
        repeating = True
        while repeating:

            # Sort a file with an array in it
            filename = get_filename()
            array = read_file(filename)
            array = sort(array)
            display(array)

            # See if they want to sort another file
            if input("Would you like to sort something else? (y/n) ").lower() == "n":
                repeating = False

# Run test cases
def test_cases(test, filename):
    print("TEST CASE: " + test)
    array = read_file(filename)
    array = sort(array)
    print(array)

# The entire program stems from here
runtime()
