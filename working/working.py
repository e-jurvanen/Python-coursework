import re

def main():
    print(convert(input("Hours: ")))


def convert(inp):
    try:
        time = r"([1-9]|1[0-2])(?:\:([0-6][0-9]))? (AM|PM)"
        full_time = re.search(f"{time} to {time}", inp)
        groups = full_time.groups()
        return time_convert(groups[:3]) + " to " + time_convert(groups[3:])
    except AssertionError:
        raise ValueError
    except AttributeError:
        raise ValueError

def time_convert(time):
    hours = time[0]
    if time[2] == "PM":
        if time[0] == "12":
            hours = 12
        else:
            hours = int(time[0]) + 12
    if time[2] == "AM":
        if time[0] == "12":
            hours = "00"
        elif int(time[0]) < 10:
            hours = "0" + time[0]
        else:
            hours = time[0]

    if time[1] == None:
        minutes = "00"
    elif int(time[1]) > 59:
        raise ValueError
    else:
        minutes = time[1]

    return f"{hours}:{minutes}"

if __name__ == "__main__":
    main()
