months = [
    "January",
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
    "December"
]

def main():
    while True:
        date = input("Date: ")
        try:
            day = date.split("/")[1]
            month = date.split("/")[0]
            year = date.split("/")[2]
            if 0 < int(month) <= 12 and 0 < int(day) <= 31:
                print(year.strip(), f"{int(month):02}", f"{int(day):02}", sep="-")
                break
        except:
            try:
                if "," not in date:
                    raise SyntaxError
                else:
                    month = date.split(" ")[0]
                    month = months.index(month) + 1
                    day = str(date.split(" ")[1]).strip(",")
                    year = date.split(" ")[2]

                    if 0 < int(month) <= 12 and 0 < int(day) <= 31:
                        print(year.strip(), f"{(month):02}", f"{int(day):02}", sep="-")
                        break
            except:
                pass

main()
