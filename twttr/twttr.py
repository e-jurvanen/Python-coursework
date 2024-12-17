def main():
    inp = input("Input: ")
    print("Output: ", end="")
    vowel_strip(inp)
    print()

def vowel_strip(word):
    for i in word:
        print(i.strip("aeiouAEIOU"), end="")

main()
