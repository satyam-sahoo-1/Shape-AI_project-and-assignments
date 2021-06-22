'''This is a Python program to check whether a year is leap or not!!'''

def IsLeap(year):
    '''Checks whether a year is leap or not'''
    if (year % 4) == 0:
        return True
    else:
        return False

    


print("\nThis is a Python program to check whether a year is leap or not!!")

year = int(input("\nEnter a year (like :- 1920, 2000, etc) : "))

flag1 = IsLeap(year)
if flag1:
    print(f"Yes, {year} is leap year.\n")
else:
    print(f"No, {year} is not a leap year\n.")
