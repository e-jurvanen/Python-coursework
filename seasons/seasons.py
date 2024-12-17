from datetime import date
import inflect
import sys
p = inflect.engine()


def main():
    birthday = input("Date of birth: ")
    try:
        minutes = convert(birthday)
        print(f"{words(minutes).replace(" and", "").capitalize()} minutes")
    except:
        sys.exit("Invalid date")

def convert(bdate):
    bdatetime = date.fromisoformat(bdate)
    currentday = date.today()
    difference = currentday - bdatetime
    seconds = difference.total_seconds()
    minutes = seconds / 60
    return f"{minutes:.0f}"

def words(number):
    return p.number_to_words(number)


if __name__ == "__main__":
    main()
