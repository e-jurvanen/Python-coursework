import validators

def main():
    print(validate(input("What's your email? ")))

def validate(mail):
    if validators.email(mail) == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
