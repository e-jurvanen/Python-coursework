def main():
    while True:
        try:
            inp = input("Fraction: ")
            percent = convert(inp)
            if percent <= 100:
                break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percent))


def convert(fraction):
    x = int(fraction.split("/")[0])
    y = int(fraction.split("/")[1])
    z = round((x / y * 100))
    if z > 100:
        raise ValueError
    else:
        return z


def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{str(percentage)}%"



if __name__ == "__main__":
    main()
