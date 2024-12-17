# Validating a Finnish Social Security Number

by Emilia Jurvanen

Video Demo:    <https://youtu.be/knhoectg7ac>

## Description:

The purpose of this project was to do a piece of code for doing a quick validating for a Finnish Social Security Number (SSN). The code can't verify whether the SSN is actually in use, it will only check whether the SSN could technically be a valid one.

The rules for the Finnish SSN are as follows:
* The first part consist of 6 numbers from the person's birth date formatted as DDMMYY
* The birth date is followed with a seperator "-" for people born in the 1900s and "A" for people born in the 2000s (there is also "+" for 1800s but this was left out of scope)
* The latter part consist of 3 numbers randomly assigned (indentification number)
* The final character comes from the number you get when you take the birth date (DDMMYY), remove the seperator and add the indentification number after the birthdate. Then you divide the new 9 character number with 31 and the remainder will determine the final character. The possible final characters have been listed in the `ending.csv` file.
    * The first column in the `ending.csv` is the remainder, the second column is the last character

### Files:

The project consists of three seperate files:
* `project.py` is the main code that checks for the validity of the Finnish SSN
* `test_project.py` is the test code to run pytest tests for the main code
* `ending.csv` is a csv file that contains remainders and the corresponding last characters for the SSN. `ending.csv` is utilized in the code for `project.py`

### Main Code

`project.py` consists of 5 different functions. All of the additional functions take in the variable `ssn` from the main function

* `main()` asks for an input for the finnish SSN and calls for the `validate()` function to then print out whether the SSN is Valid or Invalid.
* `validate()` runs the three other validating functions. If any of them returns False, the `validate()` function will also return False. If all the other functions return True, `validate()` will also return True.
* `validate_length()` checks that the length of the input is exactly 11 characters. If not, the function will return False.
* `validate_date_seperator()` checks for the validity of the birthdate and the seperator. The first part of the code determines characters 1 & 2 as the day, characters 3 & 4 as the month, and characters 5 & 6 as the year. The year check also checks for the seperator "-" or "A" to determine whether the year should start with 19 or 20 (so whether the person was born in 1900s or 2000s). If the seperator is anything else than a "-" or "A", the function will return False. Then the code checks whether the date is a valid date. I used a list for the days of the month, so I'll match the month to the maximum number of days in that month. I also checked for the possibility of a leap year. If the year is a multiple of 400 or the year is a multiple of 4 and not a multiple of 100, then the year is a leap year and the day count for February gets changed to 29. Next the code checks whether the day count is between 1 and the max days for that month, month is between 1 and 12 and year is between 1900 and 2099. The function also has a try/except structure. If there is a typo etc, where someone tries to put something else than a number to the beginning of the SSN a ValueError will get raised and the function will return False. Similarly, if the month is outside of 1-12, the code will raise an IndexError and the function will return False.
* `validate_ending()` This function firstly splits the SSN at the seperator "-" or "A". it then creates a new number with the seperator removed and removes the last character of the SSN. Then it will check for the remainder when the new number is divided with 31. It will then open the `ending.csv` file with the built in csv module (that has been imported in the beginning of the code) and check for which character should be the last character with the remainder we got from the previous calculation. If the ending in the file matches the last character on the SSN, the function returns True. If not, it returns False. The function also contains a try/except structure to catch ValueErrors. If any of the characters that are supposed to just be numbers are not, a ValueError gets raised and the function returns False.


### Test Code

`test_project.py` consists of four different test functions:

* `test_length` checks that code works correctly when a SSN is inputted that is either too short or too long
* `test_date_and_seperator` checks that the code works properly when i.e. the date is not a real date, the seperator is not valid and the code recognises leap years correctly.
* `test_ending` checks that the code works correctly at recocnizing the correct ending characters.
* `test_typos_errors` checks that the code works correctly if there are typos (i.e. someone tries to insert letters to a part that should only contain nubers)

### Out of Scope:

The code does not work for people born in the 1800s (or 2100 or forward). The code was intended for people currently alive so there was no reason to add the checks for the older dates. This could be done fairly easily by also adding a check for "+" as a seperator the same way we've done for "-" and "A".

The code also doesn't check for the person's gender. The identification number would be even for females and odd for males. However, the code doesn't check for this one since the only input we have for the code is the SSN itself and we do not know the official goverment gender for the given person with the SSN.
