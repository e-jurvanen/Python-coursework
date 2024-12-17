def main():
    inp = input("Input: ")
    print(f"Output: {shorten(inp)}")

def shorten(word):
    short = ""
    for i in word:
        short += i.strip("aeiouAEIOU")
    return short

if __name__ == "__main__":
    main()
