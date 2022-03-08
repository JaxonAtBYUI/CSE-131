# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      A calendar for any month of any year from 1753 forward.
#
# 4. What was the hardest part? Be as specific as possible.
#      
# 
# 
#
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

#CONSTANTS
MONTH_DATA =  [[31, 28, 31,
            30, 31, 30,
            31, 31, 30,
            31, 30, 31],
            ["January",
            "February", 
            "March", 
            "April", 
            "May", 
            "June", 
            "July", 
            "August", 
            "September", 
            "October", 
            "November", 
            "December"]]

# Get the month number from the user and validate it.
def get_month():
    month = -1
    invalid = True
    
    while invalid:
        month = input("Enter a month number: ")
        if month.isnumeric() and (0 < int(month) < 13):
            return int(month)
        print("ERROR: Please enter a number between 1 and 12.")
        
# Get the year from the user and validate it.
def get_year():
    year = 0
    invalid = True

    while invalid:
        year = input("Enter year: ")
        if year.isnumeric() and (int(year) >= 1753):
            return int(year)
        print("ERROR: Enter a year after 1753.")

# Display the calendar
def display(year, month):
    # Display the header of the Calendar.
    print(MONTH_DATA[1][month-1] + ", " + str(year))
    print("  Su  Mo  Tu  We  Th  Fr  Sa")
    
    # Get the offset.
    offset = find_offset(year, month)
    
    # Get the days in the month. (Take care of February).
    days_in_month = 0
    if month == 2 and is_leap(year):
        days_in_month = 29
    else:
        days_in_month = MONTH_DATA[0][month-1]
    
    # Move over the alloted spaces.
    for move in range(0, offset):
        print('    ', end='')

    # Prints the month
    for dom in range(1, days_in_month+1):
        # Wrap to the beginning of the week.
        if offset == 7:
            offset = 0
            print()
        
        # Print the day.
        if dom < 10:
            print('   ' + str(dom), end='')
        else:
            print('  ' + str(dom), end='')

        # Check which day we are on.
        offset += 1
    
    print()

# Finds which day of the week the month starts on.
def find_offset(year, month):
    total_days = 0

    # Count years between 1753 and the year, convert to days and add to sum.
    for years in range(1753, year):
        if is_leap(years):
            total_days += 366
        else:
            total_days += 365

    # Count the months between beginning of year and current month, add to sum.
    for months in range(0, month-1):
        if months == 1 and is_leap(year):
            total_days += 29
        else:
            total_days += MONTH_DATA[0][months]
    
    # Jan 1st, 1753 is a monday. This calendar starts on sunday, not monday.
    # To fix this we subtract 1 from the sum before calculations.
    total_days += 1
    
    return total_days % 7

# Decides whether or not somthing is a leap year.
def is_leap(year):
    if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
        return True
    return False

def test_case(case, year, month):
    print("TEST CASE:" + case)
    display(year, month)
    print()

# Here are the test cases not requiring user input.
test_case("January 1753", 1753, 1)
test_case("February 1753", 1753, 2)
test_case("January 1754", 1754, 1)
test_case("February 1756", 1756, 2)
test_case("February 1800", 1800, 2)
test_case("February 2000", 2000, 2)

# Actually run the program
month = get_month()
year = get_year()
display(year, month)
input()

