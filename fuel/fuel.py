def main():
    percent = inpu()
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(str(percent) + "%")

def inpu():
    while True:
        try:
            inp = input("Fraction: ")
            percent = fractions(inp)
            if percent <= 100:
                return percent
        except (ValueError, ZeroDivisionError):
            pass

def fractions(frac):
    x = int(frac.split("/")[0])
    y = int(frac.split("/")[1])
    z = round((x / y * 100))
    return z

main()
