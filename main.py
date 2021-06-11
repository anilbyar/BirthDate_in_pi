from bdayinpi import *

while True:
    # Create an object of date finder
    birthday = FindBirthdateInPi()
    birthday.find_date()  # Print Details
    print()
    if input("Type 'exit' if you want to exit: ") == 'exit':
        break
    else:
        print()
