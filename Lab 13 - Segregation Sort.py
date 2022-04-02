# 1. Name:
#      Jaxon Hamm
#
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
#
# 3. Assignment Description:
#      This program uses the quick sort algorithm to recursively sort a provided array.
#
# 4. What was the hardest part? Be as specific as possible.
#      There were a few bugs that I had to work out that took me forever to spot.
#      
#      The first bug was that my algorithm for finding the pivot was doing
#      (begin + end / 2) where begin is 9, and end is 10 as 14 which is wrong.
#      Eventually I figured out it is because it was doing 9 + (10 / 2) so I just
#      added parentheses.
#      
#      The next bug that I had was that the program was defaulting i_up, i_down, and
#      i_pivot to the left value, but then I was using begining and i_up - 1 when
#      as the beginning and end values of the first sub array, and i_up and end for
#      the second sub array. This led to me having begin, i_up, and i_pivot = 4, and
#      end = 5. When calling the quicksort function that meant I was defining the first
#      sub array as starting at 4 and ending at 3, and the second sub array as starting
#      at 4 and ending at five. With this logic, the second sub array has the same start 
#      and end as the initial sub array, and thereby we reach infinite recurssion which
#      crashes the program. This took me a week to spot because I couldn't understand why
#      that was happening. The fix was just to make the first array use i_up, and the
#      second sub array use i_up + 1 because i_up was defaulting to the left. 
# 
# 5. How long did it take for you to complete the assignment?
#      More than I can really count because I worked on it all week to find some really tiny
#      bugs that were making the entire program not work.

import json

# Get the filename.
def get_filename():
    return input("What is your filename? ")

# Open a file and return the contents of it.
def open_file(filename):
    try:
        file = open(filename, 'r')
        text = file.read()
        array = json.loads(text)
    except:
        print("That is not a valid file.")
        return False

    return array

# Sort the array passed to the function recursively.
def quick_sort(array, begin, end):
    if end - begin < 1 or end < 0:
        return
    
    i_pivot = int((begin + end) / 2)
    i_up = begin
    i_down = end

    while i_up < i_down:
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
        while i_up < i_down and array[i_down] >= array[i_pivot]:
            i_down -= 1
        
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
            array[i_up], array[i_down] = array[i_down], array[i_up]

    array[i_up], array[i_pivot] = array[i_pivot], array[i_up] 

    quick_sort(array, begin, i_up)
    quick_sort(array, i_up + 1 , end)

# Display the array.
def display(array):
    print("The results of the sort are:\n", array)

# Run tests
def test_case(case, filename):
    print("CASE:", case)
    array = open_file(filename)
    quick_sort(array, 0, len(array) - 1)
    display(array)


test = input("Would you like to run the test cases? (y/n) ").lower()
if test[0] == 'y':
    test_case("Reversed List", "quicksort1.json")
    test_case("Negatives and Duplicates", "quicksort2.json")
    test_case("Empty", "quicksort3.json")
    test_case("Single Digit", "quicksort4.json")
else:
    loop = True
    while loop:
        filename = get_filename()
        array = open_file(filename)
        display(quick_sort(array, 0, len(array) - 1))
        response = input("Would you like to sort another file? (y/n) ")
        if response.lower() == 'n':
            loop = False
