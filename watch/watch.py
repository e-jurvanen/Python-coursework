import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(html):
    try:
        url = re.search(r"<iframe.*https?://(?:www\.)?youtube\.com/embed/(\w*)", html)
        return f"https://youtu.be/" + url.group(1)
    except AttributeError:
        return "None"

if __name__ == "__main__":
    main()
