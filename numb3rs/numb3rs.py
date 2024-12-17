import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d*)\.(\d*)\.(\d*)\.(\d*)$", ip):
        no = 1
        while no <=4:
            if int(matches.group(no)) > 255:
                return False
            no += 1
        return True

    else:
        return False

if __name__ == "__main__":
    main()
