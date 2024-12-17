import csv

def main():
    ssn = input("Finnish Social Security Number: ")
    if validate(ssn) == True:
        print("Valid")
    else:
        print("Invalid")

def validate(ssn):
    if validate_length(ssn) == False:
        return False
    elif validate_date_seperator(ssn) == False:
        return False
    elif validate_ending(ssn) == False:
        return False
    else:
        return True

# first thought was to implement date and seperator validations seperately but realised I will need the seprator validation for the date to determine the birth century -> moved the seperator validation under the date validation as well

def validate_date_seperator(ssn):
    # beginning of SSN fomatted as DDMMYY
    try:
        day = int(ssn[0]+ssn[1])
        month = int(ssn[2]+ssn[3])
        if ssn[6] == "-":
            year = int("19" + ssn[4]+ssn[5])
        elif ssn[6] == "A":
            year = int("20" + ssn[4]+ssn[5])
        else:
            return False
# could have used a library as well i.e. datetime, but wanted to try implementing it manually

        day_count_month = [0, 31, 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # first number is a placeholder 0 since there can't be a 0th month
        if int(year)%4 == 0 and (year%100 != 0 or year%400==0):
            day_count_month[2] = 29

        if 1 <= day <= day_count_month[month] and 1 <= month <= 12 and 1900 <= year <= 2099:
            return True
        else:
            return False

    except (ValueError, IndexError):
        return False


def validate_ending(ssn):
    # created a csv file with the different enging possibilities
    # remove seperator
    # divide the new number with 31 and check if matches with the ending in csv
    try:

        if ssn[6] == "-":
            splitted = ssn.split("-")
            number = splitted[0] + splitted[1]
            number = int(number[:-1]) # remove the last character
        elif ssn[6] == "A":
            splitted = ssn.split("A")
            number = splitted[0] + splitted[1]
            number = int(number[:-1]) # remove the last character
        else: # not neccessarily needed since validate_date_seperator is supposed to already catch an invalid seperator
            return False

        remainder = number%31
        last_char = ssn[10]

        with open("ending.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == str(remainder):
                    file_end = row[1]
                    break
            if file_end == str(last_char):
                return True
            else:
                return False

    except ValueError:
        return False


def validate_length(ssn):
    if len(ssn) != 11:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
