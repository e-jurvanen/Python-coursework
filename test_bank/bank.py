def main():
    greet = input("Greeting: ")
    print(f"${value(greet)}")


def value(greeting):
    if greeting.lower().strip().startswith("hello") == True:
        return 0
    elif greeting.lower().strip().startswith("h") == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
