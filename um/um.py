import re

def main():
    print(count(input("Text: ")))


def count(text):
    count = re.findall(r"\bum\b", text, flags=re.IGNORECASE)
    return(len(count))

if __name__ == "__main__":
    main()
