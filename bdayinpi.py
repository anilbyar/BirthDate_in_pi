class FindBirthdateInPi:
    pi_string: str
    file = open("pi.txt", 'r')
    pi_string: str = file.readline()
    file.close()

    # Get input of birthdate
    def __init__(self):
        ask = "Enter your birthdate (DDMM): "
        print("*" * (len(ask) + 4))
        while True:
            try:
                self.birth_date = str(int(input(ask)))
                if len(self.birth_date) == 4 and int(self.birth_date[0:2]) <= 32 and int(self.birth_date[2:4]) <= 12:
                    break
                elif len(self.birth_date) != 4:
                    ask = "Please Enter your birthdate in valid format (DDMM): "
                else:
                    ask = "Please Enter a valid date: "
            except ValueError:
                ask = "Please Enter your birthdate in valid format (DDMM): "
        print("*" * (len(ask) + 4))
        print()

    # Print the location of date
    def find_date(self, pii=pi_string):
        l = len(self.birth_date)
        for i in range(1000000000 - 7):
            # print(str[i:i+l])
            if pii[i:i + l] == self.birth_date:
                print("Here is your birthdate location details:")
                print("_" * 30)
                print("Position = ", i + 1)

                # print()
                print(pii[max(i - 6, 0):min(i + 18, 1000000000 - 2)])
                if i == 0:
                    print("^" * l)
                elif i <= 5:
                    print(" " * (i - 1), "^" * l)
                else:
                    print(" " * 5, "^" * l)
                print("-" * 30)
                return
        print('Oops!, We can\'t find your birthdate in 1M digits of pi :( ')
