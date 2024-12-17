def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if plate_length(s) == False:
        return False
    elif start_letters(s) == False:
        return False
    elif no_special_characters(s) == False:
        return False
    elif end_numbers(s) == False:
        return False
    elif first_number(s) == False:
        return False
    else:
        return True

def start_letters(n):
    if n[0].isdigit() or n[1].isdigit():
        return False

def plate_length(n):
    if 2 <= len(n) <=6:
        return True
    else:
        return False

def end_numbers(n):
    digits = 0
    char = 0

    while char < len(n):
        if n[char].isdigit() == True:
            if char < (len(n) - 1):
                if n[char + 1].isdigit() == False:
                    return False
            digits += 1
        char += 1
        if char == (len(n) - 1):
            return True

def first_number(n):
    char = 0
    while char < len(n):
        if n[char].isdigit() == True:
            if n[char] == '0':
                return False
            else:
                break
        char += 1

def no_special_characters(n):
    if n.isalnum():
        return True
    else:
        return False

main()
